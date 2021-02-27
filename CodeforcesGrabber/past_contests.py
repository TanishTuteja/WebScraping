import sys
import os
import string

from selenium import webdriver


def fetchContest(contestNum, driver):
    baseURL = "https://codeforces.com/problemset/problem/" + contestNum + "/"

    if(not os.path.exists("./past/" + contestNum)):
        os.mkdir("./past/" + contestNum)

    i = 0

    while(i < 26):
        currURL = baseURL + string.ascii_uppercase[i]
        driver.get(currURL)
        if(not driver.current_url == currURL):
            break

        currPath = "./past/" + contestNum + "/" + string.ascii_uppercase[i]

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


if(not len(sys.argv) == 2):
    print("Usage: python past_contests.py <number_of_contests>")
    sys.exit(1)

num = int(sys.argv[1])
pages = num//100 + 1

if(num % 100 == 0):
    pages -= 1

if(not os.path.exists("./past")):
    os.mkdir("./past")

myURL = "https://codeforces.com/contests/page/"

driver = webdriver.Firefox(executable_path="../drivers/geckodriver.exe")
driver2 = webdriver.Firefox(executable_path="../drivers/geckodriver.exe")

for i in range(pages - 1):
    driver.get(myURL + str(i+1))
    contests = driver.find_elements_by_css_selector(".contests-table tr")
    for j in range(100):
        contestID = contests[j+1].get_attribute("data-contestid")
        fetchContest(contestID, driver2)


driver.get(myURL + str(pages))
contests = driver.find_elements_by_css_selector(".contests-table tr")

for j in range(num % 100):
    contestID = contests[j+1].get_attribute("data-contestid")
    fetchContest(contestID, driver2)

driver2.close()
driver.close()
