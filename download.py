import tkinter as tk
import os

def download():
    link = linkinput.get()
    os.system("youtube-dl.exe -x --audio-format mp3 --audio-quality 192k " + link)

selection = 1

window = tk.Tk()

R1 = tk.Radiobutton(text="Download song", variable=selection, value=1)
R1.select() # A graphical glitch occurs when we don't provide a value to be selected.
R2 = tk.Radiobutton(text="Download video", variable=selection, value=2)
R3 = tk.Radiobutton(text="Download songs from a playlist", variable=selection, value=3)
R4 = tk.Radiobutton(text="Download videos from a playlist", variable=selection, value=4)
label = tk.Label(text="Link:")
linkinput = tk.Entry(width=100)
button = tk.Button(text="Download",  command=download)

R1.pack()
R2.pack()
R3.pack()
R4.pack()
label.pack()
linkinput.pack()
button.pack()

window.mainloop()