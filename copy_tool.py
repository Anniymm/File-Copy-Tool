import pathlib
from tkinter import filedialog, Tk
import shutil

def main():
    selected_file_location = choose_file() # return chose file location
    current_folder_path = open_file()
    cpy = get_copy(selected_file_location, current_folder_path)
    if cpy:
        print('Added succesfully.')
    else:
        print('something went wrong!')
def choose_file(): #shercheuli file-is location 
    root = Tk()
    root.withdraw()
    # filetypes=[('DOCX','*.docx'),('PDF','*.pdf'), ('PNG','*.png'), ('ALL', 'all')] # Required file types
    filetypes=[('All files', '*.*')]
    path = filedialog.askopenfilename(title='Choose file',filetypes=filetypes,multiple=True)
    root.destroy()
    return path[0] # return location

def open_file():
    current_folder_path = pathlib.Path().resolve() # location of current directory
    return current_folder_path 

def get_copy(selected_file_location, current_folder_path):
    dest = shutil.copy(selected_file_location, current_folder_path) 
    return dest

if __name__ == "__main__":
    main()


