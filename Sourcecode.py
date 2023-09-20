import tkinter as tk
from tkinter import Entry, Button
import os
import shutil

# Hàm để tạo thư mục mới
def create_directory():
    new_folder_name = folder_name_entry.get()
    if new_folder_name:
        try:
            os.mkdir(new_folder_name)
            result_label.config(text=f"Đã tạo thư mục '{new_folder_name}' thành công.")
        except FileExistsError:
            result_label.config(text=f"Thư mục '{new_folder_name}' đã tồn tại.")
    else:
        result_label.config(text="Vui lòng nhập tên thư mục.")

# Hàm để xoá thư mục
def delete_directory():
    folder_to_delete = folder_name_entry.get()
    if folder_to_delete:
        try:
            shutil.rmtree(folder_to_delete)
            result_label.config(text=f"Đã xoá thư mục '{folder_to_delete}' thành công.")
        except FileNotFoundError:
            result_label.config(text=f"Thư mục '{folder_to_delete}' không tồn tại.")
    else:
        result_label.config(text="Vui lòng nhập tên thư mục.")

# Tạo cửa sổ giao diện
root = tk.Tk()
root.title("Quản Lý Thư Mục")
root.geometry("200x200")  # Đặt kích thước cửa sổ là 200x200 px

# Nhập tên thư mục
folder_name_label = tk.Label(root, text="Tên Thư Mục:")
folder_name_label.pack()

folder_name_entry = Entry(root)
folder_name_entry.pack()

# Tạo nút bấm "Tạo Thư Mục" và "Xoá Thư Mục" với góc bo tròn
create_button = Button(root, text="Tạo Thư Mục", command=create_directory, relief=tk.RAISED, borderwidth=3)
delete_button = Button(root, text="Xoá Thư Mục", command=delete_directory, relief=tk.RAISED, borderwidth=3)

create_button.pack(pady=10)
delete_button.pack()

# Hiển thị kết quả
result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack()

# Khởi động ứng dụng
root.mainloop()
