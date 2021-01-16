from win32api import GetSystemDirectory, GetUserName
import os

drive = GetSystemDirectory().split(':')[0]
user = GetUserName()
download_folders = [f'{drive}:\\Users\\{user}\\Downloads',
                    f'{drive}:\\Пользователи\\{user}\\Загрузки']


class Main:
    def __init__(self, folders: list):
        self.folders = folders
        self.folder_path = None

    def check_path(self):
        for folder in self.folders:
            if os.path.isdir(folder):
                self.folder_path = folder
                break


if __name__ == '__main__':
    inst = Main(download_folders)
    inst.check_path()
