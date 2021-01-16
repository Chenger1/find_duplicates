from win32api import GetSystemDirectory, GetUserName
import os
import re
import time
from win10toast import ToastNotifier

drive = GetSystemDirectory().split(':')[0]
user = GetUserName()
download_folders = [f'{drive}:\\Users\\{user}\\Downloads',
                    f'{drive}:\\Пользователи\\{user}\\Загрузки']


class Main:
    def __init__(self, folders: list):
        self.folders = folders
        self.folder_path = None
        self.files = self.check_files()
        self.toaster = ToastNotifier()

    def check_path(self):
        for folder in self.folders:
            if os.path.isdir(folder):
                self.folder_path = folder
                break

    def check_files(self) -> list:
        return os.listdir(self.folder_path)

    def check_duplicate(self):
        for file in self.files:
            file, is_replaced = self.filename_proceed(file)
            if is_replaced:
                if self.files.count(file) >= 1:
                    self.show_message(file)
            else:
                if self.files.count(file) >= 2:
                    self.show_message(file)

    @staticmethod
    def filename_proceed(filename: str) -> str:
        patterns = list(filter(lambda elem: '' != elem,
                        [' - Copy', ' - Копия']))
        re_found = ''.join(re.findall('\\(\\d\\).', filename))
        is_replaced = False
        for pattern in patterns:
            if pattern in filename:
                is_replaced = True
            filename = filename.replace(pattern, '')
        else:
            if re_found:
                filename = filename.replace(' {}'.format(re_found[:-1]), '')
                is_replaced = True

        return filename, is_replaced

    def show_message(self, filename: str):
        self.toaster.show_toast('Такой файл уже есть в папке', f'{filename}')

    def check_for_changes_in_dict(self) -> bool:
        trg = False
        new_state = self.check_files()
        if self.files == new_state:
            trg = True
        self.files = new_state
        return trg


if __name__ == '__main__':
    inst = Main(download_folders)
    inst.check_path()
    inst.check_files()

    while True:
        try:
            if inst.check_for_changes_in_dict():
                inst.check_duplicate()
            time.sleep(5)
        except KeyboardInterrupt:
            break
