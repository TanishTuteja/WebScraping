import sys
import os
import string

from selenium import webdriver

if(not len(sys.argv) in [2, 3, 4]):
    print("Usage: python diff_range.py [min_difficulty] [max_difficulty] [number_of_problems]\nType d in parameters to use their default value.\nDefault Values : number_of_problems = 10, min_difficulty = 0, max_difficulty = infinite")
    sys.exit(1)

minDiff = -1
maxDiff = -1
num_of_problems = 10

if(len(sys.argv) == 2):
    if(not (sys.argv[1] == 'd' or sys.argv[1] == 'D')):
        minDiff = sys.argv[1]
        assert minDiff.isnumeric()

elif(len(sys.argv) == 3):
    if(not (sys.argv[1] == 'd' or sys.argv[1] == 'D')):
        minDiff = sys.argv[1]
        assert minDiff.isnumeric()
    if(not (sys.argv[2] == 'd' or sys.argv[2] == 'D')):
        maxDiff = sys.argv[2]
        assert maxDiff.isnumeric()

elif(len(sys.argv) == 4):
    if(not (sys.argv[1] == 'd' or sys.argv[1] == 'D')):
        minDiff = sys.argv[1]
        assert minDiff.isnumeric()
    if(not (sys.argv[2] == 'd' or sys.argv[2] == 'D')):
        maxDiff = sys.argv[2]
        assert maxDiff.isnumeric()
    if(not (sys.argv[3] == 'd' or sys.argv[3] == 'D')):
        num_of_problems = sys.argv[3]
        assert num_of_problems.isnumeric()
        num_of_problems = int(num_of_problems)

baseURL = "https://codeforces.com/problemset/"
driver = webdriver.Firefox(executable_path="../drivers/geckodriver.exe")

driver.get(baseURL)

if(not minDiff == -1):
    minDiffInput = driver.find_element_by_name("minDifficulty")
    minDiffInput.send_keys(minDiff)
if(not maxDiff == -1):
    maxDiffInput = driver.find_element_by_name("maxDifficulty")
    maxDiffInput.send_keys(maxDiff)

driver.find_element_by_css_selector(
    "#sidebar form input[type='submit']").click()

myPath = "./("
if(not minDiff == -1):
    myPath += minDiff
myPath += "-"
if(not maxDiff == -1):
    myPath += maxDiff
myPath += ")"

if(not os.path.exists(myPath)):
    os.mkdir(myPath)

problems = driver.find_elements_by_css_selector("table.problems td.id a")

i = 0
j = 0

problemDriver = webdriver.Firefox(executable_path="../drivers/geckodriver.exe")

while(i < num_of_problems):
    problem_id = problems[j].text
    problemPath = myPath + "/" + problem_id
    if(not os.path.exists(problemPath)):
        os.mkdir(problemPath)

    problemDriver.get(problems[j].get_attribute("href"))

    currProblem = problemDriver.find_element_by_class_name("problem-statement")
    currProblem.screenshot(problemPath + "/problem.png")

    inputs = problemDriver.find_elements_by_css_selector("div.input pre")
    outputs = problemDriver.find_elements_by_css_selector("div.output pre")

    for k in range(len(inputs)):
        f = open(problemPath + "/input" + str(k + 1) + ".txt", "w")
        f.write(inputs[k].text)
        f.close()

    for k in range(len(outputs)):
        f = open(problemPath + "/output" + str(k + 1) + ".txt", "w")
        f.write(outputs[k].text)
        f.close()

    j += 1

    if(j == len(problems)):
        activePage = driver.find_element_by_css_selector(
            "div.pagination span.active")
        currPageIndex = activePage.get_attribute("pageindex")
        newPageIndex = str(int(currPageIndex) + 1)
        driver.find_element_by_css_selector(
            "div.pagination span[pageindex=" + newPageIndex + "] a").click()
        j = 0

    i += 1

problemDriver.close()
driver.close()
