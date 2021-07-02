from tkinter import *
from tkinter import ttk
import time
import random


def partition(data, head, tail, draw_data, time_tick=100):
    border = head
    pivot = data[tail]

    draw_data(data, get_color_array(len(data), head, tail, border, border))
    time.sleep(time_tick)

    for j in range(head, tail):
        if data[j] < pivot:
            draw_data(data, get_color_array(len(data), head, tail, border, j, True))
            time.sleep(time_tick)
            data[border], data[j] = data[j], data[border]
            border += 1
        draw_data(data, get_color_array(len(data), head, tail, border, j))
        time.sleep(time_tick)

    draw_data(data, get_color_array(len(data), head, tail, border, tail, True))
    time.sleep(time_tick)
    data[border], data[tail] = data[tail], data[border]

    return border


def quick_sort(data, head, tail, draw_data, time_tick=100):  # head - starting index, tail - end index
    if head < tail:
        partition_index = partition(data, head, tail, draw_data, time_tick)
        quick_sort(data, head, partition_index-1, draw_data, time_tick)
        quick_sort(data, partition_index+1, draw_data, time_tick)


def get_color_array(data_len, head, tail, border, current_index, is_swaping=False):
    color_array = []
    for i in range(data_len):
        if i >= head and i <= tail:
            color_array.append('Grey')
        else:
            color_array.append('White')

        if i == tail:
            color_array[i] = 'Blue'
        elif i == border:
            color_array[i] = 'Red'
        elif i == current_index:
            color_array[i] = 'Yellow'

        if is_swaping:
            if i == border or i == current_index:
                color_array[i] = 'Green'

    return color_array


main_window = Tk()
main_window.title = 'Quick sort visualizer'
main_window.maxsize(800, 600)
main_window.config(bg='White')
select_alg = StringVar()
data = []


def draw_data(data, colorlist):
    canvas.delete('all')
    can_height = 380
    can_width = 550
    x_width = can_width / (len(data)+1)
    offset = 30
    spacing = 10
    normalized_data = [i / max(data) for i in data]

    for i, height in enumerate(normalized_data):
        x0 = i*x_width + offset + spacing
        y0 = can_height - height*340
        x1 = ((i+1)*x_width) + offset
        y1 = can_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorlist[i])
        canvas.create_text(x0+2, y0, anchor=SE, text=str(data[i]))

    main_window.update_idletasks()


def generate():
    global data
    minval = int(minEntry.get())
    maxval = int(maxEntry.get())
    sizeval = int(sizeEntry.get())
    data = []
    for i in range(sizeval):
        data.append(random.randrange(minval, maxval+1))
    draw_data(data, ['Red' for x in range(len(data))])


def start_algorithm():
    global data
    if not data:
        return
    if (algmenu.get() == 'Quick Sort'):
        quick_sort(data, 0, len(data)-1, draw_data, speedbar.get())
        draw_data(data, ['Green' for x in range(len(data))])

Mainframe = Frame(main_window, width=600, height=200, bg="Grey")
Mainframe.grid(row=0, column=0, padx=10, pady=5)
canvas = Canvas(main_window, width=600, height=380, bg="Grey")
canvas.grid(row=1, column=0, padx=10, pady=5)
Label(Mainframe, text="ALGORITHM", bg='Grey').grid(row=0, column=0, padx=5, pady=5, sticky=W)
algmenu = ttk.Combobox(Mainframe, textvariable=select_alg, values=["Quick Sort"])
algmenu.grid(row=0, column=1, padx=5, pady=5)
algmenu.current(0)
Button(Mainframe, text="START", bg="Blue", command=start_algorithm).grid(row=1, column=3,
                                                                         padx=5, pady=5)
speedbar = Scale(Mainframe, from_=0.10,
                 to=2.0, length=100, digits=2,
                 resolution=0.2, orient=HORIZONTAL,
                 label="Select Speed")
speedbar.grid(row=0, column=2,
              padx=5, pady=5)
sizeEntry = Scale(Mainframe, from_=3,
                  to=60, resolution=1,
                  orient=HORIZONTAL,
                  label="Size")
sizeEntry.grid(row=1, column=0,
               padx=5, pady=5)

minEntry = Scale(Mainframe, from_=0,
                 to=10, resolution=1,
                 orient=HORIZONTAL,
                 label="Minimun Value")
minEntry.grid(row=1, column=1,
              padx=5, pady=5)
maxEntry = Scale(Mainframe, from_=10,
                 to=100, resolution=1,
                 orient=HORIZONTAL,
                 label="Maximun Value")
maxEntry.grid(row=1, column=2,
              padx=5, pady=5)
Button(Mainframe, text="Generate", bg="Red", command=generate).grid(row=0, column=3,
                                                                    padx=5, pady=5)

main_window.mainloop()