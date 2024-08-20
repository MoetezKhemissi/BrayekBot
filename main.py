from default_hepler import *
from literals import *
from high_level import *
import time


email_list = read_email_list(EMAIL_FILE)
driver,display = init_driver()
driver.get(BASE_URL)
wait_and_click_xpath(driver, Xpath_list["CONSENT_COOKIE"])

results = process_emails(email_list, driver)

write_results_to_csv(results, output_file)

time.sleep(500)
