# API to open browser (Microsoft Edge Chromiumn or Google Chrome) to prevent errors in Repl.it

from selenium import webdriver

def Init():
    pass

def openBrowser(browser, os):
    if browser == "chrome":
        if os == "windows":
            driver = webdriver.Chrome("./webdrivers/chrome/windows.exe")
        elif os == "m chip":
            driver = webdriver.Chrome("./webdrivers/chrome/mchip")
        elif os == "intel mac":
            driver = webdriver.Chrome("./webdrivers/chrome/intelmac")
        elif os == "linux":
            driver = webdriver.Chrome("./webdrivers/chrome/linux")
    elif browser == "safari":
        driver = webdriver.Safari()

    driver.get("https://google.com")
            

