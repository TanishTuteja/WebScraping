from selenium import webdriver
from selenium.webdriver.common.keys import Keys

defaultUsername = "cs1200398"
myUsername = input("Enter your username (" + defaultUsername + ") ")

if(myUsername == ""):
    myUsername = defaultUsername

myPassword = input("Enter your password ")

driver = webdriver.Chrome()
driver.get("https://moodle.iitd.ac.in/login/index.php")

usernameInput = driver.find_element_by_id("username")
usernameInput.clear()
usernameInput.send_keys(myUsername)

passwordInput = driver.find_element_by_id("password")
passwordInput.clear()
passwordInput.send_keys(myPassword)

formText = driver.find_element_by_id("login").text

if(not formText.find("first value") == -1):
    i = formText.find("first value") + len("first value") + 1
    number = ""
    while(not formText[i] == " "):
        number += formText[i]
        i += 1
    num = int(number)

elif(not formText.find("second value") == -1):
    i = formText.find("second value") + len("second value") + 1
    while(not formText[i] == " "):
        i += 1
    i += 3
    number = ""
    while(not formText[i] == " "):
        number += formText[i]
        i += 1
    num = int(number)

elif(not formText.find("add") == -1):
    i = formText.find("add") + len("add") + 1
    number1 = ""
    while(not formText[i] == " "):
        number1 += formText[i]
        i += 1
    num1 = int(number1)

    i += 3
    number2 = ""
    while(not formText[i] == " "):
        number2 += formText[i]
        i += 1
    num2 = int(number2)

    num = num1 + num2

elif(not formText.find("subtract") == -1):
    i = formText.find("subtract") + len("subtract") + 1
    number1 = ""
    while(not formText[i] == " "):
        number1 += formText[i]
        i += 1
    num1 = int(number1)

    i += 3
    number2 = ""
    while(not formText[i] == " "):
        number2 += formText[i]
        i += 1
    num2 = int(number2)

    num = num1 - num2

else:
    raise Exception("Unexpected Error")

captcha = driver.find_element_by_id("valuepkg3")
captcha.clear()
captcha.send_keys(str(num))

driver.find_element_by_id("loginbtn").click()
