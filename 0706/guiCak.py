import math
import tkinter as tk
from tkinter import font

# ===== 상태 관리 =====
current_expr = ""  # 현재 입력된 수식
history_list = []  # 저장된 계산 기록 리스트 (최대 5개)


def press(key):
    """버튼 클릭 및 키보드 입력 처리"""
    global current_expr

    if key == "C":
        current_expr = ""
    elif key == "⌫" or key == "Backspace":
        current_expr = current_expr[:-1]
    elif key == "=" or key == "Return":
        if not current_expr:
            return

        try:
            # 특수 기호 치환
            expr = (
                current_expr.replace("÷", "/")
                .replace("×", "*")
                .replace("π", "math.pi")
                .replace("e", "math.e")
                .replace("sin(", "math.sin(math.radians(")
                .replace("cos(", "math.cos(math.radians(")
                .replace("tan(", "math.tan(math.radians(")
                .replace("log(", "math.log10(")
                .replace("ln(", "math.log(")
                .replace("√(", "math.sqrt(")
            )

            # 괄호 자동 보정
            open_count = expr.count("(")
            close_count = expr.count(")")
            if open_count > close_count:
                expr += ")" * (open_count - close_count)

            result = eval(expr)

            if isinstance(result, float) and result.is_integer():
                result = int(result)
            elif isinstance(result, float):
                result = round(result, 10)

            current_expr = str(result)
        except Exception:
            current_expr = "오류"
    elif key in ["sin", "cos", "tan", "log", "ln", "√"]:
        current_expr += f"{key}("
    elif key == "x²":
        current_expr += "**2"
    elif key == "xʸ":
        current_expr += "**"
    else:
        if key in ["+", "-", "×", "÷"] and (
            not current_expr or current_expr[-1] in ["+", "-", "×", "÷"]
        ):
            return
        current_expr += str(key)

    # 화면 갱신
    display_label.config(text=current_expr if current_expr else "0")


# ===== 💡 새로운 기능: 수동 저장 및 리셋 로직 =====
def save_to_history():
    """현재 디스플레이에 있는 값을 기록에 수동 저장"""
    global history_list
    val = display_label.cget("text")

    # '0'이거나 '오류'인 경우는 저장하지 않음
    if val in ["0", "오류"]:
        return

    # 이미 기록에 있는 값이면 중복 저장 방지
    if val in history_list:
        return

    # 최신 기록을 맨 위에 추가
    history_list.insert(0, val)

    # 5개까지만 유지
    if len(history_list) > 5:
        history_list.pop()

    update_history_display()


def clear_history():
    """저장된 기록을 모두 삭제 (리셋)"""
    global history_list
    history_list.clear()
    update_history_display()


def update_history_display():
    """우측 기록 레이블 갱신"""
    for label in history_labels:
        label.config(text="")

    for i, record in enumerate(history_list):
        history_labels[i].config(text=f"📌 {record}")


def key_input(event):
    """키보드 입력 매핑"""
    key = event.char
    keysym = event.keysym

    if key in "0123456789.+-()pi":
        press(key)
    elif key == "*":
        press("×")
    elif key == "/":
        press("÷")
    elif key == "^":
        press("xʸ")
    elif keysym in ["Return", "KP_Enter"]:
        press("=")
    elif keysym == "Backspace":
        press("⌫")
    elif keysym == "Escape":
        press("C")


# ===== GUI 레이아웃 구성 =====
root = tk.Tk()
root.title("공학용 계산기 (수동 기록 제어)")
root.geometry("820x500")
root.configure(bg="#f3f3f3")
root.resizable(False, False)

root.bind("<Key>", key_input)

display_font = font.Font(family="Segoe UI", size=32, weight="bold")
btn_font = font.Font(family="Segoe UI", size=12)
history_font = font.Font(family="Segoe UI", size=12, weight="bold")

# 레이아웃 분할
left_body = tk.Frame(root, bg="#f3f3f3")
left_body.pack(side="left", fill="both", expand=True)

right_panel = tk.Frame(root, bg="#fcfcfc", bd=1, relief="solid")
right_panel.pack(side="right", fill="both", padx=10, pady=10)

# --- [좌측] 계산기 구성 ---
display_label = tk.Label(
    left_body,
    text="0",
    anchor="e",
    font=display_font,
    bg="#f3f3f3",
    fg="#000000",
    padx=15,
    pady=20,
)
display_label.pack(fill="x", expand=True)

main_frame = tk.Frame(left_body, bg="#f3f3f3")
main_frame.pack(fill="both", expand=True, padx=5, pady=5)

sci_frame = tk.Frame(main_frame, bg="#f3f3f3")
sci_frame.pack(side="left", fill="both", expand=True, padx=2)

std_frame = tk.Frame(main_frame, bg="#f3f3f3")
std_frame.pack(side="right", fill="both", expand=True, padx=2)

for i in range(5):
    sci_frame.rowconfigure(i, weight=1)
    std_frame.rowconfigure(i, weight=1)
for i in range(3):
    sci_frame.columnconfigure(i, weight=1)
for i in range(4):
    std_frame.columnconfigure(i, weight=1)

# --- [우측] 기록 제어 패널 구성 ---
history_title = tk.Label(
    right_panel,
    text="나의 저장 내역 (최대 5개)",
    font=font.Font(family="Segoe UI", size=12, weight="bold"),
    bg="#fcfcfc",
    anchor="w",
    padx=10,
    pady=10,
)
history_title.pack(fill="x")

# 💡 기능 버튼 프레임 (저장 / 리셋)
ctrl_frame = tk.Frame(right_panel, bg="#fcfcfc")
ctrl_frame.pack(fill="x", padx=10, pady=5)

save_btn = tk.Button(
    ctrl_frame,
    text="현재 값 저장",
    font=font.Font(family="Segoe UI", size=10),
    bg="#e1dfdd",
    relief="flat",
    command=save_to_history,
)
save_btn.pack(side="left", fill="x", expand=True, padx=2)

clear_btn = tk.Button(
    ctrl_frame,
    text="기록 리셋",
    font=font.Font(family="Segoe UI", size=10),
    bg="#fde7e9",
    fg="#a80000",
    relief="flat",
    command=clear_history,
)
clear_btn.pack(side="right", fill="x", expand=True, padx=2)

# 기록 표시용 레이블 5개
history_labels = []
for i in range(5):
    lbl = tk.Label(
        right_panel,
        text="",
        font=history_font,
        bg="#fcfcfc",
        fg="#0078d4",  # 저장된 값은 파란색 강조
        anchor="e",
        padx=10,
        pady=10,
    )
    lbl.pack(fill="x")
    history_labels.append(lbl)

# ===== 버튼 데이터 및 생성 =====
sci_buttons = [
    ("sin", 0, 0),
    ("cos", 0, 1),
    ("tan", 0, 2),
    ("ln", 1, 0),
    ("log", 1, 1),
    ("√", 1, 2),
    ("x²", 2, 0),
    ("xʸ", 2, 1),
    ("(", 2, 2),
    ("π", 3, 0),
    ("e", 3, 1),
    (")", 3, 2),
    ("C", 4, 0),
    ("⌫", 4, 1),
]

std_buttons = [
    ("÷", 0, 2),
    ("×", 0, 3),
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("-", 1, 3),
    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("+", 2, 3),
    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("=", 3, 3),
    ("0", 4, 0),
    (".", 4, 2),
]


def create_buttons(frame, button_list, is_sci=False):
    for text, row, col in button_list:
        if text == "=":
            bg_color, fg_color, active_bg = "#0078d4", "#ffffff", "#005a9e"
        elif is_sci:
            bg_color, fg_color, active_bg = "#f9f9f9", "#000000", "#e5e5e5"
        elif text in ["÷", "×", "-", "+", "C", "⌫"]:
            bg_color, fg_color, active_bg = "#e6e6e6", "#000000", "#cccccc"
        else:
            bg_color, fg_color, active_bg = "#ffffff", "#000000", "#f9f9f9"

        grid_kwargs = {
            "row": row,
            "column": col,
            "sticky": "nsew",
            "padx": 2,
            "pady": 2,
        }
        if text == "=":
            grid_kwargs["rowspan"] = 2
        elif text == "0":
            grid_kwargs["columnspan"] = 2

        btn = tk.Button(
            frame,
            text=text,
            font=btn_font,
            bg=bg_color,
            fg=fg_color,
            activebackground=active_bg,
            activeforeground=fg_color,
            relief="flat",
            command=lambda t=text: press(t),
        )
        btn.grid(**grid_kwargs)


create_buttons(sci_frame, sci_buttons, is_sci=True)
create_buttons(std_frame, std_buttons, is_sci=False)

root.mainloop()