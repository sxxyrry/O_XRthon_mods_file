import os
from O_XRthon_mods_file._XRthon_.XRthon_main import XRthon_main
from tkinter import Tk, Text, Scrollbar, END, messagebox
import tkinter as tk

class XRthonEditor(Tk):
    def __init__(self):
        super().__init__()
        self.title("XRthon Editor")
        self.geometry('800x600')

        # 创建文本区域与滚动条
        self.text_area = Text(self)
        self.scroll_bar = Scrollbar(self, command=self.text_area.yview)
        self.text_area.configure(yscrollcommand=self.scroll_bar.set)

        self.scroll_bar.pack(side='right', fill='y')
        self.text_area.pack(fill='both', expand=True)

        # 保存按钮事件绑定
        self.save_button = tk.Button(self, text="Save & Run", command=self.save_and_run)
        self.save_button.pack(side='bottom')

        # 初始化XRthon解析器实例
        self.xrthon = XRthon_main()

    def save_and_run(self):
        xrthon_code = self.text_area.get('1.0', END)
        
        try:
            if os.path.exists('./temp.XRn'):
                with open('./temp.XRn', 'w') as file:
                    file.write(xrthon_code)
            else:
                with open('./temp.XRn', 'x') as file:
                    file.write(xrthon_code)

            self.xrthon.XRthon_file(open('./temp.XRn'))
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    app = XRthonEditor()
    app.mainloop()