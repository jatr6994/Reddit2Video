from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

chrome_opts = Options()
# chrome_opts.add_argument( "--headless" );

chrome_driver = os.getcwd() + r"\chromedriver.exe"
print(chrome_driver)
driver = webdriver.Chrome( chrome_options=chrome_opts, executable_path=chrome_driver )

driver.get( r"file:///C:/Users/Jacob/Desktop/Reddit2Video/cssAnim.html" )

# driver.close();