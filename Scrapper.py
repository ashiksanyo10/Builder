from selenium import webdriver
from selenium.webdriver.common.by import By

def scrape_website():
    driver = webdriver.Chrome()
    driver.get("https://www.md.dev/")
    
    try:
        gti = driver.find_element(By.XPATH, "//xpath-to-gti").text
        task_id = driver.find_element(By.XPATH, "//xpath-to-task-id").text
    except Exception as e:
        print(f"Error scraping website: {e}")
        gti, task_id = None, None
    finally:
        driver.quit()
    
    return gti, task_id
