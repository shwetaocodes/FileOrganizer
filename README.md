# File Organizer (Python)

A Python-based file organizer that automatically sorts files in a folder into categorized directories based on file extensions.  
This project demonstrates **OOP design, modular code, and real-world file handling** — perfect for interviews or portfolio demonstration.

---

## Problem Statement

Folders like **Downloads** or **Desktop** often contain a mix of file types, making it difficult to locate files.  
Manually organizing files is time-consuming and error-prone.  

This script automatically organizes files into folders such as **Images**, **Music**, **Videos**, **Documents**, and **Others**.

---

## Features

- Organizes files based on extensions
- Automatically creates category folders if they don’t exist
- Handles unknown file types gracefully
- Displays completion messages after organizing
- Notifies the user if there are no files to organize
- Validates folder paths and displays clear error messages

---

## Skills Demonstrated

- Python fundamentals and execution model
- Object-Oriented Programming (OOP)
- Modular code structure (separate `config.py`, `organizer.py`, `main.py`)
- File system handling (`os`, `shutil`)
- Dictionary-based logic for clean and scalable code
- Input validation and error handling
- Time & space complexity awareness

---

## Project Structure

FileOrganizer/
├── main.py # Program entry point
├── organizer.py # FileOrganizer class and organizing logic
├── config.py # File extension → category mapping
├── README.md


---

## How to Run

1. Clone the repository
2. Navigate to the project folder
3. Run the program
4. Enter the folder path when prompted


## Example

# Before Running the Script

TestFolder/
├── photo.jpg
├── song.mp3
├── movie.mp4
├── notes.txt
├── resume.pdf
├── random.xyz


# After Running the Script

TestFolder/
├── Images/
│   └── photo.jpg
├── Music/
│   └── song.mp3
├── Videos/
│   └── movie.mp4
├── Documents/
│   ├── notes.txt
│   └── resume.pdf
├── Others/
│   └── random.xyz
