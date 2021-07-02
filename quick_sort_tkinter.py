import tkinter

main_window = tkinter.Tk()
main_window.title('Quick sort visualizer')
button = tkinter.Button(main_window, text='Stop', width=25, command=main_window.destroy)
button.pack()
canvas = tkinter.Canvas(main_window, width=640, height=480)
canvas.pack()
canvas_height = 20
canvas_width = 200
y = int(canvas_height / 2)
canvas.create_line(0, y, canvas_width, y)
main_window.mainloop()