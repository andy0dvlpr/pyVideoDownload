import tkinter as tk
import os

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
radio_var = tk.IntVar()
R1 = tk.Radiobutton(window, text="Download song", variable=radio_var, value=1)
R1.select() # A graphical glitch occurs when we don't provide a value to be selected.
R2 = tk.Radiobutton(window, text="Download video", variable=radio_var, value=2)
R3 = tk.Radiobutton(window, text="Download songs from a playlist", variable=radio_var, value=3)
R4 = tk.Radiobutton(window, text="Download videos from a playlist", variable=radio_var, value=4)
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