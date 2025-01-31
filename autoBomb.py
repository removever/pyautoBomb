import pyautogui
import time
from check_function import *
import threading
import keyboard
event = threading.Event()
import os

from tkinter import *
root = Tk()
root.geometry("400x300")
root.title(" AutoBomb by Wara ")



lb1 = Label(text = "เวลาทำงาน (นาที)")
work_time = Text(root, height = 1,
                width = 25,
                bg = "light yellow")
lb2 = Label(text = "เวลาพัก (นาที)")
rest_time = Text(root, height = 1,
                width = 25,
                bg = "light yellow")
lb3 = Label(text = "ระดับของฮีโร่สูงสุดที่จะทำงาน")
lb4 = Label(text = "1 = common , 2 = rare ,3= super rare, 4 = epic")
max_class = Text(root, height = 1,
                width = 25,
                bg = "light yellow",
                )
Output = Text(root, height = 3, 
              width = 25, 
              bg = "light cyan")
Display = Button(root, height = 1,
                 width = 10, 
                 text ="Run",
                 command = lambda:read_input())
Output.insert(END, "รอทำงาน")

lb1.pack()
work_time.pack()
lb2.pack()
rest_time.pack()
lb3.pack()
lb4.pack()
max_class.pack()
Display.pack()
Output.pack()


def run_bot(input_work_time,input_rest_time,input_max_class) :

    while True:


        root.update()
        show_time = 0 
        work_time = input_work_time
        wait_time = input_rest_time
        max_class = input_max_class
        resize()
        check_disconnect()
        check_login()
        check_mtm()
        open_hero()
        set_hero_work(max_class,1)
        wait_loading()
        enter_map()
        #ทำงาน
        for x in range(work_time*60) : 
            show_time += 1
      
            if (show_time % 180) == 1 and show_time > 180 :
                remap()
            Output.delete("1.0", END)
            Output.insert(END, "WORK : ")
            Output.insert(END,show_time)
            root.update()
            time.sleep(1)
            
            print(show_time)
        show_time = 0
        back_button()
        open_hero()
        set_hero_rest()
        wait_loading()
        back_button()
        # #หยุดพัก
        for y in range(wait_time*60) : 
            show_time += 1
            Output.delete("1.0", END)
            Output.insert(END, "REST : ")
            Output.insert(END,show_time)
            root.update()
            time.sleep(1)
            print(show_time)



def stop():
    event.set()
    print("stop")
    os._exit(0)

keyboard.add_hotkey("esc", stop)

run_loop = False

def read_input():
    work_val = work_time.get("1.0", "end-1c")
    rest_time_val = rest_time.get("1.0", "end-1c")
    max_class_val = max_class.get("1.0", "end-1c")
    print(work_val)
    print(rest_time_val)
    print(max_class_val)
    Output.delete("1.0", END)
    Output.insert(END, "ทำงาน")
    run_bot(int(work_val),int(rest_time_val),int(max_class_val))

    
    


mainloop()



