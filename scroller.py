from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import os
import signal

# Console colors
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray

def signal_handler(signal, frame):
    logo()
    print(B + '\n[' + C + '*' + B + '] ' + C + "CTRL + C" + W + " PRESSED\n")
    exit()

signal.signal(signal.SIGINT, signal_handler)

def start():
    logo()
    home()

def logo():
    os.system('clear')
    print(C + '''
        ╔══╗
        ║╔╗║
        ║╚╝╚╦═╦══╦╗╔╗╔╦══╦══╦═╗
        ║╔═╗║╔╣╔╗║╚╝╚╝║══╣║═╣╔╝
        ║╚═╝║║║╚╝╠╗╔╗╔╬══║║═╣║
        ╚═══╩╝╚══╝╚╝╚╝╚══╩══╩╝
        ╔═══╗       ____
        ║╔═╗║       ║║║║
        ║╚══╦══╦═╦══╣║║║╔══╦═╗
        ╚══╗║╔═╣╔╣╔╗║║║║║║═╣╔╝
        ║╚═╝║╚═╣║║╚╝║╚╣╚╣║═╣║
        ╚═══╩══╩╝╚══╩═╩═╩══╩╝
        ''')
    print(C + "         Done By:" + W + " ShyGorilla")
    print(C + "     https://github.com/ShyGorilla\n")

def home():
    print(B + '[' + C + '*' + B + '] ' + C + "Choose Option: \n")
    print(B + '[' + C + '1' + B + '] ' + C + "Instagram", end='\t')
    print(B + '[' + C + '2' + B + '] ' + C + "Twitter")
    print(B + '[' + C + '3' + B + '] ' + C + "Whatsapp", end='\t')
    print(B + '[' + C + '4' + B + '] ' + C + "Telegram")
    print(B + '[' + C + '5' + B + '] ' + C + "Facebook", end='\t')
    print(B + '[' + C + '6' + B + '] ' + C + "Tiktok")
    print(B + '[' + C + '7' + B + '] ' + C + "Other\n")
    print(B + '[' + C + '0' + B + '] ' + C + "Exit")

    num = input(B + '\n[' + C + '*' + B + '] ' + W)

    global driver
    try:
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome('driver/chromedriver', chrome_options=chrome_options)
    except:
        print(B + '\n[' + C + '*' + B + '] ' + R + "Could not import the driver\n")
        exit()

    if num == '1':
        driver.get('https://www.instagram.com/')
        time.sleep(3)
        logo()
        print(C + "        Instagram Scroller\n")
        print(B + '[' + C + '*' + B + '] ' + C + "Choose Option: \n")
        print(B + '[' + C + '1' + B + '] ' + C + "Scroll UP", end='\t')
        print(B + '[' + C + '2' + B + '] ' + C + "Scroll Down", end='\t')
        print(B + '[' + C + '0' + B + '] ' + C + "Main Menu")
        num1 = input(B + '\n[' + C + '*' + B + '] ' + W)
        if num1 == '1':
            print(B + '\n[' + C + '*' + B + '] ' + C + "Please navegate to the page you want to start scrolling")
            print(B + '[' + C + '*' + B + '] ' + C + "Press CTRL + C To Stop Scrolling")
            input(B + '[' + C + '*' + B + '] ' + C + "Press Enter to start scrolling...")
            try:
                scrollup()
            except:
                print(B + '\n[' + C + '*' + B + '] ' + R + "Something went wrong!!!\n")
                exit()
        elif num1 == '2':
            print(B + '\n[' + C + '*' + B + '] ' + C + "Please navegate to the page you want to start scrolling")
            print(B + '[' + C + '*' + B + '] ' + C + "Press CTRL + C To Stop Scrolling")
            input(B + '[' + C + '*' + B + '] ' + C + "Press Enter to start scrolling...")
            try:
                scrolldown()
            except:
                print(B + '\n[' + C + '*' + B + '] ' + R + "Something went wrong!!!\n")
                exit()
        elif num1 == '0':
            driver.close()
            start()
        else:
            driver.close()
            print(B + '\n[' + C + '*' + B + '] ' + R + "Wrong input\n")
            time.sleep(2)
            start()
    #Twitter
    elif num == '2':
        driver.get('https://twitter.com/login/')
        time.sleep(3)
        logo()
        print(C + "        Twitter Scroller\n")
        print(B + '[' + C + '*' + B + '] ' + C + "Choose Option: \n")
        print(B + '[' + C + '1' + B + '] ' + C + "Scroll UP", end='\t')
        print(B + '[' + C + '2' + B + '] ' + C + "Scroll Down", end='\t')
        print(B + '[' + C + '0' + B + '] ' + C + "Main Menu")
        num1 = input(B + '\n[' + C + '*' + B + '] ' + W)
        if num1 == '1':
            print(B + '\n[' + C + '*' + B + '] ' + C + "Please navegate to the page you want to start scrolling")
            print(B + '[' + C + '*' + B + '] ' + C + "Press CTRL + C To Stop Scrolling")
            input(B + '[' + C + '*' + B + '] ' + C + "Press Enter to start scrolling...")
            try:
                scrollup()
            except:
                print(B + '\n[' + C + '*' + B + '] ' + R + "Something went wrong!!!\n")
                exit()
        elif num1 == '2':
            print(B + '\n[' + C + '*' + B + '] ' + C + "Please navegate to the page you want to start scrolling")
            print(B + '[' + C + '*' + B + '] ' + C + "Press CTRL + C To Stop Scrolling")
            input(B + '[' + C + '*' + B + '] ' + C + "Press Enter to start scrolling...")
            try:
                scrolldown()
            except:
                print(B + '\n[' + C + '*' + B + '] ' + R + "Something went wrong!!!\n")
                exit()
        elif num1 == '0':
            driver.close()
            start()
        else:
            driver.close()
            print(B + '\n[' + C + '*' + B + '] ' + R + "Wrong input\n")
            time.sleep(2)
            start()
    #Whatsapp
    elif num == '3':
        driver.get('https://web.whatsapp.com')
        time.sleep(3)
        logo()
        print(C + "        Whatsapp Scroller\n")
        print(B + '[' + C + '*' + B + '] ' + C + "Choose Option: \n")
        print(B + '[' + C + '1' + B + '] ' + C + "Scroll UP", end='\t')
        print(B + '[' + C + '2' + B + '] ' + C + "Scroll Down", end='\t')
        print(B + '[' + C + '0' + B + '] ' + C + "Main Menu")
        num1 = input(B + '\n[' + C + '*' + B + '] ' + W)
        if num1 == '1':
            print(B + '\n[' + C + '*' + B + '] ' + C + "Please navegate to the page you want to start scrolling")
            print(B + '[' + C + '*' + B + '] ' + C + "Press CTRL + C To Stop Scrolling")
            input(B + '[' + C + '*' + B + '] ' + C + "Press Enter to start scrolling...")
            try:
                scrollup()
            except:
                print(B + '\n[' + C + '*' + B + '] ' + R + "Something went wrong!!!\n")
                exit()
        elif num1 == '2':
            print(B + '\n[' + C + '*' + B + '] ' + C + "Please navegate to the page you want to start scrolling")
            print(B + '[' + C + '*' + B + '] ' + C + "Press CTRL + C To Stop Scrolling")
            input(B + '[' + C + '*' + B + '] ' + C + "Press Enter to start scrolling...")
            try:
                scrolldown()
            except:
                print(B + '\n[' + C + '*' + B + '] ' + R + "Something went wrong!!!\n")
                exit()
        elif num1 == '0':
            driver.close()
            start()
        else:
            driver.close()
            print(B + '\n[' + C + '*' + B + '] ' + R + "Wrong input\n")
            time.sleep(2)
            start()

    #Telegram
    elif num == '4':
        driver.get('https://web.telegram.org/#/login')
        time.sleep(3)
        logo()
        print(C + "        Telegram Scroller\n")
        print(B + '[' + C + '*' + B + '] ' + C + "Choose Option: \n")
        print(B + '[' + C + '1' + B + '] ' + C + "Scroll UP", end='\t')
        print(B + '[' + C + '2' + B + '] ' + C + "Scroll Down", end='\t')
        print(B + '[' + C + '0' + B + '] ' + C + "Main Menu")
        num1 = input(B + '\n[' + C + '*' + B + '] ' + W)
        if num1 == '1':
            print(B + '\n[' + C + '*' + B + '] ' + C + "Please navegate to the page you want to start scrolling")
            print(B + '[' + C + '*' + B + '] ' + C + "Press CTRL + C To Stop Scrolling")
            input(B + '[' + C + '*' + B + '] ' + C + "Press Enter to start scrolling...")
            try:
                scrollup()
            except:
                print(B + '\n[' + C + '*' + B + '] ' + R + "Something went wrong!!!\n")
                exit()
        elif num1 == '2':
            print(B + '\n[' + C + '*' + B + '] ' + C + "Please navegate to the page you want to start scrolling")
            print(B + '[' + C + '*' + B + '] ' + C + "Press CTRL + C To Stop Scrolling")
            input(B + '[' + C + '*' + B + '] ' + C + "Press Enter to start scrolling...")
            try:
                scrolldown()
            except:
                print(B + '\n[' + C + '*' + B + '] ' + R + "Something went wrong!!!\n")
                exit()
        elif num1 == '0':
            driver.close()
            start()
        else:
            driver.close()
            print(B + '\n[' + C + '*' + B + '] ' + R + "Wrong input\n")
            time.sleep(2)
            start()

    #Facebook
    elif num == '5':
        driver.get('https://www.facebook.com/')
        time.sleep(3)
        logo()
        print(C + "        Facebook Scroller\n")
        print(B + '[' + C + '*' + B + '] ' + C + "Choose Option: \n")
        print(B + '[' + C + '1' + B + '] ' + C + "Scroll UP", end='\t')
        print(B + '[' + C + '2' + B + '] ' + C + "Scroll Down", end='\t')
        print(B + '[' + C + '0' + B + '] ' + C + "Main Menu")
        num1 = input(B + '\n[' + C + '*' + B + '] ' + W)
        if num1 == '1':
            print(B + '\n[' + C + '*' + B + '] ' + C + "Please navegate to the page you want to start scrolling")
            print(B + '[' + C + '*' + B + '] ' + C + "Press CTRL + C To Stop Scrolling")
            input(B + '[' + C + '*' + B + '] ' + C + "Press Enter to start scrolling...")
            try:
                scrollup()
            except:
                print(B + '\n[' + C + '*' + B + '] ' + R + "Something went wrong!!!\n")
                exit()
        elif num1 == '2':
            print(B + '\n[' + C + '*' + B + '] ' + C + "Please navegate to the page you want to start scrolling")
            print(B + '[' + C + '*' + B + '] ' + C + "Press CTRL + C To Stop Scrolling")
            input(B + '[' + C + '*' + B + '] ' + C + "Press Enter to start scrolling...")
            try:
                scrolldown()
            except:
                print(B + '\n[' + C + '*' + B + '] ' + R + "Something went wrong!!!\n")
                exit()
        elif num1 == '0':
            driver.close()
            start()
        else:
            driver.close()
            print(B + '\n[' + C + '*' + B + '] ' + R + "Wrong input\n")
            time.sleep(2)
            start()

    #Tiktok
    elif num == '6':
        driver.get('https://www.tiktok.com')
        time.sleep(3)
        logo()
        print(C + "        Tiktok Scroller\n")
        print(B + '[' + C + '*' + B + '] ' + C + "Choose Option: \n")
        print(B + '[' + C + '1' + B + '] ' + C + "Scroll UP", end='\t')
        print(B + '[' + C + '2' + B + '] ' + C + "Scroll Down", end='\t')
        print(B + '[' + C + '0' + B + '] ' + C + "Main Menu")
        num1 = input(B + '\n[' + C + '*' + B + '] ' + W)
        if num1 == '1':
            print(B + '\n[' + C + '*' + B + '] ' + C + "Please navegate to the page you want to start scrolling")
            print(B + '[' + C + '*' + B + '] ' + C + "Press CTRL + C To Stop Scrolling")
            input(B + '[' + C + '*' + B + '] ' + C + "Press Enter to start scrolling...")
            try:
                scrollup()
            except:
                print(B + '\n[' + C + '*' + B + '] ' + R + "Something went wrong!!!\n")
                exit()
        elif num1 == '2':
            print(B + '\n[' + C + '*' + B + '] ' + C + "Please navegate to the page you want to start scrolling")
            print(B + '[' + C + '*' + B + '] ' + C + "Press CTRL + C To Stop Scrolling")
            input(B + '[' + C + '*' + B + '] ' + C + "Press Enter to start scrolling...")
            try:
                scrolldown()
            except:
                print(B + '\n[' + C + '*' + B + '] ' + R + "Something went wrong!!!\n")
                exit()
        elif num1 == '0':
            driver.close()
            start()
        else:
            driver.close()
            print(B + '\n[' + C + '*' + B + '] ' + R + "Wrong input\n")
            time.sleep(2)
            start()
    elif num == '7':
        logo()
        url1 = input(B + '\n[' + C + '*' + B + '] ' + C + 'Enter the URL: ' + W)
        url = url1.replace(" ", "")
        try:
            driver.get(url)
        except:
            print(B + '\n[' + C + '*' + B + '] ' + R + "Something went wrong!!!\n")
            exit()
        time.sleep(3)
        print(B + '\n[' + C + '*' + B + '] ' + C + "Choose Option: \n")
        print(B + '[' + C + '1' + B + '] ' + C + "Scroll UP", end='\t')
        print(B + '[' + C + '2' + B + '] ' + C + "Scroll Down", end='\t')
        print(B + '[' + C + '0' + B + '] ' + C + "Main Menu")
        num1 = input(B + '\n[' + C + '*' + B + '] ' + W)
        if num1 == '1':
            print(B + '\n[' + C + '*' + B + '] ' + C + "Please navegate to the page you want to start scrolling")
            print(B + '[' + C + '*' + B + '] ' + C + "Press CTRL + C To Stop Scrolling")
            input(B + '[' + C + '*' + B + '] ' + C + "Press Enter to start scrolling...")
            try:
                scrollup()
            except:
                print(B + '\n[' + C + '*' + B + '] ' + R + "Something went wrong!!!\n")
                exit()
        elif num1 == '2':
            print(B + '\n[' + C + '*' + B + '] ' + C + "Please navegate to the page you want to start scrolling")
            print(B + '[' + C + '*' + B + '] ' + C + "Press CTRL + C To Stop Scrolling")
            input(B + '[' + C + '*' + B + '] ' + C + "Press Enter to start scrolling...")
            try:
                scrolldown()
            except:
                print(B + '\n[' + C + '*' + B + '] ' + R + "Something went wrong!!!\n")
                exit()
        elif num1 == '0':
            driver.close()
            start()
        else:
            driver.close()
            print(B + '\n[' + C + '*' + B + '] ' + R + "Wrong input\n")
            time.sleep(2)
            start()
    elif num == '0':
        driver.close()
        logo()
        exit()
    else:
        print(B + '\n[' + C + '*' + B + '] ' + R + "Wrong input\n")
        time.sleep(2)
        start()

def scrollup():
    element = driver.find_element_by_tag_name('body')
    while True:
        element.send_keys(Keys.PAGE_UP)
        time.sleep(0.25)
        element.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.25)
        element.send_keys(Keys.PAGE_UP)
        time.sleep(0.25)
        element.send_keys(Keys.PAGE_UP)
        time.sleep(0.25)

def scrolldown():
    element = driver.find_element_by_tag_name('body')
    while True:
        element.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.25)
        element.send_keys(Keys.PAGE_UP)
        time.sleep(0.25)
        element.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.25)
        element.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.25)

start()