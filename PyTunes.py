import tkinter as tk
from tkinter import *
import os
import fnmatch
from pygame import mixer
from random import sample

mixer.init()

Root = tk.Tk()
Root.title("Py Tunes")
Root.geometry("557x850")

bg_label = Label(Root, bg='black')
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# CONTRAST

var1 = 0


def contrast():
    global var1
    var1 += 1
    if (var1 % 2) != 0:
        bg_label.config(bg="white")
        align.config(bg='white')
        label.config(bg='white')
        def_label.config(bg='white')
        listbox.config(bg='PeachPuff2', fg='Red')
        status_bar.config(bg='white', fg='black')
        align.config(bg='white')
        prev_button.config(bg='white')
        pause_button.config(bg='white')
        play_button.config(bg='white')
        stop_button.config(bg='white')
        next_button.config(bg='white')
        extra_buttons.config(bg="white")
        shuffle_button.config(bg="white")

    elif (var1 % 2) == 0:
        bg_label.config(bg='black')
        align.config(bg='black')
        label.config(bg='black')
        def_label.config(bg='black')
        listbox.config(bg='black', fg='Turquoise2')
        status_bar.config(bg='black', fg='white')
        align.config(bg='black')
        prev_button.config(bg='black')
        pause_button.config(bg='black')
        play_button.config(bg='black')
        stop_button.config(bg='black')
        next_button.config(bg='black')
        extra_buttons.config(bg="black")
        shuffle_button.config(bg="black")


contrast_img = tk.PhotoImage(file='D:\\py tunes\\imgs\\contrast.png')
contrast_button = Button(Root, image=contrast_img, command=contrast)
contrast_button.pack(pady=5, padx=5, anchor=N, side='right')

# path
rootpath = "D:\\py tunes\\tunes"
pattern = "*.mp3"

# pytunes logo
Label(Root, text="Py Tunes", bg="gold", fg="lime green", font=('Kaushan Script', 40, 'bold')).pack(pady=10)

# vol_label
mute_label = tk.PhotoImage(file="D:\\py tunes\\imgs\\volume_mute.png")
low_label = tk.PhotoImage(file="D:\\py tunes\\imgs\\volume_low.png")
high_label = tk.PhotoImage(file="D:\\py tunes\\imgs\\volume_high.png")
def_label = Label(Root, bg='black', image=low_label)
def_label.pack(side='left', anchor=N, pady=5, padx=10)

# volume_buttons
vol = 0.2
vol_up_img = tk.PhotoImage(file="D:\\py tunes\\imgs\\vol_up.png")
vol_down_img = tk.PhotoImage(file="D:\\py tunes\\imgs\\vol_down.png")
mute_img = tk.PhotoImage(file="D:\\py tunes\\imgs\\mute_button.png")

vol_frame = tk.Frame(Root)
vol_frame.pack(padx=30, pady=5, anchor=E)

prev_vol = vol


def vol_up():
    global vol
    global prev_vol
    vol += 0.05
    if vol > 1:
        vol = 1
        def_label.config(image=high_label)
    elif vol == 0:
        def_label.config(image=mute_label)
    elif 0 < vol < 0.4:
        def_label.config(image=low_label)
    elif 0.4 <= vol <= 1:
        def_label.config(image=high_label)
    prev_vol = vol
    mixer.music.set_volume(vol)
    print('vol=', int(vol * 100))


def vol_down():
    global vol
    global prev_vol
    vol -= 0.05
    if vol < 0:
        vol = 0
        def_label.config(image=mute_label)
    elif vol == 0:
        def_label.config(image=mute_label)
    elif 0 < vol < 0.4:
        def_label.config(image=low_label)
    elif 0.4 <= vol <= 1:
        def_label.config(image=high_label)
    prev_vol = vol
    mixer.music.set_volume(vol)
    print('vol=', int(vol * 100))


def mute():
    global vol

    if mixer.music.get_volume() == 0:

        mixer.music.set_volume(prev_vol)
        if prev_vol == 0:
            def_label.config(image=mute_label)
        elif 0 < prev_vol < 0.4:
            def_label.config(image=low_label)
        elif 0.4 <= prev_vol <= 1:
            def_label.config(image=high_label)
        vol = prev_vol
    elif mixer.music.get_volume() != 0:
        vol = 0
        mixer.music.set_volume(vol)
        def_label.config(image=mute_label)
        vol = prev_vol

    print("vol=", int(vol * 100))
#    print('prev_vol=', int(prev_vol * 100))


vol_down_button = Button(vol_frame, text="-", command=vol_down, image=vol_down_img)
vol_down_button.pack(side='left')

mute_button = Button(vol_frame, text="X", command=mute, image=mute_img)
mute_button.pack(side='left')

vol_up_button = Button(vol_frame, text="+", command=vol_up, image=vol_up_img)
vol_up_button.pack(side='left')

# listbox
list_frame = Frame(Root)
list_frame.config()
scroll_bar = Scrollbar(list_frame, orient=VERTICAL)

listbox = tk.Listbox(list_frame, fg="Turquoise2", bg="black", font=('Ticking Timebomb BB', 30, 'bold'),
                     yscrollcommand=scroll_bar.set)
song_list_0 = []
for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        for i in filename:
            if i == ".":
                song_name = filename[:filename.index(i):]
                listbox.insert("end", song_name)
                song_list_0.append(song_name)
scroll_bar.config(command=listbox.yview)
scroll_bar.pack(side=RIGHT, fill=Y)
listbox.pack(anchor=N)
list_frame.pack(anchor=N, pady=10)

label = tk.Label(Root, text="", bg="black", fg='green', font=('Ticking Timebomb BB', 20, 'bold'))
label.pack(pady=20)


# Mixer functions
def play_time():
    current_song_pos = (mixer.music.get_pos()) // 1000
    status_bar.config(text=current_song_pos)
    status_bar.after(900, play_time)

    if current_song_pos == -1:

        if listbox.index(ACTIVE) != (listbox.size() - 1):
            mixer.music.set_volume(vol)
            if vol == 0:
                def_label.config(image=mute_label)
            elif 0 < vol < 0.4:
                def_label.config(image=low_label)
            elif 0.4 <= vol <= 1:
                def_label.config(image=high_label)

            next_song = listbox.curselection()
            next_song = next_song[0] + 1
            next_song_name = listbox.get(next_song)
            label.config(text=next_song_name)

            mixer.music.load(rootpath + "\\" + next_song_name + ".mp3")
            mixer.music.play(fade_ms=1000)

            listbox.select_clear(0, 'end')
            listbox.activate(next_song)
            listbox.select_set(next_song)
            file_data()

        else:
            mixer.music.set_volume(vol)
            if vol == 0:
                def_label.config(image=mute_label)
            elif 0 < vol < 0.4:
                def_label.config(image=low_label)
            elif 0.4 <= vol <= 1:
                def_label.config(image=high_label)

            first_song = listbox.get(0)
            label.config(text=first_song)

            mixer.music.load(rootpath + "\\" + first_song + ".mp3")
            mixer.music.play(fade_ms=1000)

            listbox.select_clear(0, 'end')
            listbox.activate(index=0)
            listbox.select_set(ACTIVE)
            file_data()


def select():
    mixer.music.set_volume(vol)
    if vol == 0:
        def_label.config(image=mute_label)
    elif 0 < vol < 0.4:
        def_label.config(image=low_label)
    elif 0.4 <= vol <= 1:
        def_label.config(image=high_label)

    label.config(text=listbox.get(ANCHOR))
    mixer.music.load(rootpath + "\\" + listbox.get(ANCHOR) + ".mp3")
    mixer.music.play(fade_ms=1000)
    file_data()
    play_time()


def Stop():
    mixer.music.fadeout(1000)
    listbox.select_clear("active")


def play_next():
    mixer.music.set_volume(vol)
    if vol == 0:
        def_label.config(image=mute_label)
    elif 0 < vol < 0.4:
        def_label.config(image=low_label)
    elif 0.4 <= vol <= 1:
        def_label.config(image=high_label)

    next_song = listbox.curselection()
    next_song = next_song[0] + 1
    next_song_name = listbox.get(next_song)
    label.config(text=next_song_name)

    mixer.music.load(rootpath + "\\" + next_song_name + ".mp3")
    mixer.music.play(fade_ms=1000)

    listbox.select_clear(0, 'end')
    listbox.activate(next_song)
    listbox.select_set(next_song)
    file_data()
    play_time()


def play_prev():
    next_song = listbox.curselection()
    next_song = next_song[0] - 1
    next_song_name = listbox.get(next_song)
    label.config(text=next_song_name)

    mixer.music.load(rootpath + "\\" + next_song_name + ".mp3")
    mixer.music.play(fade_ms=1000)
    mixer.music.set_volume(vol)
    if vol == 0:
        def_label.config(image=mute_label)
    elif 0 < vol < 0.4:
        def_label.config(image=low_label)
    elif 0.4 <= vol <= 1:
        def_label.config(image=high_label)

    listbox.select_clear(0, 'end')
    listbox.activate(next_song)
    listbox.select_set(next_song)
    file_data()
    play_time()


var2 = 0


def pausee():
    global var2
    var2 += 1
    if (var2 + 1) % 2 == 0:
        mixer.music.pause()

    elif var2 % 2 == 0:

        mixer.music.unpause()


# mixer BUTTONS

prev_img = tk.PhotoImage(file="D:\\py tunes\\imgs\\back.png")
pause_img = tk.PhotoImage(file="D:\\py tunes\\imgs\\pause.png")
play_img = tk.PhotoImage(file="D:\\py tunes\\imgs\\play.png")
next_img = tk.PhotoImage(file="D:\\py tunes\\imgs\\next.png")
stop_img = tk.PhotoImage(file="D:\\py tunes\\imgs\\stop.png")

align = tk.Frame(Root, bg="black")
align.pack(padx=10, anchor=S)

prev_button = tk.Button(Root, text='prev', image=prev_img, bg="black", borderwidth=0, command=play_prev)
prev_button.pack(pady=10, in_=align, side="left")

pause_button = tk.Button(Root, text='pause', image=pause_img, bg="black", borderwidth=0, command=pausee)
pause_button.pack(pady=10, in_=align, side="left")

play_button = tk.Button(Root, text='play', image=play_img, bg="black", borderwidth=0, command=select)
play_button.pack(pady=10, in_=align, side="left")

stop_button = tk.Button(Root, text='stop', image=stop_img, bg="black", borderwidth=0, command=Stop)
stop_button.pack(pady=10, in_=align, side="left")

next_button = tk.Button(Root, text='next', image=next_img, bg="black", borderwidth=0, command=play_next)
next_button.pack(pady=10, in_=align, side="left")


# data

def file_reset():
    global song_list_0
    base_file = open('data.txt', 'w')
    for i in song_list_0:
        base_file.write(i)
    base_file.close()


def file_data():
    data = open('data.txt')
    song_list = data.read().split('\n')
    #    print(song_list)
    data.close()

    data_write = open('data.txt', 'w')
    for elements in song_list:
        for song_name_char in elements:
            if song_name_char == "=":
                song_name = elements[:elements.index(song_name_char)]
                times_played = elements[elements.index(song_name_char) + 1::]

                if song_name == listbox.get(ACTIVE):
                    # print(int(times_played))
                    ele_ind = song_list.index(elements)

                    song_list[ele_ind] = song_name + "=" + str(int(times_played) + 1)

    s1 = '\n'.join(song_list)
    data_write.write(s1)
    data_write.close()


# SHUFFLE
extra_buttons = tk.Frame(Root, bg="black")
extra_buttons.pack(anchor=NE)


def shufflee():
    global song_list_0
    song = listbox.curselection()
    song = song[0]

    shuffle_list = list(sample(song_list_0, len(song_list_0)))

    listbox.delete(0, END)
    for shuffled_song in shuffle_list:
        listbox.insert("end", shuffled_song)

    song_name = song_list_0[song]
    song_index = shuffle_list.index(song_name)
    listbox.select_clear(0, 'end')
    listbox.activate(song_index)
    listbox.select_set(song_index)
    song_list_0 = shuffle_list


shuffle_img = tk.PhotoImage(file="D:\\py tunes\\imgs\\shuffle.png")
shuffle_button = Button(Root, text="shuffle", command=shufflee, image=shuffle_img)
shuffle_button.pack(padx=23, in_=extra_buttons)

status_bar = Label(Root, text='', bg='black', fg='white')
status_bar.pack(anchor=SE, pady=10)

Root.mainloop()
