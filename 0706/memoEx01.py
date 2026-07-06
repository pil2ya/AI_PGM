import sys
import os
from PyQt6.QtWidgets import (QApplication, QMainWindow, QTextEdit, 
                             QFileDialog, QMessageBox)
from PyQt6.QtGui import QFont, QAction
from PyQt6.QtCore import Qt

class Notepad(QMainWindow):
    def __init__(self):
        super().__init__()
        self.current_file = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle("제목 없음 - 파이썬 메모장")
        self.setGeometry(100, 100, 800, 600)

        # ===== 텍스트 창 생성 (한글 버그 절대 없음) =====
        self.text_edit = QTextEdit()
        # 윈도우 메모장 기본 폰트와 동일하게 설정
        self.current_font = QFont("맑은 고딕", 12)
        self.text_edit.setFont(self.current_font)
        self.setCentralWidget(self.text_edit)

        # ===== 상단 메뉴바 구성 =====
        menu_bar = self.menuBar()

        # 1. 파일 메뉴
        file_menu = menu_bar.addMenu("파일(&F)")
        
        new_action = QAction("새로 만들기(&N)", self)
        new_action.triggered.connect(self.new_file)
        file_menu.addAction(new_action)

        open_action = QAction("열기(&O)...", self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        save_action = QAction("저장(&S)", self)
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)

        save_as_action = QAction("다른 이름으로 저장(&A)...", self)
        save_as_action.triggered.connect(self.save_as_file)
        file_menu.addAction(save_as_action)

        file_menu.addSeparator()
        
        exit_action = QAction("종료(&X)", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # 2. 서식(글꼴) 메뉴
        font_menu = menu_bar.addMenu("서식(&O)")
        
        # 글꼴 크기 변경 서브 메뉴
        size_menu = font_menu.addMenu("크기(&S)")
        sizes = [10, 12, 14, 16, 20, 24]
        for size in sizes:
            size_action = QAction(f"{size}", self)
            # lambda를 활용해 클릭한 크기를 전달
            size_action.triggered.connect(lambda checked, s=size: self.change_size(s))
            size_menu.addAction(size_action)

    # ===== 파일 기능 로직 =====
    def new_file(self):
        self.text_edit.clear()
        self.current_file = None
        self.setWindowTitle("제목 없음 - 파이썬 메모장")

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "파일 열기", "", "텍스트 문서 (*.txt);;모든 파일 (*.*)")
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    self.text_edit.setPlainText(f.read())
                self.current_file = file_path
                self.setWindowTitle(f"{os.path.basename(file_path)} - 파이썬 메모장")
            except Exception as e:
                QMessageBox.critical(self, "오류", f"파일을 열 수 없습니다:\n{e}")

    def save_file(self):
        if self.current_file:
            try:
                with open(self.current_file, "w", encoding="utf-8") as f:
                    f.write(self.text_edit.toPlainText())
            except Exception as e:
                QMessageBox.critical(self, "오류", f"파일을 저장할 수 없습니다:\n{e}")
        else:
            self.save_as_file()

    def save_as_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "다른 이름으로 저장", "", "텍스트 문서 (*.txt);;모든 파일 (*.*)")
        if file_path:
            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(self.text_edit.toPlainText())
                self.current_file = file_path
                self.setWindowTitle(f"{os.path.basename(file_path)} - 파이썬 메모장")
            except Exception as e:
                QMessageBox.critical(self, "오류", f"파일을 저장할 수 없습니다:\n{e}")

    # ===== 글자 크기 변경 로직 =====
    def change_size(self, size):
        self.current_font.setPointSize(size)
        self.text_edit.setFont(self.current_font)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    notepad = Notepad()
    notepad.show()
    sys.exit(app.exec())