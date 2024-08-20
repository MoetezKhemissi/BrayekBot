from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import *
from literals import *
from default_hepler import *
import csv
def wait_and_click_xpath(driver,xpath):
    wait = WebDriverWait(driver, DEFAULT_WAIT_TIME)  
    button = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    button.click()
    return driver
def wait_and_return(driver,xpath):
    wait = WebDriverWait(driver, DEFAULT_WAIT_TIME)  
    element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
    return element
def quick_wait_and_return(driver,xpath):
    wait = WebDriverWait(driver, DEFAULT_WAIT_TIME/2)  
    element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
    return element
def check_status(driver):
    try:
        # Check if the error message is present first
        quick_wait_and_return(driver, Xpath_list["NOT_FOUND"])
        print("not found ..")
        return "not found"
    except:
        pass
    
    try:
        # Check if the success message is present
        quick_wait_and_return(driver, Xpath_list["FOUND"])
        print("found ..")
        return "exists"
    except:
        print("unknown ..")
        return "unknown"  # Fallback if neither message is found
def read_email_list(file_path):
    with open(file_path, 'r') as file:
        emails = [line.strip() for line in file if line.strip()]  # Remove empty lines and strip whitespace
    return emails



def write_results_to_csv(results, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['email', 'status']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()  
        for result in results:
            writer.writerow(result)
def take_screenshot(driver, file_path):
    driver.save_screenshot(file_path)
def process_emails(email_list, driver):
    results = []

    for email in email_list:
        attempt = 0
        while attempt < 2:  # Attempt to process the email up to 2 times
            try:
                print("Parsing ", email, "..")
                email_input = wait_and_return(driver, Xpath_list["EMAIL_INPUT"])
                email_input.clear()
                slow_type(email_input, email)
                
                wait_and_click_xpath(driver, Xpath_list["RESET_PASSWORD_XPATH"])
                time.sleep(2)  
                
                status = check_status(driver)
                
                if status == "exists":
                    driver.refresh()
                    time.sleep(2)

                results.append({'email': email, 'status': status})
                
                if status != "unknown":
                    break  # Exit the loop if the status is not "unknown"
                
                else:
                    raise ValueError("Status returned as 'unknown'. Restarting driver...")

            except Exception as e:
                print(f"Error encountered: {e}. Restarting driver...")
                driver.quit()  # Close the current driver instance
                time.sleep(2)  # Short pause before restarting
                driver = init_driver()  # Restart the driver
                driver.get(BASE_URL)
                wait_and_click_xpath(driver, Xpath_list["CONSENT_COOKIE"])
                attempt += 1  # Increment attempt counter

    return results
