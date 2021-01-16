from win32api import GetSystemDirectory, GetUserName
import os
from win10toast import ToastNotifier

drive = GetSystemDirectory().split(':')[0]
user = GetUserName()
download_folders = [f'{drive}:\\Users\\{user}\\Downloads',
                    f'{drive}:\\Пользователи\\{user}\\Загрузки']


class Main:
    def __init__(self, folders: list):
        self.folders = folders
        self.folder_path = None
        self.files = []
        self.toaster = ToastNotifier()

    def check_path(self):
        for folder in self.folders:
            if os.path.isdir(folder):
                self.folder_path = folder
                break

    def check_files(self):
        self.files = os.listdir(self.folder_path)

    def check_duplicate(self):
        for file in self.files:
            if self.files.count(file) >= 2:
                self.show_message(file)

    def show_message(self, filename: str):
        self.toaster.show_toast('Такой файл уже есть в папке', f'{filename}')


if __name__ == '__main__':
    inst = Main(download_folders)
    inst.check_path()
    inst.check_files()
    inst.check_duplicate()
