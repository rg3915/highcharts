import time
from selenium import webdriver

page = webdriver.Firefox()
page.maximize_window()
time.sleep(0.5)

page.get('http://localhost:8000/dollar-graphic')
time.sleep(2)
page.save_screenshot('img/dollar.png')

page.get('http://localhost:8000/euro-graphic')
time.sleep(2)
page.save_screenshot('img/euro.png')

page.get('http://localhost:8000/product-graphic')
time.sleep(2)
page.save_screenshot('img/product.png')

page.quit()
