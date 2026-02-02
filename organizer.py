import os
import shutil
from config import File_Categories

class FileOrganizer:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def organize(self):

        if not os.path.exists(self.folder_path):
            print("Error: The provided path does not exist.")
            return

        if not os.path.isdir(self.folder_path):
                print("Error: The provided path is not a folder.")
                return

        file_count = 0

        for item in os.listdir(self.folder_path):
            full_path = os.path.join(self.folder_path, item)

            if os.path.isfile(full_path):
                self._move_file(item)
                file_count += 1

        if file_count == 0:
            print(" No files found to organize.")
        else:
            print(f"File organization completed {file_count} files processed.")        


    def _move_file(self, filename):
        extension = os.path.splitext(filename)[1].lower()
    
        for folder, extensions in File_Categories.items():
            if extension in extensions:
                self._move_to_folder(filename, folder)
                return

        self._move_to_folder(filename, "Others")


    def _move_to_folder(self, filename, folder_name):
        target_folder = os.path.join(self.folder_path, folder_name)

        if not os.path.exists(target_folder):
            os.makedirs(target_folder)

        shutil.move(
            os.path.join(self.folder_path, filename),
            os.path.join(target_folder, filename)
        )            
