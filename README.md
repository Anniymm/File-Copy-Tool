# File Copy Utility

A simple Python GUI application for copying files to the current directory. This tool uses `tkinter` to create a user-friendly interface that allows you to select files from your computer and copy them to the directory where the script is running. It also includes a progress bar to display the status of the copying process and logs all activities for troubleshooting purposes.

## Features

- Select multiple files to copy using a graphical file dialog.
- Display a progress bar for file copying status.
- Log file operations, including successful copies and errors.
- Provide error messages for failed copy attempts.
  
## Requirements

- Python 3.10
- `tkinter` (usually included with Python)
- `shutil` (Python standard library)
- `pathlib` (Python standard library)

## Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/Anniymm/File-Copy-Tool.git
    cd File-Copy-Tool
    ```

2. **Run the Script:**

    Make sure you have Python 3.x installed on your system. Run the following command:

    ```bash
    python copy_tool_oop.py
    ```
## Here is a screenshot of the application:
![copy 1](https://github.com/user-attachments/assets/907f7e2c-1dfd-49e7-9fd8-016ab919c8eb)
![copy 2](https://github.com/user-attachments/assets/7a6ce323-dc49-40a3-9b49-0a98f090126f)
![copy 3](https://github.com/user-attachments/assets/494e4436-922b-48af-9871-f859ee6fa029)

## Usage

1. Run the script using Python.
2. Click the **Select Files** button to open a file dialog.
3. Choose the files you want to copy. You can select multiple files.
4. The progress bar will show the status of the file copying process.
5. The status label will indicate the number of files copied and any errors that occur.

## Error Handling

The application handles the following errors:
- **`shutil.SameFileError`:** If the source and destination files are the same.
- **`FileNotFoundError`:** If the source file is not found.
- **`PermissionError`:** If there is no permission to copy the file.

All errors are logged to `file_copy.log` for debugging purposes.

## Logging

All file operations are logged in `file_copy.log`. This file records:

- The date and time of each operation.
- The severity level (INFO or ERROR).
- Descriptions of the operations or errors.

## Contributing

Contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.


