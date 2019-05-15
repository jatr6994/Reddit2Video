from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

chrome_opts = Options();
# chrome_opts.add_argument( "--headless" );

chrome_driver = os.getcwd() + "\\chromedriver.exe";

driver = webdriver.Chrome( chrome_options=chrome_opts, executable_path=chrome_driver );
driver.get( "file://C:\\Users\\7UR7L3\\Documents\\MEGAsync\\dev\\projects\\reddit2video\\Reddit2Video\\cssAnim.html" );



driver.close();