import tkinter as tk
from tkinter import filedialog

import pyttsx3

from main import Speach

from pydub import AudioSegment

class TTS_GUI:

    WIDTH = '1200'
    HEIGHT = '600'

    def __init__(self):

        self.root = tk.Tk()

        self.root.title('TTS')

        self.icon = tk.PhotoImage(file='TTS_icon.png')
        self.root.iconphoto(False, self.icon)

        self.root.minsize(self.WIDTH, self.HEIGHT)
        self.root.maxsize(self.WIDTH, self.HEIGHT)

        self.root.geometry(self.WIDTH + 'x' + self.HEIGHT)

        self.textbox = tk.Text(self.root, font=('Arial', 16))
        self.textbox.place(x=10, y=5)

        self.var = tk.IntVar()  # IntVar obyektini yaratish
        self.male = tk.Radiobutton(self.root, text="Male", font=('Arial', 14), variable=self.var, value=0)
        self.male.place(x=1020, y=150)

        self.female = tk.Radiobutton(self.root, text="Female", font=('Arial', 14), variable=self.var, value=1)
        self.female.place(x=1020, y=180)

        self.click = tk.Button(self.root, text="Speach", font=('Arial', 16), command=self.speach)
        self.click.place(x=1020, y=220)

        self.clrbtn = tk.Button(self.root, text="Clear", font=('Arial', 16), command=self.clr)
        self.clrbtn.place(x=1020, y=280)

        # Menuni yaratish
        self.menubar = tk.Menu(self.root)

        # File menyusi yaratish
        self.file_menu = tk.Menu(self.menubar, tearoff=0)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_audio)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)
        self.menubar.add_cascade(label="File", menu=self.file_menu)


        # Menuni oynaga bog'lash
        self.root.config(menu=self.menubar)

        self.root.mainloop()

    def get_gender(self):
        gender = self.var.get()  # get metodini IntVar obyektidan chaqirish
        return gender

    def get_text(self):
        return self.textbox.get("1.0", tk.END).strip()  # Matnni olish

    def open_file(self):
        filetypes = (
            ('Text Files', '*.txt'),
            ('All', '*.*')
        )
        file_path = filedialog.askopenfilename(filetypes=filetypes)
        if file_path:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()
                self.textbox.insert(tk.END, content)

    def save_audio(self):
        text = self.textbox.get("1.0", tk.END).strip()
        if text:
            first_word = text.split()[0]
            gender = "Male" if self.var.get() == 0 else "Female"
            default_filename = f"{first_word}_{gender}.mp3"

            # Fayl tanlash oynasini ochish
            file_path = filedialog.asksaveasfilename(initialfile=default_filename,
                                                     defaultextension=".mp3",
                                                     filetypes=[("MP3 files", "*.mp3")])
            if file_path:
                self.engine = pyttsx3.init()
                self.voices = self.engine.getProperty('voices')
                self.engine.setProperty('voice', self.voices[self.var.get()].id)
                self.engine.save_to_file(text, file_path)
                self.engine.runAndWait()

    def speach(self):
        text = self.get_text()
        gender = self.get_gender()
        sp = Speach(text, gender)
        sp.speak()  # Matnni ovozga aylantirish


    def clr(self):
        self.textbox.delete('1.0', tk.END)  # Matnni tozalash





