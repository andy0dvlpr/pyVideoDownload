import tkinter as tk
import os

def download():
    link = linkinput.get()
    os.system("youtube-dl.exe -x --audio-format mp3 --audio-quality 192k " + link)

window = tk.Tk()

label = tk.Label(text="Link:")
linkinput = tk.Entry(width=100)
button = tk.Button(text="Download",  command=download)

label.pack()
linkinput.pack()
button.pack()

window.mainloop()