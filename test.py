
# from tkinter import *

# root = Tk()
# root.geometry("300x300")
# root.title(" AutoBomb by Wara ")

# def read_input():
#     work_val = work_time.get("1.0", "end-1c")
#     rest_time_val = rest_time.get("1.0", "end-1c")
#     max_class_val = max_class.get("1.0", "end-1c")
#     print(work_val)
#     print(rest_time_val)
#     print(max_class_val)


# lb1 = Label(text = "เวลาทำงาน (นาที)")
# work_time = Text(root, height = 1,
#                 width = 25,
#                 bg = "light yellow")
# lb2 = Label(text = "เวลาพัก (นาที)")
# rest_time = Text(root, height = 1,
#                 width = 25,
#                 bg = "light yellow")
# lb3 = Label(text = "ระดับของฮีโร่สูงสุดที่จะทำงาน")
# lb4 = Label(text = "1 = common , 2 = rare ,3= super rare, 4 = epic")
# max_class = Text(root, height = 1,
#                 width = 25,
#                 bg = "light yellow")
# Output = Text(root, height = 5,
#               width = 25,
#               bg = "light cyan")
# Display = Button(root, height = 1,
#                  width = 10,
#                  text ="Run",
#                  command = lambda:read_input())

# lb1.pack()
# work_time.pack()
# lb2.pack()
# rest_time.pack()
# lb3.pack()
# lb4.pack()
# max_class.pack()
# Display.pack()
# Output.pack()

# mainloop()
# import pyautogui
# import time
# interval_check = 5
# common = None
# check_count = 0
# time.sleep(3)
# for i in range(11) :
#     print(i)
#     for box in pyautogui.locateAllOnScreen('rare.png',grayscale=False,confidence=.95):
#         print(pyautogui.center(box))
#         pyautogui.moveTo(pyautogui.center(box))
#         pyautogui.moveRel(290,-20) #rest
#         pyautogui.click()
#         # pyautogui.moveRel(220,-20) #work
#         pyautogui.sleep(2)
#     for box in pyautogui.locateAllOnScreen('common.png',grayscale=False,confidence=.95):
#         print(pyautogui.center(box))
#         pyautogui.moveTo(pyautogui.center(box))
#         pyautogui.moveRel(290,-20) #rest
#         pyautogui.click()
#         # pyautogui.moveRel(220,-20) #work
#         pyautogui.sleep(2)
#     for box in pyautogui.locateAllOnScreen('super_rare.png',grayscale=False,confidence=.95):
#         print(pyautogui.center(box))
#         pyautogui.moveTo(pyautogui.center(box))
#         pyautogui.moveRel(290,-20) #rest
#         pyautogui.click()
#         # pyautogui.moveRel(220,-20) #work
#         pyautogui.sleep(2)
#     for box in pyautogui.locateAllOnScreen('epic.png',grayscale=False,confidence=.95):
#         print(pyautogui.center(box))
#         pyautogui.moveTo(pyautogui.center(box))
#         pyautogui.moveRel(290,-20) #rest
#         pyautogui.click()
#         # pyautogui.moveRel(220,-20) #work
#         pyautogui.sleep(2)
#     for scroll in range (4):
#         pyautogui.scroll(-50)
#     pyautogui.sleep(0.5)

# print("end")
# while common == '' or common == None :
#     common = pyautogui.locateCenterOnScreen('disconnect.png',grayscale=False,confidence=.95)
#     print(common)
#     if common != None :
#         pyautogui.moveTo(common)
#         pyautogui.click()
#         check_count = 0
#     if check_count >= interval_check :
#         check_count = 0
#         print('break start')
#         break
#     else :
#         check_count +=1

import pyautogui
import time
windows = []
window_list = pyautogui.getWindowsWithTitle('Bombcrypto')

for w in window_list:
    windows.append({
        "window": w,
        "login": 0,
        "heroes": 0,
        "new_map": 0,
        "refresh_heroes": 0
    })
for active in windows:
    active["window"].activate()
    time.sleep(2)
print(window_list)
print(windows)
