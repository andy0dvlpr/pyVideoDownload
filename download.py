import tkinter as tk
import os
from typing import Collection

def download():
    link = linkinput.get()
    selection = radio_var.get()
    if selection == 1:
        os.system("youtube-dl.exe -x --audio-format mp3 --audio-quality 192k" + " " + "\"" + link + "\"")
    if selection == 2:
        os.system("youtube-dl.exe -f mp4" + " " + "\"" + link + "\"")
    if selection == 3:
        os.system("youtube-dl.exe --yes-playlist -x --audio-format mp3 --audio-quality 192k" + " " + "\"" + link + "\"")
    if selection == 4:
        os.system("youtube-dl.exe --yes-playlist -f mp4" + " " + "\"" + link + "\"")

window = tk.Tk()
bitrate = tk.Frame(window)
bitrateinput = tk.Entry(bitrate, width=10)
label2 = tk.Label(bitrate, text="Bitrate:")
radio_var = tk.IntVar()
R1 = tk.Radiobutton(window, text="Download song", variable=radio_var, value=1)
R1.select() # A graphical glitch occurs when we don't provide a value to be selected.
R2 = tk.Radiobutton(window, text="Download video", variable=radio_var, value=2)
R3 = tk.Radiobutton(window, text="Download songs from a playlist", variable=radio_var, value=3)
R4 = tk.Radiobutton(window, text="Download videos from a playlist", variable=radio_var, value=4)
label = tk.Label(text="Link:")
linkinput = tk.Entry(width=100)
button = tk.Button(text="Download",  command=download)

bitrate.grid(column=1, row=1)
label2.grid(column=1, row=1)#column=1, row=1, sticky="W")
bitrateinput.grid(column=2, row=1)#column=2, row=1, sticky="W")
R1.grid(column=1, row=2)
R2.grid(column=1, row=3)
R3.grid(column=1, row=4)
R4.grid(column=1, row=5)
label.grid(column=1, row=6)
linkinput.grid(column=1, row=7)
button.grid(column=1, row=8)

window.mainloop()