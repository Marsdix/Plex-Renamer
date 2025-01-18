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
1. Download the latest `.exe` file from the [Releases](https://github.com/your-username/plex-renamer/releases) section.
2. Double-click the `.exe` file to launch Plex Renamer.
3. Follow the on-screen instructions to organize your media.

> **Note**: The `.exe` file is standalone and does not require Python to be installed on your system.

---

### Option 2: Using the Python Script (Manual Installation)

1. Make sure you have Python installed on your system:
   - Download and install Python from [python.org](https://www.python.org/).
   - During installation, **make sure to check the option "Add Python to PATH"** to ensure Python works correctly from the command line.

2. Clone the Plex Renamer repository:
   ```bash
   git clone https://github.com/your-username/plex-renamer.git

	3.	Navigate to the project directory:

cd plex-renamer


	4.	(Optional) Install any required dependencies if your project uses them:

pip install -r requirements.txt


	5.	Run the Python script:

python plex-renamer.py



	Note: Replace plex-renamer.py with the actual name of your main Python script, if different.

📖 Usage

For the .exe Version:
	1.	Double-click the .exe file to open Plex Renamer.
	2.	Select the folder containing your media files.
	3.	Follow the instructions to rename and organize your files automatically.

For the Python Version:
	1.	Run the script from the command line:

python plex-renamer.py


	2.	Follow the prompts to:
	•	Select the folder with your media files.
	•	Choose the renaming pattern or use the default one.
	3.	Check the output folder to see your organized media library.

🛠️ Technologies Used
	•	Languages:
	•	Python (for core logic)
	•	JavaScript (if applicable for any GUI or web functionality).
	•	Tools:
	•	PyInstaller: Used to compile the Python script into a .exe file for easier distribution.
	•	Libraries: Examples include os, shutil, or other Python modules for file handling.

🤝 Contributing

Contributions are welcome! If you have ideas to improve Plex Renamer or want to report a bug, follow these steps:
	1.	Fork this repository.
	2.	Create a new branch for your feature or fix:

git checkout -b feature-name


	3.	Commit your changes:

git commit -m "Add new feature or fix bug"


	4.	Push to your branch:

git push origin feature-name


	5.	Open a Pull Request and describe your changes.

📄 License

This project is licensed under the MIT License. Feel free to use, modify, and distribute this project as needed.

🌟 Acknowledgments
	•	Thanks to the Plex community for inspiring this project.
	•	Special thanks to everyone providing feedback and support to improve Plex Renamer.

⭐ Show Your Support

If you find Plex Renamer helpful, please consider giving the repository a ⭐ to show your support!

---