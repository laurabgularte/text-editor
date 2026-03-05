import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import font as tkFont

class TextEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Editor")
        self.root.geometry("800x600")
        self.filename = None

        menubar = tk.Menu(root)
        root.config(menu=menubar)
        
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)
        
        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Undo", command=lambda: self.text_area.edit_undo())
        edit_menu.add_command(label="Redo", command=lambda: self.text_area.edit_redo())
        
        frame = tk.Frame(root)
        frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.text_area = tk.Text(frame, yscrollcommand=scrollbar.set, wrap=tk.WORD)
        self.text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.text_area.yview)
    
        self.text_area.config(undo=True, maxundo=-1)
    
        self.status = tk.Label(root, text="Untitled", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status.pack(side=tk.BOTTOM, fill=tk.X)
    
    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.filename = None
        self.root.title("Text Editor - Untitled")
        self.status.config(text="Untitled")
    
    def open_file(self):
        filepath = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if filepath:
            with open(filepath, 'r') as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(1.0, file.read())
            self.filename = filepath
            self.root.title(f"Text Editor - {filepath}")
            self.status.config(text=filepath)
    
    def save_file(self):
        if self.filename:
            with open(self.filename, 'w') as file:
                file.write(self.text_area.get(1.0, tk.END))
            messagebox.showinfo("Success", "File saved successfully!")
        else:
            self.save_as_file()
    
    def save_as_file(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if filepath:
            with open(filepath, 'w') as file:
                file.write(self.text_area.get(1.0, tk.END))
            self.filename = filepath
            self.root.title(f"Text Editor - {filepath}")
            self.status.config(text=filepath)
            messagebox.showinfo("Success", "File saved successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditorApp(root)
    root.mainloop()