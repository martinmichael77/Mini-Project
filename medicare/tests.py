from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime


class Hosttest(TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.live_server_url = 'http://127.0.0.1:8000/'

    def tearDown(self):
        self.driver.quit()

    

    def test_01_login_page(self):
        driver = self.driver
        driver.get(self.live_server_url)
        driver.maximize_window()
        login=driver.find_element(By.CSS_SELECTOR,"a.nav-link[href='/login/']")
        login.click()
        time.sleep(2)
        login=driver.find_element(By.CSS_SELECTOR,"input#username")
        login.send_keys('kevin7')
        time.sleep(2)
        login=driver.find_element(By.CSS_SELECTOR,"input#password")
        login.send_keys('Kevin@123')
        time.sleep(2)
        login=driver.find_element(By.CSS_SELECTOR,"input#loginButton")
        login.click()
        time.sleep(3)
        login=driver.find_element(By.CSS_SELECTOR,"svg.svg-inline--fa.fa-user-circle.fa-w-16.fa-fw.text-primary")
        login.click()
        time.sleep(2)
        login=driver.find_element(By.CSS_SELECTOR,'a.dropdown-item[href="/user_profile/"]')
        login.click()
        time.sleep(2)
        login=driver.find_element(By.CSS_SELECTOR,'i.fas.fa-user-circle.fa-fw.text-primary')
        login.click()
        time.sleep(2)
        login=driver.find_element(By.CSS_SELECTOR,'a.dropdown-item[data-toggle="modal"][data-target="#logoutModal"]')
        login.click()
        time.sleep(2)
        login=driver.find_element(By.CSS_SELECTOR,'a.btn.btn-primary[href="/logout/"]')
        login.click()
        time.sleep(2)
        login=driver.find_element(By.CSS_SELECTOR,"a.nav-link[href='/login/']")
        login.click()
        time.sleep(2)
        login=driver.find_element(By.CSS_SELECTOR,"input#username")
        login.send_keys('admin')
        time.sleep(2)
        login=driver.find_element(By.CSS_SELECTOR,"input#password")
        login.send_keys('admin')
        time.sleep(2)
        login=driver.find_element(By.CSS_SELECTOR,"input#loginButton")
        login.click()
        time.sleep(3)
        login=driver.find_element(By.CSS_SELECTOR,'li#patient-info-link > a.nav-link > span[style="color: white"]')
        login.click()
        time.sleep(2)
        login=driver.find_element(By.CSS_SELECTOR,'a.btn.btn-primary[href="/export_csv/"]')
        login.click()
        time.sleep(2)
        login=driver.find_element(By.CSS_SELECTOR,'a.btn.btn-secondary[href="/export_pdf/"]')
        login.click()
        time.sleep(2)
        login=driver.find_element(By.CSS_SELECTOR,'li#add-doc > a.nav-link > span[style="color: white"]')
        login.click()
        time.sleep(2)
        login=driver.find_element(By.CSS_SELECTOR,'input#first_name.form-control[name="first_name"][placeholder="Your first name"]')
        login.send_keys('Abigail')
        time.sleep(1)
        login=driver.find_element(By.CSS_SELECTOR,'input#last_name.form-control[name="last_name"][placeholder="Your last name"]')
        login.send_keys('Hughes')
        time.sleep(1)
        login=driver.find_element(By.CSS_SELECTOR,'input#email.form-control[name="email"][placeholder="Your email address"]')
        login.send_keys('abigailhughes12@gmail.com')
        time.sleep(1)
        login=driver.find_element(By.CSS_SELECTOR,'select#specialization.form-control[name="specialization"]')
        login.click()
        time.sleep(1)
        login=driver.find_element(By.CSS_SELECTOR,'select#specialization.form-control[name="specialization"] > option[value="Allergists"]')
        login.click()
        time.sleep(1)
        login=driver.find_element(By.CSS_SELECTOR,'input#license_no.form-control[name="license_no"][placeholder="Your License Number"]')
        login.send_keys('MDIN1042')
        time.sleep(1)
        login=driver.find_element(By.CSS_SELECTOR,'input#phone.form-control[name="phone"][placeholder="Your Phone Number"]')
        login.send_keys('7865345678')
        time.sleep(1)
        login=driver.find_element(By.CSS_SELECTOR,'button[type="submit"].btn.btn-warning[style*="min-width: 15em"]')
        login.click()
        time.sleep(2)
        login=driver.find_element(By.CSS_SELECTOR,'li#doc-info > a.nav-link > span[style="color: white"]')
        login.click()
        time.sleep(2)
        login=driver.find_element(By.CSS_SELECTOR,'li#appoint > a.nav-link > span[style="color: white"]')
        login.click()
        time.sleep(2)
        login=driver.find_element(By.CSS_SELECTOR,'i.fas.fa-user-circle.fa-fw.text-primary')
        login.click()
        time.sleep(2)
        login=driver.find_element(By.CSS_SELECTOR,'a.dropdown-item[data-toggle="modal"][data-target="#logoutModal"]')
        login.click()
        time.sleep(2)
        login=driver.find_element(By.CSS_SELECTOR,'a.btn.btn-primary[href="/logout"]')
        login.click()
        time.sleep(2)

        