from organizer import FileOrganizer

if __name__ == "__main__":

    folder_path = input("Enter the folder's path to organizer: ")
    organizer = FileOrganizer(folder_path)
    organizer.organize()