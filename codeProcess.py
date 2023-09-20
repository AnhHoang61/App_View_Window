import tkinter as tk
from tkinter import Listbox, Scrollbar, END
import pygetwindow as gw

# Hàm để cập nhật danh sách cửa sổ
def update_window_list():
    window_list.delete(0, END)
    window_titles = gw.getAllTitles()
    for window_title in window_titles:
        window_list.insert(END, window_title)

# Tạo cửa sổ giao diện
root = tk.Tk()
root.title("Danh Sách Cửa Sổ Đang Chạy")

# Danh sách cửa sổ
window_label = tk.Label(root, text="Danh Sách Cửa Sổ Đang Chạy")
window_label.pack()

window_list = Listbox(root, width=90, height=50)
window_list.pack()

window_scrollbar = Scrollbar(root, command=window_list.yview)
window_list.config(yscrollcommand=window_scrollbar.set)
window_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Nút cập nhật danh sách
update_button = tk.Button(root, text="Cập Nhật Danh Sách", command=update_window_list)
update_button.pack()

# Cập nhật danh sách khi khởi động
update_window_list()

# Khởi động ứng dụng
root.mainloop()
