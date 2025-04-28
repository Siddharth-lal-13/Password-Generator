# Password Manager

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)
![Version](https://img.shields.io/badge/version-1.0.0-brightgreen.svg)

A secure, local password manager application that generates strong passwords, stores them safely on your device, and provides quick access when needed.

![Password Manager Logo](logo.png)

## Features

- **Strong Password Generation**: Create complex passwords with customizable length (4-20 characters)
- **Local Storage**: All passwords are saved securely in a local JSON file
- **Automatic Clipboard Copy**: Generated passwords are automatically copied to clipboard
- **Search Functionality**: Quickly find stored credentials for any website
- **Username Memory**: Save your most used email/username for quick access
- **User-Friendly Interface**: Clean and intuitive GUI built with Tkinter

## Table of Contents

- [Installation](#installation)
  - [Windows](#windows)
  - [macOS](#macos)
  - [Linux](#linux)
- [Usage](#usage)
- [Tech Stack](#tech-stack)
- [Development](#development)
- [License](#license)
- [Author](#author)

## Installation

### Windows

#### Option 1: Executable (.exe)
1. Download the latest release from the releases page
2. Extract the ZIP file to your desired location
3. Run `PasswordManager.exe`

#### Option 2: From Source
1. Ensure Python 3.x is installed on your system
2. Clone this repository or download the source code
3. Open Command Prompt and navigate to the project directory
4. Install required packages:
   ```
   pip install pyperclip
   ```
5. Run the application:
   ```
   python main.py
   ```

### macOS

1. Ensure Python 3.x is installed on your system
2. Clone this repository or download the source code
3. Open Terminal and navigate to the project directory
4. Install required packages:
   ```
   pip3 install pyperclip
   ```
5. Run the application:
   ```
   python3 main.py
   ```

### Linux

1. Ensure Python 3.x and Tkinter are installed on your system:
   ```
   sudo apt-get install python3 python3-tk xclip
   ```
2. Clone this repository or download the source code
3. Open Terminal and navigate to the project directory
4. Install required packages:
   ```
   pip3 install pyperclip
   ```
5. Run the application:
   ```
   python3 main.py
   ```

## Usage

1. **Adding a New Password**:
   - Enter the website name
   - Enter your email/username or use the "Save/Retrieve" button to use a saved one
   - Either enter a password manually or click "Generate Password"
   - Adjust the slider to set your desired password length
   - Click "Add" to save the credentials

2. **Finding a Password**:
   - Enter the website name
   - Click "Search"
   - If found, the password will be displayed and automatically copied to your clipboard

3. **Saving a Username**:
   - Enter your preferred email/username 
   - Click "Save/Retrieve" to store for future use
   - Next time, just click "Save/Retrieve" with an empty field to retrieve your saved username

## Tech Stack

- **Python**: Core programming language
- **Tkinter**: GUI framework
- **JSON**: Data storage format
- **Standard Library Modules**:
  - `random`: For password generation
  - `pyperclip`: For clipboard functionality
  - `json`: For data storage and retrieval
  - `os`: For file operations

## Development

### Project Structure

```
password-manager/
├── main.py          # Main application code
├── logo.png         # Application logo
├── data.json        # Password storage file (created on first use)
└── username.txt     # Saved username file (created on first use)
```

### Building from Source

To create your own executable:

1. Install PyInstaller:
   ```
   pip install pyinstaller
   ```

2. Create the executable:
   ```
   pyinstaller --onefile --windowed --add-data "logo.png;." main.py
   ```

3. Find the executable in the `dist` folder

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Siddharth Lal

---

**Note**: This password manager stores data locally without encryption. For highly sensitive information, consider using a solution with additional security features.
