import tkinter

main_window = tkinter.Tk()
main_window.title('Quick sort visualizer')
button = tkinter.Button(main_window, text='Stop', width=25, command=main_window.destroy)
button.pack()
main_window.mainloop()