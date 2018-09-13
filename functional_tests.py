from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://localhost:8000')

# django default welcome page. ensures the django startproject command ran fine
assert 'Django' in browser.title


browser.quit()
