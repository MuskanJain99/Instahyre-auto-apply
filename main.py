import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Load environment variables from .env file
load_dotenv()
EMAIL = os.getenv("INSTA_EMAIL")
PASSWORD = os.getenv("INSTA_PASSWORD")
DESIRED_OPTIONS = os.getenv("DESIRED_OPTIONS").split(',')

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://www.instahyre.com/login/")
time.sleep(3)  # Allow page to load

# Function to log in to Instahyre
def login():
    try:
        driver.find_element(By.NAME, "email").send_keys(EMAIL)
        driver.find_element(By.NAME, "password").send_keys(PASSWORD)
        driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()
        time.sleep(5)  # Wait for login to complete
    except Exception as e:
        print("Error during login:", e)
        driver.quit()
        exit()

# Function to select job functions
def select_job_functions():
    try:
        driver.get("https://www.instahyre.com/candidate/opportunities/")
        time.sleep(5)
        
        dropdowns = driver.find_elements(By.CLASS_NAME, "selectize-control")
        job_function_dropdown = dropdowns[1]
        
        # Clear existing selections
        for remove_button in job_function_dropdown.find_elements(By.CLASS_NAME, "remove"):
            remove_button.click()
            time.sleep(1)
        
        # Select new job functions
        dropdown_input = job_function_dropdown.find_element(By.TAG_NAME, "input")
        job_function_dropdown.click()
        time.sleep(1)
        
        for option in DESIRED_OPTIONS:
            dropdown_input.send_keys(option.strip())
            time.sleep(1)
            dropdown_input.send_keys(Keys.ENTER)
            time.sleep(1)
        
        # Apply filter
        driver.find_element(By.XPATH, "//button[contains(text(),'Show results')]").click()
        time.sleep(5)
    except Exception as e:
        print("Error selecting job functions:", e)

# Function to apply for jobs
def apply_for_jobs():
    try:
        view_buttons = driver.find_elements(By.XPATH, "//button[contains(text(),'View »')]")
        if view_buttons:
            view_buttons[0].click()
            time.sleep(5)
        
        apply_count = 0  # Counter for the number of applications
        
        while True:
            try:
                apply_button = driver.find_element(By.XPATH, "//button[contains(text(),'Apply')]")
                apply_button.click()
                time.sleep(5)  # Allow application to process
                apply_count += 1  # Increment the counter each time apply is clicked
            except Exception:
                print(f"Process complete. Total applications clicked: {apply_count}")
                break
    except Exception as e:
        print("Error clicking 'View' button:", e)

# Execute functions
login()
select_job_functions()
apply_for_jobs()

# Close the browser
driver.quit()
