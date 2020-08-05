#ini buat module bang
import time
from datetime import datetime
import calendar
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#yang ini isi sendiri bang username sama passowrdnya
usernameStr = "ini username"
passwordStr = "ini password"

#ini jadwal
mtkmin = 'Mon 07 30 00'
qurdis = 'Mon 09 00 00'
ppkn = 'Mon 10 30 00'
bio = 'Tue 07 30 00'
akidah = 'Tue 09 00 00'
b_indo = 'Tue 10 30 00'
fisika = 'Wed 07 30 00'
fikih = 'Wed 09 00 00'
sejarah = 'Wed 10 30 00'
matwa = 'Thu 07 30 00'
ski = 'Thu 09 00 00'
pjok = 'Thu 10 30 00'
kimia = 'Fri 07 30 00'
sbk = 'Fri 09 00 00'
lm = 'Fri 10 30 00'
b_inggris = 'Sat 07 30 00'
b_arab = 'Sat 09 00 00'
prakarya = 'Sat 10 00 00'

#ini eksekusinya bang
while kimia == 'Fri 07 30 00':
    #yang di atas variabel pasti bang
    now = datetime.now()
    sekarang = now.strftime('%a %H %M %S')
    print(sekarang)
    if sekarang == mtkmin:
        time.sleep(5)
        browser = webdriver.Chrome()
        browser.minimize_window()
        browser.get(('https://elearning.man1bandarlampung.sch.id'))

        username = browser.find_element_by_name('username')
        username.send_keys(usernameStr)

        password = browser.find_element_by_name('password')
        password.send_keys(passwordStr)

        nextButton = browser.find_element_by_xpath('//button[@type="submit"][@value="submit"]')
        nextButton.click()

        time.sleep(10)

        browser.get(('https://elearning.man1bandarlampung.sch.id/studentkelas/absensi/MTIxWU1UNA==/WCBNSUEgMyBNYXRlbWF0aWthIFBlbWluYXRhbg==/MTIx'))
        time.sleep(10)
        browser.quit()
        continue
    
    elif sekarang == ppkn:
        time.sleep(5)
        browser = webdriver.Chrome()
        browser.minimize_window()
        browser.get(('https://elearning.man1bandarlampung.sch.id'))

        username = browser.find_element_by_name('username')
        username.send_keys(usernameStr)

        password = browser.find_element_by_name('password')
        password.send_keys(passwordStr)

        nextButton = browser.find_element_by_xpath('//button[@type="submit"][@value="submit"]')
        nextButton.click()

        time.sleep(10)
        #ini url absennya bang
        browser.get(('https://elearning.man1bandarlampung.sch.id/studentkelas/absensi/MjEyNFdZOA==/UFBLbiBLZWxhcyBYIE1JQSAz/MjEy'))
        time.sleep(10)
        browser.quit()
        continue
    elif sekarang == bio:
        time.sleep(5)
        browser = webdriver.Chrome()
        browser.minimize_window()
        browser.get(('https://elearning.man1bandarlampung.sch.id'))

        username = browser.find_element_by_name('username')
        username.send_keys(usernameStr)

        password = browser.find_element_by_name('password')
        password.send_keys(passwordStr)

        nextButton = browser.find_element_by_xpath('//button[@type="submit"][@value="submit"]')
        nextButton.click()

        time.sleep(10)

        browser.get(('https://elearning.man1bandarlampung.sch.id/studentkelas/absensi/NDk0NlBRUw==/QklPIFggTUlBIDM=/NDk0'))
        time.sleep(10)
        browser.quit()
        continue
    elif sekarang == akidah:
        time.sleep(5)
        browser = webdriver.Chrome()
        browser.minimize_window()
        browser.get(('https://elearning.man1bandarlampung.sch.id'))

        username = browser.find_element_by_name('username')
        username.send_keys(usernameStr)

        password = browser.find_element_by_name('password')
        password.send_keys(passwordStr)

        nextButton = browser.find_element_by_xpath('//button[@type="submit"][@value="submit"]')
        nextButton.click()

        time.sleep(10)

        browser.get(('https://elearning.man1bandarlampung.sch.id/studentkelas/absensi/NTA1Q1BUNw==/WCBNSUEgMyBBS0lEQUggQUtITEFL/NTA1'))
        time.sleep(10)
        browser.quit()
        continue
    elif sekarang == b_indo:
        time.sleep(5)
        browser = webdriver.Chrome()
        browser.minimize_window()
        browser.get(('https://elearning.man1bandarlampung.sch.id'))

        username = browser.find_element_by_name('username')
        username.send_keys(usernameStr)

        password = browser.find_element_by_name('password')
        password.send_keys(passwordStr)

        nextButton = browser.find_element_by_xpath('//button[@type="submit"][@value="submit"]')
        nextButton.click()

        time.sleep(10)

        browser.get(('https://elearning.man1bandarlampung.sch.id/studentkelas/absensi/NDA5MjVQOQ==/WCBNSUEgMyBDZXJpYQ==/NDA5'))
        time.sleep(10)
        browser.quit()
        continue
    elif sekarang == fikih:
        time.sleep(5)
        browser = webdriver.Chrome()
        browser.minimize_window()
        browser.get(('https://elearning.man1bandarlampung.sch.id'))

        username = browser.find_element_by_name('username')
        username.send_keys(usernameStr)

        password = browser.find_element_by_name('password')
        password.send_keys(passwordStr)

        nextButton = browser.find_element_by_xpath('//button[@type="submit"][@value="submit"]')
        nextButton.click()

        time.sleep(10)
        
        browser.get(('https://elearning.man1bandarlampung.sch.id/studentkelas/absensi/NDU0RlpHUg==/WCBNSUEgMyBGSUtJSA==/NDU0'))
        time.sleep(10)
        browser.quit()
        continue
    elif sekarang == sejarah:
        time.sleep(5)
        browser = webdriver.Chrome()
        browser.minimize_window()
        browser.get(('https://elearning.man1bandarlampung.sch.id'))

        username = browser.find_element_by_name('username')
        username.send_keys(usernameStr)

        password = browser.find_element_by_name('password')
        password.send_keys(passwordStr)

        nextButton = browser.find_element_by_xpath('//button[@type="submit"][@value="submit"]')
        nextButton.click()

        time.sleep(10)
        
        browser.get(('https://elearning.man1bandarlampung.sch.id/studentkelas/absensi/NjA0N1Y2OQ==/WCBNSUEgMyBTRUpBUkFIIElORE9ORVNJQQ==/NjA0'))
        time.sleep(10)
        browser.quit()
        continue
    elif sekarang == matwa:
         time.sleep(5)
         browser = webdriver.Chrome()
         browser.minimize_window()
         browser.get(('https://elearning.man1bandarlampung.sch.id'))
         username = browser.find_element_by_name('username')
         username.send_keys(usernameStr)
         password = browser.find_element_by_name('password')
         password.send_keys(passwordStr)
         nextButton = browser.find_element_by_xpath('//button[@type="submit"][@value="submit"]')
         nextButton.click()
         time.sleep(10)
         browser.get(('https://elearning.man1bandarlampung.sch.id/studentkelas/absensi/OTcyTkNTMA==/TVRLIFdBSklCIFggTUlBIDM=/OTc='))
         time.sleep(10)
         browser.quit()
         continue
    elif sekarang == ski:
        time.sleep(5)
        browser = webdriver.Chrome()
        browser.minimize_window()
        browser.get(('https://elearning.man1bandarlampung.sch.id'))

        username = browser.find_element_by_name('username')
        username.send_keys(usernameStr)

        password = browser.find_element_by_name('password')
        password.send_keys(passwordStr)

        nextButton = browser.find_element_by_xpath('//button[@type="submit"][@value="submit"]')
        nextButton.click()

        time.sleep(10)
        
        browser.get(('https://elearning.man1bandarlampung.sch.id/studentkelas/absensi/MzI4TlFCUw==/U0tJIFggTUlBIDM=/MzI4'))
        time.sleep(10)
        browser.quit()
        continue
    elif sekarang == pjok:
        time.sleep(5)
        browser = webdriver.Chrome()
        browser.minimize_window()
        browser.get(('https://elearning.man1bandarlampung.sch.id'))

        username = browser.find_element_by_name('username')
        username.send_keys(usernameStr)

        password = browser.find_element_by_name('password')
        password.send_keys(passwordStr)

        nextButton = browser.find_element_by_xpath('//button[@type="submit"][@value="submit"]')
        nextButton.click()

        time.sleep(10)
        
        browser.get(('https://elearning.man1bandarlampung.sch.id/studentkelas/absensi/NjkzOUZIRA==/WCBNSUEgMyBQRU5KQVNLRVM=/Njkz'))
        time.sleep(10)
        browser.quit()
        continue
    elif sekarang == kimia:
        time.sleep(5)
        browser = webdriver.Chrome()
        browser.minimize_window()
        browser.get(('https://elearning.man1bandarlampung.sch.id'))

        username = browser.find_element_by_name('username')
        username.send_keys(usernameStr)

        password = browser.find_element_by_name('password')
        password.send_keys(passwordStr)

        nextButton = browser.find_element_by_xpath('//button[@type="submit"][@value="submit"]')
        nextButton.click()

        time.sleep(10)
        
        browser.get(('https://elearning.man1bandarlampung.sch.id/studentkelas/absensi/NTcwWlJESg==/WCBNSUEgMyBLSU1JQSBCVSBFRlJJWUVOVEk=/NTcw'))
        time.sleep(10)
        browser.quit()
        continue
    elif sekarang == sbk:
        time.sleep(5)
        browser = webdriver.Chrome()
        browser.minimize_window()
        browser.get(('https://elearning.man1bandarlampung.sch.id'))

        username = browser.find_element_by_name('username')
        username.send_keys(usernameStr)

        password = browser.find_element_by_name('password')
        password.send_keys(passwordStr)

        nextButton = browser.find_element_by_xpath('//button[@type="submit"][@value="submit"]')
        nextButton.click()

        time.sleep(10)
        
        browser.get(('https://elearning.man1bandarlampung.sch.id/studentkelas/absensi/MTQwUlkzNw==/WCBNSUEgMyBTRU5JIEJVREFZQQ==/MTQw'))
        time.sleep(10)
        browser.quit()
        continue
    elif sekarang == lm:
        time.sleep(5)
        browser = webdriver.Chrome()
        browser.minimize_window()
        browser.get(('https://elearning.man1bandarlampung.sch.id'))

        username = browser.find_element_by_name('username')
        username.send_keys(usernameStr)

        password = browser.find_element_by_name('password')
        password.send_keys(passwordStr)

        nextButton = browser.find_element_by_xpath('//button[@type="submit"][@value="submit"]')
        nextButton.click()

        time.sleep(10)
        
        browser.get(('https://elearning.man1bandarlampung.sch.id/studentkelas/absensi/NTkyVjhLWA==/WCBNSUEgMyBCSU5ETyBMTQ==/NTky'))
        time.sleep(10)
        browser.quit()
        continue
    elif sekarang == b_inggris:
        time.sleep(5)
        browser = webdriver.Chrome()
        browser.minimize_window()
        browser.get(('https://elearning.man1bandarlampung.sch.id'))

        username = browser.find_element_by_name('username')
        username.send_keys(usernameStr)

        password = browser.find_element_by_name('password')
        password.send_keys(passwordStr)

        nextButton = browser.find_element_by_xpath('//button[@type="submit"][@value="submit"]')
        nextButton.click()

        time.sleep(10)
        
        browser.get(('https://elearning.man1bandarlampung.sch.id/studentkelas/absensi/NDg1M1hGQw==/WCBNSUEgMw==/NDg1'))
        time.sleep(10)
        browser.quit()
        continue
    elif sekarang == b_arab:
        time.sleep(5)
        browser = webdriver.Chrome()
        browser.minimize_window()
        browser.get(('https://elearning.man1bandarlampung.sch.id'))

        username = browser.find_element_by_name('username')
        username.send_keys(usernameStr)

        password = browser.find_element_by_name('password')
        password.send_keys(passwordStr)

        nextButton = browser.find_element_by_xpath('//button[@type="submit"][@value="submit"]')
        nextButton.click()

        time.sleep(10)
        
        browser.get(('https://elearning.man1bandarlampung.sch.id/studentkelas/absensi/NjY0SEszRA==/WCBNSUEgMyBCLiBBUkFC/NjY0'))
        time.sleep(10)
        browser.quit()
        continue
    elif sekarang == prakarya:
        time.sleep(5)
        browser = webdriver.Chrome()
        browser.minimize_window()
        browser.get(('https://elearning.man1bandarlampung.sch.id'))

        username = browser.find_element_by_name('username')
        username.send_keys(usernameStr)

        password = browser.find_element_by_name('password')
        password.send_keys(passwordStr)

        nextButton = browser.find_element_by_xpath('//button[@type="submit"][@value="submit"]')
        nextButton.click()

        time.sleep(10)
        
        browser.get(('https://elearning.man1bandarlampung.sch.id/studentkelas/absensi/NTMxMFAyWg==/WCBNSUEgMyBLV1U=/NTMx'))
        time.sleep(10)
        browser.quit()
        continue
    else:
        continue
        
    
    
