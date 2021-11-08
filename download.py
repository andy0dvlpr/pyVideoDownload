import tkinter as tk
import os
from typing import Collection

def download():
    link = linki.get()
    bitrate = bitratei.get()
    selection = radio_var.get()
    if selection == 1:
        os.system("youtube-dl.exe -x --audio-format mp3 --audio-quality " + bitrate + "k" + " " + "\"" + link + "\"")
    if selection == 2:
        os.system("youtube-dl.exe -f mp4" + " " + "\"" + link + "\"")
    if selection == 3:
        os.system("youtube-dl.exe --yes-playlist -x --audio-format mp3 --audio-quality " + bitrate + "k" + " " + "\"" + link + "\"")
    if selection == 4:
        os.system("youtube-dl.exe --yes-playlist -f mp4" + " " + "\"" + link + "\"")

#### GUI
#region

## ELEMENTS
#region
window = tk.Tk()

# BITRATE
bitratef = tk.Frame(window)
bitratei = tk.Entry(bitratef, width=10)
bitratet = tk.Label(bitratef, text="Bitrate:")
bitratei.insert(0, string="192")

# RADIO
radiof = tk.Frame(window)
radio_var = tk.IntVar()
R1 = tk.Radiobutton(radiof, text="Download song", variable=radio_var, value=1)
R1.select() # A graphical glitch occurs when we don't provide a value to be selected.
R2 = tk.Radiobutton(radiof, text="Download video", variable=radio_var, value=2)
R3 = tk.Radiobutton(radiof, text="Download songs from a playlist", variable=radio_var, value=3)
R4 = tk.Radiobutton(radiof, text="Download videos from a playlist", variable=radio_var, value=4)

# LINK
linkf = tk.Frame(window)
linkt = tk.Label(linkf, text="Link:")
linki = tk.Entry(linkf, width=100)
linkb = tk.Button(linkf, text="Download",  command=download)
#endregion

## RENDER
#region
radiof.grid(column=1, row=1)
R1.grid()
R2.grid()
R3.grid()
R4.grid()

bitratef.grid(column=2, row=1)
bitratet.grid(column=1, row=1)
bitratei.grid(column=2, row=1)

linkf.grid(column=1, row=2, columnspan=2)
linkt.grid()
linki.grid()
linkb.grid()

window.mainloop()
#endregion
#endregion