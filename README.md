# 📁 Plex Renamer

**Plex Renamer** is a tool designed to help you organize your media library in a way that's fully compatible with **Plex**. Whether it's renaming your series, creating folders for movies, series, or documents, or adding "extras" folders, Plex Renamer makes it easy to maintain a clean and structured media library.

---

## 🚀 Features

- 🔄 **Automatic renaming**: Rename your series and media files based on your preferences.
- 🗂️ **Folder creation**: Automatically create folders for:
  - 📺 Series
  - 🎥 Movies
  - 📄 Documents
- ➕ **Extras support**: Add "Extras" folders to existing series or movies for additional content.
- 🎯 **Plex compatibility**: Ensure your media files and folders are organized in a way that Plex understands perfectly.
- 🖥️ **Two versions available**:
  - A precompiled `.exe` file for easy use.
  - A Python script for manual installation and customization.

---

## 📥 Installation

You can use **Plex Renamer** in two ways: by downloading the `.exe` file (recommended for simplicity) or by running the Python script manually.

### Option 1: Using the `.exe` File (Recommended)
1. Download the latest `.exe` file from the [Releases](https://github.com/Marsdix/Plex-Renamer/releases/tag/v1.0.0).
2. Double-click the `.exe` file to launch Plex Renamer.
3. Follow the on-screen instructions to organize your media.
4. The first time you run the `.exe`, it will create a desktop shortcut named **Plex Renamer**, which you can use to open the program directly in the future.

> **Note**: The `.exe` file is standalone and does not require Python to be installed on your system.

---

### Option 2: Using the Python Script (Manual Installation)

1. **Install Python**:
   - Download the latest version of Python from [python.org](https://www.python.org/).
   - During installation:
     - **Check the box** for "Add Python to PATH".
     - Choose the option to install Python for all users (recommended).
   - Verify the installation by running this command in your terminal or command prompt:
     ```bash
     python --version
     ```

2. **Download the files**:
   - Go to the [repository](https://github.com/Marsdix/Plex-Renamer).
   - Click the green **"Code"** button and select **"Download ZIP"**.
   - Extract the ZIP file to a folder on your computer.

3. **Run the setup script**:
   - Navigate to the folder where you extracted the files.
   - Double-click on `setup.py`.
   - This will create a desktop shortcut named **Plex Renamer**.

4. **Run the main Python script**:
   - After running `setup.py`, you can use the **Plex Renamer** shortcut on your desktop to start the program directly.
   - **Important**: Place the downloaded folder in a permanent location. The desktop shortcut will point to the current folder location. If you move the folder later, the shortcut will stop working, and you’ll need to run `setup.py` again to generate a new shortcut.

---

## 📖 Usage

### For the `.exe` Version:
1. Double-click the `.exe` file to open Plex Renamer.
2. Select the folder containing your media files.
3. Follow the instructions to rename and organize your files automatically.

### For the Python Version:
1. Ensure you’ve completed the steps in the **Installation** section.
2. Use the desktop shortcut created by `setup.py` to launch Plex Renamer.
3. Follow the prompts to:
   - Select the folder with your media files.
   - Choose the renaming pattern or use the default one.
4. Check the output folder to see your organized media library.

---

## 🛠️ Technologies Used

- **Languages**:
  - Python (for core logic)
  - JavaScript (if applicable for any GUI or web functionality).
- **Tools**:
  - PyInstaller: Used to compile the Python script into a `.exe` file for easier distribution.
  - Libraries: Examples include `os`, `shutil`, or other Python modules for file handling.

---

## 🤝 Contributing

Contributions are welcome! If you have ideas to improve Plex Renamer or want to report a bug, follow these steps:

1. Fork this repository.
2. Create a new branch for your feature or fix:
   ```bash
   git checkout -b feature-name
Commit your changes:
bash
Copiar
Editar
git commit -m "Add new feature or fix bug"
Push to your branch:
bash
Copiar
Editar
git push origin feature-name
Open a Pull Request and describe your changes.
📄 License
This project is licensed under the MIT License. Feel free to use, modify, and distribute this project as needed.

🌟 Acknowledgments
Thanks to the Plex community for inspiring this project.
Special thanks to everyone providing feedback and support to improve Plex Renamer.
⭐ Show Your Support
If you find Plex Renamer helpful, please consider giving the repository a ⭐ to show your support!
