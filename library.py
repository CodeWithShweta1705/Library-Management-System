import tkinter as tk
from tkinter import messagebox, ttk
import csv
import os

# फाइल को डेस्कटॉप पर सेव करने के लिए पाथ
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
FILE_NAME = os.path.join(desktop, "SkillBuilder_Library_Data.csv")

def initialize_storage():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["Book Name", "Author", "Status"])

class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SkillBuilder Library System")
        self.root.geometry("600x500")
        self.root.configure(bg="#f4f7f6")

        tk.Label(root, text="SKILLBUILDER LIBRARY SYSTEM", font=("Arial", 14, "bold"), 
                 bg="#2c3e50", fg="white", pady=10).pack(fill="x")

        # Input Frame
        frame = tk.Frame(root, bg="#f4f7f6", pady=20)
        frame.pack()

        tk.Label(frame, text="Book Name:", bg="#f4f7f6").grid(row=0, column=0, pady=5)
        self.book_entry = tk.Entry(frame, width=30)
        self.book_entry.grid(row=0, column=1, pady=5)

        tk.Label(frame, text="Author:", bg="#f4f7f6").grid(row=1, column=0, pady=5)
        self.author_entry = tk.Entry(frame, width=30)
        self.author_entry.grid(row=1, column=1, pady=5)

        # Buttons
        tk.Button(root, text="SAVE TO DESKTOP", command=self.add_book, bg="#27ae60", fg="white", width=20).pack(pady=10)

        # Table
        self.tree = ttk.Treeview(root, columns=("Book", "Author"), show='headings')
        self.tree.heading("Book", text="Book Title")
        self.tree.heading("Author", text="Author Name")
        self.tree.pack(pady=10, padx=20, fill="both")

        self.view_books()

    def add_book(self):
        name = self.book_entry.get()
        author = self.author_entry.get()
        if name and author:
            initialize_storage()
            with open(FILE_NAME, mode='a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([name, author, "Available"])
            messagebox.showinfo("Success", f"File saved on your Desktop as:\n{FILE_NAME}")
            self.view_books()
        else:
            messagebox.showwarning("Error", "Fill all fields")

    def view_books(self):
        for i in self.tree.get_children(): self.tree.delete(i)
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, mode='r', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader: self.tree.insert("", tk.END, values=(row[0], row[1]))

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()