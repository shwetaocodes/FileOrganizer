# 📂 File Organizer (Python)

A simple and efficient Python script that automatically organizes files
inside a folder based on their extensions.\
Perfect for cleaning messy Downloads / Desktop / Project directories.

------------------------------------------------------------------------

## 🚀 Features

-   Automatically sorts files into category folders\
-   Creates folders if they don't exist\
-   Handles unknown file types safely\
-   Easy to run -- no external dependencies\
-   Works on Windows / Mac / Linux

------------------------------------------------------------------------

## 🧩 Supported Categories (Example)

  File Type   Extensions
  ----------- --------------------------
  Images      .jpg, .png, .jpeg, .gif
  Documents   .pdf, .docx, .txt, .xlsx
  Music       .mp3, .wav
  Videos      .mp4, .mkv
  Archives    .zip, .rar
  Code        .py, .js, .html

Unknown extensions will be moved to "Others" folder.

------------------------------------------------------------------------

## 📁 Project Structure

    FileOrganizer/
    │
    ├── main.py
    ├── organizer.py
    ├── config.py
    └── README.md

------------------------------------------------------------------------

## ▶ How to Run

### 1. Clone the repository

    git clone https://github.com/shwetaocodes/FileOrganizer.git

### 2. Go to project folder

    cd FileOrganizer

### 3. Run the script

    python main.py

------------------------------------------------------------------------

## 🧪 Example

### Before

    Downloads/
    ├── photo.jpg
    ├── song.mp3
    ├── report.pdf
    ├── video.mp4

### After

    Downloads/
    ├── Images/
    │   └── photo.jpg
    ├── Music/
    │   └── song.mp3
    ├── Documents/
    │   └── report.pdf
    └── Videos/
        └── video.mp4

------------------------------------------------------------------------

## ⚙ Customization

Edit config.py to add your own extensions.

------------------------------------------------------------------------

## 📄 License

Open Source
