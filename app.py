import tkinter as tk

import subprocess
import sys


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.text = tk.Button(self)
        self.text['text'] = "Запустить мониторинг дубликатов"
        self.text.pack(side="top")
        self.text['command'] = self.runloop

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.kill_programm)
        self.quit.pack(side="bottom")

    def runloop(self):
        self.sub = subprocess.Popen([sys.executable, 'main.py'], shell=False, stdin=None, stdout=None, stderr=None,
                                    close_fds=True)
        self.text['text'] = 'Мониторинг запущен'
        self.text.pack(side='top')

    def kill_programm(self):
        self.sub.kill()
        self.master.destroy()


root = tk.Tk()
app = Application(master=root)
app.mainloop()
