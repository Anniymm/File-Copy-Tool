import pathlib
from tkinter import filedialog, Tk, messagebox, Label, Button, ttk
import shutil
import os
import logging

logging.basicConfig(filename='file_copy.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class FileCopyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Copier")
        self.root.geometry("400x200")

        self.label = Label(root, text="Choose files to copy:")
        self.label.pack(pady=10)

        self.select_button = Button(root, text="Select Files", command=self.choose_files)
        self.select_button.pack(pady=5)

        self.progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
        self.progress.pack(pady=10)

        self.status_label = Label(root, text="")
        self.status_label.pack(pady=10)
        self.file_paths = []

    def choose_files(self):
        filetypes = [('All files', '*.*')]
        self.file_paths = filedialog.askopenfilenames(title='Choose files', filetypes=filetypes)
        
        if self.file_paths:
            self.status_label.config(text=f"{len(self.file_paths)} files selected.")
            self.copy_files()
        else:
            self.status_label.config(text="No files selected.")

    def copy_files(self):
        if not self.file_paths:
            messagebox.showerror('Error', 'No files selected to copy.')
            return

        current_folder_path = pathlib.Path().resolve()
        total_files = len(self.file_paths)
        self.progress['maximum'] = total_files

        for index, file_path in enumerate(self.file_paths, start=1):
            try:
                shutil.copy(file_path, current_folder_path)
                logging.info(f'Copied {file_path} to {current_folder_path}')
                self.status_label.config(text=f'Copied {index}/{total_files} files...')
                self.progress['value'] = index
                self.root.update_idletasks()  
            except (shutil.SameFileError, FileNotFoundError, PermissionError) as e:
                logging.error(f'Error copying {file_path}: {e}')
                messagebox.showerror('Error', f'Failed to copy {file_path}: {e}')
                return

        messagebox.showinfo('Success', 'All files added successfully.')

def main():
    root = Tk()
    app = FileCopyApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
