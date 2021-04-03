import threading
import os, random, string
import colorama
from colorama import Fore, Style
import selenium
import psutil
import platform
from os import system
from datetime import datetime
from time import sleep
from selenium import webdriver
from discord.ext import commands
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
colorama.init()


reports = 0
system("title " + "[IRB] by Kinda Cute#0525")
system('mode con: cols=45 lines=20')

def logo():
    msg = Fore.LIGHTRED_EX+"""
            ██╗██████╗ ██████╗ 
            ██║██╔══██╗██╔══██╗
            ██║██████╔╝██████╔╝
            ██║██╔══██╗██╔══██╗
            ██║██║  ██║██████╔╝
            ╚═╝╚═╝  ╚═╝╚═════╝ 
                   """
    print(msg)

def report():
    global reports
    while True:
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"     
        options = webdriver.ChromeOptions()
        options.headless = True
        options.add_argument(f'user-agent={user_agent}')
        options.add_argument("--window-size=1920,1080")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--allow-running-insecure-content')
        options.add_argument("--disable-extensions")
        options.add_argument("--proxy-server='direct://'")
        options.add_argument("--proxy-bypass-list=*")
        options.add_argument("--start-maximized")
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
        system("title " + "Logs:[Loading Webpage]")
        driver.get('https://www.instagram.com/')
        system("title " + "Logs:[Webpage Loaded]")
        driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]').click()
        sleep(0.8)
        system("title " + "Logs:[Attempting to Login]")
        driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(username)
        sleep(random.randint(1, 3))
        driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
        sleep(random.randint(1, 3)) 
        driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()
        system("title " + "Logs:[Logged In!]")
        sleep(3)
        system("title " + "Logs:[Loading Account]")
        driver.get(f"https://www.instagram.com/{account}/")
        sleep(2)
        system("title " + "Logs:[Account Loaded!]")
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/button').click()
        sleep(random.randint(1, 3))
        system("title " + "Logs:[Reaporting...]")
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div/button[3]').click()
        sleep(random.randint(1, 3))
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[2]/div').click()
        sleep(random.randint(1, 3))
        if reason1 == "1":
            driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[1]/div').click()
            sleep(random.randint(1, 3))
            driver.find_element_by_xpath(f"/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[{reason12}]/div").click()
        elif reason1 == "2":
            driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[2]/div').click()
            sleep(random.randint(1, 3))
            driver.find_element_by_xpath(f"/html/body/div[5]/div/div/div/div[2]/div/div/div/fieldset/div[{reason13}]/label/div").click()
            sleep(random.randint(1, 3))
            driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[6]/button').click()
        else:
            pass
        reports += 1
        system("title " + "Logs:[Reported!]")
        os.system("cls")
        logo()
        print(Fore.WHITE+"━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(Fore.WHITE+"Account:"+Fore.LIGHTGREEN_EX+f"{account}")
        print(Fore.WHITE+"Reports:"+Fore.LIGHTGREEN_EX+f"{reports}")
        print(Fore.WHITE+"━━━━━━━━━━━━━━━━━━━━━━━━━")
        driver.quit()

os.system("cls")
logo()
print(Fore.LIGHTBLUE_EX+"[ ? ]"+Fore.WHITE+f"Username?: ")
username = input("")
os.system("cls")
logo()
print(Fore.LIGHTBLUE_EX+"[ ? ]"+Fore.WHITE+f"Password?: ")
password = input("")
os.system("cls")
logo()
print(Fore.LIGHTBLUE_EX+"[ ? ]"+Fore.WHITE+f"Account?: ")
account = input("")
system('mode con: cols=65 lines=25')
os.system("cls")
logo()
print(Fore.LIGHTBLUE_EX+"[ * ]"+Fore.WHITE+f"It's posting content that shouldn't be on instagram [1]")
print(Fore.LIGHTBLUE_EX+"[ * ]"+Fore.WHITE+f"It's pretending to be someone else [2]")
reason1 = input("")
os.system("cls")
logo()
if reason1 == "1":
    print(Fore.LIGHTBLUE_EX+"[ * ]"+Fore.WHITE+f"It's spam [1]")
    print(Fore.LIGHTBLUE_EX+"[ * ]"+Fore.WHITE+f"I just don't like it [2]")
    print(Fore.LIGHTBLUE_EX+"[ * ]"+Fore.WHITE+f"Suicide, self-injury or eating disorders [3]")
    print(Fore.LIGHTBLUE_EX+"[ * ]"+Fore.WHITE+f"Sale of illegal or regulated goods [4]")
    print(Fore.LIGHTBLUE_EX+"[ * ]"+Fore.WHITE+f"Nudity or sexual activity [5]")
    print(Fore.LIGHTBLUE_EX+"[ * ]"+Fore.WHITE+f"Hate speech or symbols [6]")
    print(Fore.LIGHTBLUE_EX+"[ * ]"+Fore.WHITE+f"Violence or dangerous organization [7]")
    print(Fore.LIGHTBLUE_EX+"[ * ]"+Fore.WHITE+f"Bullying or harassment [8]")
    print(Fore.LIGHTBLUE_EX+"[ * ]"+Fore.WHITE+f"Intellectual property violation [9]")
    print(Fore.LIGHTBLUE_EX+"[ * ]"+Fore.WHITE+f"Scam or fruad [10]")
    print(Fore.LIGHTBLUE_EX+"[ * ]"+Fore.WHITE+f"False information [11]")
    reason12 = input("")
    os.system("cls")
    logo()
elif reason1 == "2":
    print(Fore.LIGHTBLUE_EX+"[ * ]"+Fore.WHITE+f"Me [1]")
    print(Fore.LIGHTBLUE_EX+"[ * ]"+Fore.WHITE+f"Someone I know [2]")
    print(Fore.LIGHTBLUE_EX+"[ * ]"+Fore.WHITE+f"A celebrity or public figure [3]")
    print(Fore.LIGHTBLUE_EX+"[ * ]"+Fore.WHITE+f"A business or organization [4]")
    reason13 = input("")
    os.system("cls")
    logo()
else:
    pass
print(Fore.LIGHTGREEN_EX+"[ OK ]"+Fore.WHITE+f"Username [{username}]")
sleep(1)
print(Fore.LIGHTGREEN_EX+"[ OK ]"+Fore.WHITE+f"Password [{password}]")
sleep(1)
print(Fore.LIGHTGREEN_EX+"[ OK ]"+Fore.WHITE+f"Account [{account}]")
sleep(1)
print(Fore.LIGHTGREEN_EX+"[ OK ]"+Fore.WHITE+f"Reason 1 Number: [{reason1}]")
sleep(1)
if reason1 == "1":
    print(Fore.LIGHTGREEN_EX+"[ OK ]"+Fore.WHITE+f"Reason 2 Number: [{reason12}]")
    sleep(1)
elif reason1 == "2":
    print(Fore.LIGHTGREEN_EX+"[ OK ]"+Fore.WHITE+f"Reason 2 Number: [{reason13}]")
    sleep(1)
else:
    pass
system('mode con: cols=45 lines=20')
os.system("cls")
logo()
print(Fore.WHITE+"━━━━━━━━━━━━━━━━━━━━━━━━━")
print(Fore.WHITE+"Account:"+Fore.LIGHTGREEN_EX+f"{account}")
print(Fore.WHITE+"Reports:"+Fore.LIGHTGREEN_EX+f"{reports}")
print(Fore.WHITE+"━━━━━━━━━━━━━━━━━━━━━━━━━")
report()

