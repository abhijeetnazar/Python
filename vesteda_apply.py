from selenium import webdriver
import time
 

while True:
    driver = webdriver.Chrome(r"C:/Users/abhijeet.nazar/Downloads/chromedriver_win32/chromedriver.exe")
    driver.get('https://www.vesteda.com/en/private-rentals/belangstellingsregistratie/log-in.aspx')

    vesteda_username = driver.find_element_by_id("ctl38_tbUsername")
    vesteda_username.send_keys("abhijeet.nazar@gmail.com")
    vesteda_password = driver.find_element_by_id("ctl38_tbPassword")
    vesteda_password.send_keys("")
    vesteda_button = driver.find_element_by_name("ctl38$btnSubmit")
    vesteda_button.click()

    #vesteda_surname = driver.find_element_by_name("ctl33$tbAchternaam")
    #vesteda_surname.send_keys("Nazar")

    #vesteda_button_final = driver.find_element_by_name("ctl33$btnSubmit2")
    #vesteda_button_final.click()
    driver.quit()
    time.sleep(10)
