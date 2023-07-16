import time
import pyautogui
import tkinter as tk
from threading import Thread, Event


def move_mouse(stop_event):
    pyautogui.FAILSAFE = False
    while not stop_event.is_set():
        pyautogui.moveTo(960, 540, 2)
        time.sleep(10)
        if stop_event.is_set():
            break  # Exit the loop immediately if stop event is set
        pyautogui.moveTo(1060, 640, 2)
        pyautogui.click(button='right')


def start_program():
    global mouse_thread, stop_event
    if mouse_thread is None or not mouse_thread.is_alive():
        stop_event = Event()
        mouse_thread = Thread(target=move_mouse, args=(stop_event,))
        mouse_thread.start()
        start_button.config(relief=tk.SUNKEN)
        stop_button.config(relief=tk.RAISED)



def stop_program():
    global stop_event
    if stop_event is not None:
        stop_event.set()
        start_button.config(relief=tk.RAISED)
        stop_button.config(relief=tk.SUNKEN)

mouse_thread = None
stop_event = None

root = tk.Tk()
root.title("Auto Mouse Mover")
root.geometry("300x50")
root.title("Auto Mouse Mover")

start_button = tk.Button(root, text="Start", command=start_program, bg="green",  relief=tk.RAISED)
start_button.pack()

stop_button = tk.Button(root, text="Pause", command=stop_program, bg="red",  relief=tk.SUNKEN)
stop_button.pack()

root.mainloop()
