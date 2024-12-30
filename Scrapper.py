from selenium import webdriver

def scrape_website():
    driver = webdriver.Chrome()
    driver.get("https://www.md.dev/")
    
    gti = driver.find_element("xpath", "//xpath-to-gti").text
    task_id = driver.find_element("xpath", "//xpath-to-task-id").text
    driver.quit()
    
    return gti, task_id
