import tkinter as tk
from tkinter import colorchooser, filedialog, simpledialog
from PIL import Image, ImageDraw

class UltimatePaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Ultimate Paint")
        self.root.geometry("1000x750")

        # 초기 설정
        self.brush_color = "black"
        self.bg_color = "white"
        self.brush_size = 5
        self.tool = "brush"  # brush, eraser, rect, oval, line, bucket, text

        # 그리기 좌표 및 객체 기록
        self.last_x, self.last_y = None, None
        self.start_x, self.start_y = None, None
        self.temp_shape = None

        # ------------------ 상단 툴바 UI ------------------
        toolbar = tk.Frame(root, bg="#f0f0f0", bd=1, relief=tk.RAISED)
        toolbar.pack(side="top", fill="x")

        # 1. 그리기 도구 그룹
        draw_group = tk.LabelFrame(toolbar, text="도구")
        draw_group.pack(side="left", padx=5, pady=2)
        tk.Button(draw_group, text="🖌️", width=3, command=lambda: self.set_tool("brush")).pack(side="left")
        tk.Button(draw_group, text="🧽", width=3, command=lambda: self.set_tool("eraser")).pack(side="left")
        tk.Button(draw_group, text="🪣", width=3, command=lambda: self.set_tool("bucket")).pack(side="left")
        tk.Button(draw_group, text="Text", width=4, command=lambda: self.set_tool("text")).pack(side="left")

        # 2. 도형 도구 그룹
        shape_group = tk.LabelFrame(toolbar, text="도형")
        shape_group.pack(side="left", padx=5, pady=2)
        tk.Button(shape_group, text="📏", width=3, command=lambda: self.set_tool("line")).pack(side="left")
        tk.Button(shape_group, text="⬛", width=3, command=lambda: self.set_tool("rect")).pack(side="left")
        tk.Button(shape_group, text="⚪", width=3, command=lambda: self.set_tool("oval")).pack(side="left")

        # 3. 설정 그룹 (색상, 크기)
        settings_group = tk.LabelFrame(toolbar, text="설정")
        settings_group.pack(side="left", padx=5, pady=2)
        self.color_btn = tk.Button(settings_group, bg=self.brush_color, width=3, command=self.choose_color)
        self.color_btn.pack(side="left", padx=5)
        
        tk.Label(settings_group, text="크기:").pack(side="left")
        self.size_slider = tk.Scale(settings_group, from_=1, to=50, orient="horizontal", length=100)
        self.size_slider.set(5)
        self.size_slider.pack(side="left")

        # 4. 파일 액션
        tk.Button(toolbar, text="💾 저장", command=self.save_image).pack(side="right", padx=5)
        tk.Button(toolbar, text="❌ 비우기", command=self.clear_canvas).pack(side="right", padx=5)

        # ------------------ 캔버스 설정 ------------------
        self.canvas = tk.Canvas(root, bg=self.bg_color, width=1000, height=650, cursor="cross")
        self.canvas.pack(fill="both", expand=True)

        # PIL 이미지 (저장용)
        self.image = Image.new("RGB", (1000, 650), self.bg_color)
        self.draw = ImageDraw.Draw(self.image)

        # 마우스 이벤트 바인딩
        self.canvas.bind("<Button-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

    def set_tool(self, tool):
        self.tool = tool

    def choose_color(self):
        color = colorchooser.askcolor(title="색상을 고르세요")[1]
        if color:
            self.brush_color = color
            self.color_btn.config(bg=color)

    def on_press(self, event):
        self.start_x, self.start_y = event.x, event.y
        self.last_x, self.last_y = event.x, event.y

        # 페인트통(채우기) 기능은 클릭 즉시 실행
        if self.tool == "bucket":
            # Pillow의 floodfill은 RGB 튜플이 필요함
            rgb_color = self.root.winfo_rgb(self.brush_color)
            rgb_color = (rgb_color[0]//256, rgb_color[1]//256, rgb_color[2]//256)
            ImageDraw.floodfill(self.image, (event.x, event.y), rgb_color, thresh=10)
            self.refresh_canvas()
        
        # 텍스트 도구는 클릭한 위치에 입력창 띄움
        elif self.tool == "text":
            text = simpledialog.askstring("입력", "넣을 글자를 입력하세요:")
            if text:
                size = self.size_slider.get() * 2
                # 화면에 그리기
                self.canvas.create_text(event.x, event.y, text=text, fill=self.brush_color, 
                                        font=("Arial", size), anchor="nw")
                # 이미지에 저장
                self.draw.text((event.x, event.y), text, fill=self.brush_color)

    def on_drag(self, event):
        size = self.size_slider.get()
        color = self.bg_color if self.tool == "eraser" else self.brush_color

        if self.tool in ["brush", "eraser"]:
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y,
                                    fill=color, width=size, capstyle=tk.ROUND, smooth=True)
            self.draw.line([self.last_x, self.last_y, event.x, event.y], fill=color, width=size)
            self.last_x, self.last_y = event.x, event.y

        elif self.tool in ["rect", "oval", "line"]:
            if self.temp_shape:
                self.canvas.delete(self.temp_shape)
            
            if self.tool == "rect":
                self.temp_shape = self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y, 
                                                               outline=self.brush_color, width=size)
            elif self.tool == "oval":
                self.temp_shape = self.canvas.create_oval(self.start_x, self.start_y, event.x, event.y, 
                                                          outline=self.brush_color, width=size)
            elif self.tool == "line":
                self.temp_shape = self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, 
                                                          fill=self.brush_color, width=size)

    def on_release(self, event):
        size = self.size_slider.get()
        if self.tool == "rect":
            self.draw.rectangle([self.start_x, self.start_y, event.x, event.y], outline=self.brush_color, width=size)
        elif self.tool == "oval":
            self.draw.ellipse([self.start_x, self.start_y, event.x, event.y], outline=self.brush_color, width=size)
        elif self.tool == "line":
            self.draw.line([self.start_x, self.start_y, event.x, event.y], fill=self.brush_color, width=size)
        
        self.temp_shape = None

    def refresh_canvas(self):
        """Pillow 이미지를 Tkinter 캔버스에 동기화 (주로 bucket 사용 후)"""
        # 임시 저장을 통해 화면 갱신 (효율적이지는 않으나 가장 확실한 방법)
        self.canvas.delete("all")
        from PIL import ImageTk
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, image=self.tk_image, anchor="nw")

    def clear_canvas(self):
        self.canvas.delete("all")
        self.image = Image.new("RGB", (1000, 650), self.bg_color)
        self.draw = ImageDraw.Draw(self.image)

    def save_image(self):
        file = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG", "*.png"), ("JPG", "*.jpg")])
        if file:
            self.image.save(file)

if __name__ == "__main__":
    root = tk.Tk()
    UltimatePaintApp(root)
    root.mainloop()

