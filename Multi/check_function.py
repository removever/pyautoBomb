from tkinter.constants import TRUE
import pyautogui
import win32gui
import time
# ,region=(screen.left,screen.top,screen.width,screen.height)


def current_page(w):
    w.activate()
    w.activate()
    w.activate()
    pyautogui.sleep(1)
    start = pyautogui.locateCenterOnScreen(
        './img/connect_wallet.PNG', region=(w.left, w.top, w.width, w.height), grayscale=TRUE, confidence=.9)
    if start != None:
        return 'login'
    start = pyautogui.locateCenterOnScreen(
        './img/treasue_hunt.PNG', region=(w.left, w.top, w.width, w.height), grayscale=TRUE, confidence=.9)
    if start != None:
        return 'home'
    start = pyautogui.locateCenterOnScreen(
        './img/back_btn.PNG', region=(w.left, w.top, w.width, w.height), grayscale=TRUE, confidence=.9)
    if start != None:
        return 'treasue_hunt'
    start = pyautogui.locateCenterOnScreen(
        './img/back_btn.PNG', region=(w.left, w.top, w.width, w.height), grayscale=TRUE, confidence=.9)
    if start != None:
        return 'hero_list'
    start = pyautogui.locateCenterOnScreen(
        './img/error_btn.PNG', region=(w.left, w.top, w.width, w.height), grayscale=TRUE, confidence=.9)
    if start != None:
        return 'error_page'


def work_all(w):
    cp = current_page(w)
    if cp == 'treasue_hunt':
        hunt_to_home(w)
        pyautogui.sleep(1)
    home_to_hero(w)
    pyautogui.sleep(1)
    work_all_click(w)
    pyautogui.sleep(3)
    hero_list_to_home(w)
    pyautogui.sleep(1)
    home_to_hunt(w)


def remap(w, active):
    cp = current_page(w)
    if cp == 'error_page':
        ok_error(w)
        pyautogui.sleep(15)
        login(w, active)
        active['login'] = active['login'] + 1
        pyautogui.sleep(2)
        home_to_hunt(w)
    if cp == 'treasue_hunt':
        hunt_to_home(w)
        pyautogui.sleep(1)
        home_to_hunt(w)
    if cp == 'home':
        home_to_hunt()
    if cp == 'hero_list':
        hero_list_to_home(w)
        pyautogui.sleep(1)
        home_to_hunt(w)


def home_to_hunt(w):
    start = pyautogui.locateCenterOnScreen(
        './img/treasue_hunt.PNG', region=(w.left, w.top, w.width, w.height), grayscale=TRUE, confidence=.9)
    pyautogui.moveTo(start)
    pyautogui.click()


def hunt_to_home(w):
    start = pyautogui.locateCenterOnScreen(
        './img/back_btn.PNG', region=(w.left, w.top, w.width, w.height), grayscale=TRUE, confidence=.9)
    pyautogui.moveTo(start)
    pyautogui.click()


def home_to_hero(w):
    start = pyautogui.locateCenterOnScreen(
        './img/hero_list.PNG', region=(w.left, w.top, w.width, w.height), grayscale=TRUE, confidence=.9)
    pyautogui.moveTo(start)
    pyautogui.click()


def work_all_click(w):
    start = pyautogui.locateCenterOnScreen(
        './img/work_all.PNG', region=(w.left, w.top, w.width, w.height), grayscale=TRUE, confidence=.9)
    pyautogui.moveTo(start)
    pyautogui.click()


def hero_list_to_home(w):
    start = pyautogui.locateCenterOnScreen(
        './img/close_hreo_list.PNG', region=(w.left, w.top, w.width, w.height), grayscale=TRUE, confidence=.9)
    pyautogui.moveTo(start)
    pyautogui.click()


def ok_error(w):
    start = pyautogui.locateCenterOnScreen(
        './img/error_btn.PNG', region=(w.left, w.top, w.width, w.height), grayscale=TRUE, confidence=.9)
    pyautogui.moveTo(start)
    pyautogui.click()


def cp_resize(w, active):
    w.restore()
    w.resizeTo(550, 450)
    w.moveTo(active["x"], active["y"])


def login(w, active):
    w.maximize()
    pyautogui.sleep(2)
    start = pyautogui.locateCenterOnScreen(
        './img/connect_wallet.PNG',  grayscale=TRUE, confidence=.9)
    pyautogui.moveTo(start)
    pyautogui.click()
    pyautogui.sleep(10)
    start = pyautogui.locateCenterOnScreen(
        './img/sign_btn.PNG',  grayscale=TRUE, confidence=.9)
    pyautogui.moveTo(start)
    pyautogui.click()
    pyautogui.sleep(3)
    cp_resize(w, active)
