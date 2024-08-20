from default_hepler import *
from literals import *
from high_level import *
import time
from pyvirtualdisplay import Display

email_list = read_email_list(EMAIL_FILE)
display = Display(visible=0, size=(1920, 1080))
display.start()
driver = init_driver()

driver.get(BASE_URL)
wait_and_click_xpath(driver, Xpath_list["CONSENT_COOKIE"])

results = process_emails(email_list, driver)

write_results_to_csv(results, output_file)

time.sleep(500)
