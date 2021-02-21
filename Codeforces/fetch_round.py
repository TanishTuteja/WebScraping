import sys
import os
import string

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

if(not len(sys.argv) == 2):
    print("Usage: python fetch_round.py <contest_number>")
    sys.exit(1)

contestNum = sys.argv[1]
baseURL = "https://codeforces.com/problemset/problem/" + contestNum + "/"

if(not os.path.exists("./" + contestNum)):
    os.mkdir("./" + contestNum)

driver = webdriver.Chrome()

i = 0

while(i < 26):
    currURL = baseURL + string.ascii_uppercase[i]
    driver.get(currURL)
    if(not driver.current_url == currURL):
        break

    currPath = "./" + contestNum + "/" + string.ascii_uppercase[i]

    if(not os.path.exists(currPath)):
        os.mkdir(currPath)

    problem = driver.find_element_by_class_name("problem-statement")
    problem.screenshot(currPath + "/problem.png")

    inputs = driver.find_elements_by_css_selector("div.input pre")
    outputs = driver.find_elements_by_css_selector("div.output pre")

    for j in range(len(inputs)):
        f = open(currPath + "/input" + str(j + 1) + ".txt", "w")
        f.write(inputs[j].text)
        f.close()

    for j in range(len(outputs)):
        f = open(currPath + "/output" + str(j + 1) + ".txt", "w")
        f.write(outputs[j].text)
        f.close()

    i += 1

driver.close()
