import pathlib
from tkinter import filedialog, Tk
import shutil

class Main:
    def __init__(self, selected_file_location, current_folder_path):
        self.selected_file_location  = selected_file_location
        self.current_folder_path  = current_folder_path

    def __str__(self):
        return f'{self.selected_file_location} successfully added to {self.current_folder_path}'
        
class ChooseFile(Main):
    def __init__(self, selected_file_location, current_folder_path):
        super().__init__(selected_file_location, current_folder_path)    
    
    def choose_file(self):
        root = Tk()
        root.withdraw()
        filetypes=[('All files', '*.*')]
        path = filedialog.askopenfilename(title='Choose file',filetypes = filetypes, multiple = True)
        root.destroy() #file-is 
        self.selected_file_location = path[0]
        return self.selected_file_location

    def open_file(self):
        self.current_folder_path = pathlib.Path().resolve() # get location of current path
        return self.current_folder_path
    
    def get_copy(self):
        if self.selected_file_location and self.current_folder_path:
            dest = shutil.copy(self.selected_file_location, self.current_folder_path) # copy file to current directory
            return dest
        else:
            return None
        
if __name__ == "__main__":
    chooser = ChooseFile('', '')
    selected_file = chooser.choose_file()
    if selected_file:
        current_folder = chooser.open_file()
        copied_file = chooser.get_copy()
        print(chooser)  
        if copied_file:
            pass
        else:
            print("Failed to copy the file.")