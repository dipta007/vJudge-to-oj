import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
from sys import platform as _platform

waitTime = 4
path = os.getcwd() + "/ac/"

def GetPathOfChromeDriver():
    path = os.getcwd() + "/chromedriver"
    if _platform == "linux" or _platform == "linux2":
        # linux
        path += "_linux"
    elif _platform == "darwin":
        # MAC OS X
        path += "_mac"
    elif _platform == "win32" or _platform == "win64":
        # Windows
        path += "_win"
    return path

driver = webdriver.Chrome(GetPathOfChromeDriver())


def CFLogIn(user, passwd):
    login_site = "http://codeforces.com/enter"
    driver.get(login_site)
    time.sleep(waitTime)
    username = driver.find_element_by_id("handle")
    password = driver.find_element_by_id("password")

    username.send_keys(user)
    password.send_keys(passwd)

    driver.find_element_by_class_name("submit").click()
    time.sleep(waitTime)


def CFSubmit(problemName, path):
    submit_site = "http://codeforces.com/problemset/submit"
    driver.get(submit_site)
    time.sleep(waitTime)

    problemField = driver.find_element_by_name("submittedProblemCode")
    dropDown = driver.find_element_by_name("programTypeId")
    codeFile = driver.find_element_by_name("sourceFile")

    problemField.send_keys(problemName)
    Select(dropDown).select_by_value("50")
    codeFile.send_keys(path)

    driver.find_element_by_class_name("submit").click()

    time.sleep(waitTime)


def Codeforces():
    CFLogIn("dipta007_v2", " .iamdipta. ")
    code_dir = path + "Codeforces/"
    os.chdir(code_dir)
    folders = [name for name in os.listdir(".") if os.path.isdir(name)]

    for folder in folders:
        problem_name = folder
        print(problem_name)
        os.chdir(code_dir + problem_name)

        files = [name for name in os.listdir(".") if os.path.isfile(name)]

        for file in files:
            CFSubmit(problem_name, code_dir + folder + "//" + file)
            break


def UVALogIn(user, passwd):
    login_site = "https://uva.onlinejudge.org/"
    driver.get(login_site)
    time.sleep(waitTime)
    driver.switch_to.frame(driver.find_element_by_xpath("/html/body/div[3]/iframe"))
    driver.find_element_by_xpath("//*[@id=\"cancel\"]").click()
    driver.switch_to.default_content()
    time.sleep(2)

    username = driver.find_element_by_name("username")
    password = driver.find_element_by_name("passwd")
    remember = driver.find_element_by_name("remember")

    username.send_keys(user)
    password.send_keys(passwd)
    remember.click()

    driver.find_element_by_name("Submit").click()
    time.sleep(waitTime)


def UVASubmit(problemName, path):
    submit_site = "https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=25"
    driver.get(submit_site)
    time.sleep(waitTime)

    problemField = driver.find_element_by_name("localid")
    dropDown = driver.find_elements_by_name("language")
    codeFile = driver.find_element_by_name("codeupl")

    problemField.send_keys(problemName)
    dropDown[4].click()
    # Select(dropDown).select_by_value("5")

    codeFile.send_keys(path)

    driver.find_element_by_css_selector(
        "#col3_content_wrapper form table tbody tr:nth-of-type(5) td:nth-of-type(2) input:nth-of-type(1)").click();
    # driver.find_element_by_class_name("Submit").click()

    time.sleep(waitTime)


def UVA():
    UVALogIn("dipta007", " .dipta007. ")
    code_dir = path + "UVA"
    os.chdir(code_dir)
    folders = [name for name in os.listdir(".") if os.path.isdir(name)]

    for folder in folders:
        problem_name = folder
        print(problem_name)
        os.chdir(code_dir + problem_name)

        files = [name for name in os.listdir(".") if os.path.isfile(name)]

        for file in files:
            UVASubmit(problem_name, code_dir + folder + "\\" + file)
            break


def LOJLogIn(user, passwd):
    login_site = "http://www.lightoj.com/login_main.php"
    driver.get(login_site)
    time.sleep(waitTime)

    username = driver.find_element_by_id("myuserid")
    password = driver.find_element_by_name("mypassword")
    remember = driver.find_element_by_name("myrem")

    username.send_keys(user)
    password.send_keys(passwd)
    remember.click()

    driver.find_element_by_name("Submit").click()
    time.sleep(waitTime)


def LOJSubmit(problemName, path):
    submit_site = "https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=25"
    driver.get(submit_site)
    time.sleep(waitTime)

    problemField = driver.find_element_by_name("localid")
    dropDown = driver.find_elements_by_name("language")
    codeFile = driver.find_element_by_name("codeupl")

    problemField.send_keys(problemName)
    dropDown[4].click()

    codeFile.send_keys(path)

    driver.find_element_by_css_selector("#col3_content_wrapper form table tbody tr:nth-of-type(5) td:nth-of-type(2) input:nth-of-type(1)").click();
    # driver.find_element_by_class_name("Submit").click()

    time.sleep(waitTime)


def LightOJ():
    LOJLogIn("iamdipta@gmail.com", " .dipta007. ")
    return
    code_dir = path + "LightOJ"
    os.chdir(code_dir)
    folders = [name for name in os.listdir(".") if os.path.isdir(name)]

    for folder in folders:
        problem_name = folder
        print(problem_name)
        os.chdir(code_dir + problem_name)

        files = [name for name in os.listdir(".") if os.path.isfile(name)]

        for file in files:
            LOJSubmit(problem_name, code_dir + folder + "\\" + file)
            break


'''****main start here****'''
if __name__ == "__main__":
    print("What do you want to do?")
    print("1. VJudge to Codeforces")
    print("2. VJudge to UVA")
    print("3. VJudge to LightOJ")

    cmd = int(input())
    if cmd == 1:
        Codeforces()
    elif cmd == 2:
        UVA()
    elif cmd == 3:
        LightOJ()
