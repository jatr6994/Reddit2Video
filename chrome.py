from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

chrome_opts = Options();
# chrome_opts.add_argument( "--headless" );

chrome_driver = os.getcwd() + "\\chromedriver.exe";

print( chrome_opts )
driver = webdriver.Chrome( options=chrome_opts, executable_path=chrome_driver );
driver.get( "https://www.google.com" );

# driver.close();