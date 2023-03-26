import os
import shutil

ext_to_dir = {
    ".pdf": "C:\\Users\\user\\Downloads\\PDFs",
    ".jpeg": "C:\\Users\\user\\Downloads\\Images",
    ".png": "C:\\Users\\user\\Downloads\\Images",
    ".zip": "C:\\Users\\user\\Downloads\\Archives",
    ".exe": "C:\\Users\\user\\Downloads\\Executables",
    ".txt": "C:\\Users\\user\\Downloads\\Texts",
    ".mp4": "C:\\Users\\user\\Downloads\\Videos",
    ".mp3": "C:\\Users\\user\\Downloads\\Music",
    ".wav": "C:\\Users\\user\\Downloads\\Music"
}
def move_files_to_dirs(downloads_folder):
    for filename in os.listdir(downloads_folder):
        filepath = os.path.join(downloads_folder, filename)
        if os.path.isfile(filepath):
            ext = os.path.splitext(filename)[1]
            if ext in ext_to_dir:
                dest_dir = ext_to_dir[ext]
                shutil.move(filepath, dest_dir)
downloads_folder = "C:\\Users\\user\\Downloads"
move_files_to_dirs(downloads_folder)
