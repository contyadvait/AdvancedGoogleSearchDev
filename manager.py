import platform
import os
from selenium import webdriver


class Manager():
    def __init__(self):
        answering = True
        first_time = False
        while answering:
            answer = input("Would you like to open Google? Y/n WARNING: This does NOT work in Repl.it ")
            if answer == "y":
                while answering:
                    browser = input("""Enter your browser according to number:
[1] Mozilla Firefox
[2] Google Chrome
[3] Microsoft Edge
[4] Cancel
[5] Safari
Android support coming soon!
""")
                    if browser == 1:
                        # if platform.system() == "Darwin"
                        answering = False

                    elif browser == 2:
                        if platform.system() == "Windows":
                            driver = webdriver.Chrome("./browsermanage/webdrivers/chrome/windows.exe")
                        elif platform.system() == "Darwin":
                            if platform.machine == "arm64":
                                driver = webdriver.Chrome("./browsermanage/webdrivers/chrome/mchip")
                            else:
                                driver = webdriver.Chrome("./browsermanage/webdrivers/chrome/intelmac")
                        elif platform.system() == "Linux":
                                driver = webdriver.Chrome("./browsermanage/webdrivers/chrome/linux")     

                        
                        driver.get("https://google.com")                     

                    elif browser == 3:
                        pass
                    elif browser == 4:
                        answering == False
                    elif browser == 5:
                        if platform.system != "Darwin":
                            print("Safari is only available on Mac systems.")
                        else:
                            print("Enter password to enable Safari driver: ")
                            os.system("safaridriver --enable")
                            driver = webdriver.Safari()

                            driver.get("https://google.com")

            else:
                answering = False
        
    def openBrowser(browser, os):
        if browser == "chrome":
            if os == "windows":
                driver = webdriver.Chrome("./browsermanage/webdrivers/chrome/windows.exe")
            elif os == "m chip":
                driver = webdriver.Chrome("./browsermanage/webdrivers/chrome/mchip")
            elif os == "intel mac":
                driver = webdriver.Chrome("./browsermanage/webdrivers/chrome/intelmac")
            elif os == "linux":
                driver = webdriver.Chrome("./browsermanage/webdrivers/chrome/linux")
        elif browser == "safari":
            print("Enter password to enable Safari driver: ")
            os.system("safaridriver --enable")
            driver = webdriver.Safari()

        driver.get("https://google.com")
        
# File is incomplete, fix at end