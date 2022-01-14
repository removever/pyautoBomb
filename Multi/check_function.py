from tkinter.constants import TRUE
import pyautogui
import win32gui
import time


def current_page(w):
    w.activate()
    w.maximize()
    pyautogui.sleep(1)
    start = pyautogui.locateCenterOnScreen(
        './img/connect_wallet.PNG', grayscale=TRUE, confidence=.9)
    if start != None:
        return 'login'
    start = pyautogui.locateCenterOnScreen(
        './img/treasue_hunt.PNG', grayscale=TRUE, confidence=.9)
    if start != None:
        return 'home'
    start = pyautogui.locateCenterOnScreen(
        './img/back_btn.PNG', grayscale=TRUE, confidence=.9)
    if start != None:
        return 'treasue_hunt'
    start = pyautogui.locateCenterOnScreen(
        './img/back_btn.PNG', grayscale=TRUE, confidence=.9)
    if start != None:
        return 'hero_list'
    start = pyautogui.locateCenterOnScreen(
        './img/error_btn.PNG', grayscale=TRUE, confidence=.9)
    if start != None:
        return 'error_page'


def work_all(w):
    cp = current_page(w)
    if cp == 'treasue_hunt':
        hunt_to_home()
        pyautogui.sleep(1)
    home_to_hero()
    pyautogui.sleep(1)
    work_all_click()
    pyautogui.sleep(3)
    hero_list_to_home()
    pyautogui.sleep(1)
    home_to_hunt()


def remap(w, active):
    cp = current_page(w)
    if cp == 'error_page':
        ok_error()
        pyautogui.sleep(15)
        login()
        active['login'] = active['login'] + 1
        pyautogui.sleep(2)
        home_to_hunt()
    if cp == 'treasue_hunt':
        hunt_to_home()
        pyautogui.sleep(1)
        home_to_hunt()
    if cp == 'home':
        home_to_hunt()
    if cp == 'hero_list':
        hero_list_to_home()
        pyautogui.sleep(1)
        home_to_hunt()


def home_to_hunt():
    start = pyautogui.locateCenterOnScreen(
        './img/treasue_hunt.PNG', grayscale=TRUE, confidence=.9)
    pyautogui.moveTo(start)
    pyautogui.click()


def hunt_to_home():
    start = pyautogui.locateCenterOnScreen(
        './img/back_btn.PNG', grayscale=TRUE, confidence=.9)
    pyautogui.moveTo(start)
    pyautogui.click()


def home_to_hero():
    start = pyautogui.locateCenterOnScreen(
        './img/hero_list.PNG', grayscale=TRUE, confidence=.9)
    pyautogui.moveTo(start)
    pyautogui.click()


def work_all_click():
    start = pyautogui.locateCenterOnScreen(
        './img/work_all.PNG', grayscale=TRUE, confidence=.9)
    pyautogui.moveTo(start)
    pyautogui.click()


def hero_list_to_home():
    start = pyautogui.locateCenterOnScreen(
        './img/close_hreo_list.PNG', grayscale=TRUE, confidence=.9)
    pyautogui.moveTo(start)
    pyautogui.click()


def ok_error():
    start = pyautogui.locateCenterOnScreen(
        './img/error_btn.PNG', grayscale=TRUE, confidence=.9)
    pyautogui.moveTo(start)
    pyautogui.click()


def cp_resize(w, active):
    w.restore()
    w.resizeTo(550, 450)
    w.moveTo(active["x"], active["y"])


def login():
    start = pyautogui.locateCenterOnScreen(
        './img/connect_wallet.PNG', grayscale=TRUE, confidence=.9)
    pyautogui.moveTo(start)
    pyautogui.click()
    pyautogui.sleep(10)
    start = pyautogui.locateCenterOnScreen(
        './img/sign_btn.PNG', grayscale=TRUE, confidence=.9)
    pyautogui.moveTo(start)
    pyautogui.click()
