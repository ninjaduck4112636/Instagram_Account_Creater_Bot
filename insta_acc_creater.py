from selenium import webdriver
from time import sleep
from random import choice
from selenium.webdriver.common.keys import Keys
import pyperclip

# path = C:/Users/New user/Desktop/Yahoo_Bulk_Account_bot/user_name_and_password.txt

try:
        driver = webdriver.Chrome('C:/Users/New user/Downloads/chromedriver.exe')

        lst = []
        number_for_account = ''

        count = 0

        number_list = list(map(lambda x : chr(x),list(range(48,58))))
        for _ in range(5):
                number_for_account += choice(number_list)

        print(number_for_account)
    
        number_of_accounts = int(input('Enter the Number of Account to Create: '))

        xxxnumber = list(map(lambda x : chr(x),list(range(48,58))))
        ynumber = ''
        for value in range(5):
                ynumber += choice(xxxnumber)
    
        for _ in range(number_of_accounts):
                with open('Boys_names.txt','r') as f:
                        with open('Girl_names.txt','r') as f1:
                                while f.readline().__len__()>0:
                                        lst.append(f.readline().strip('\n'))
                        while f.readline().__len__()>0:
                                lst.append(f.readline().strip('\n'))
                first_name = choice(lst).strip(' ')
                last_name = choice(lst).strip(' ')
                print(first_name,last_name)
                alpha_list = list(range(65,125))
                alpha_list = list(map(lambda x:chr(x),alpha_list))

                print(alpha_list)
                password = ''
        
                for value in range(choice(list(range(10,15)))):
                        password += choice(alpha_list)
                print(password)
                print(len(password))

                driver.get('https://www.instagram.com/accounts/emailsignup/?hl=en')
                sleep(5)
                # opening instagram

                delay_time = list(range(0.2,1.3))
                
                if count==0:
                        driver.execute_script('window.open('');')
                        sleep(3)
                driver.switch_to_window(driver.window_handles[1])
                print('Switched to TempMail')
                
                driver.get('https://temp-mail.org/en/')
                sleep(20)
                if count>0:
                        driver.find_element_by_xpath('//button[@id="click-to-delete"]').click()
                sleep(8)

                driver.switch_to_window(driver.window_handles[1])
                driver.find_element_by_xpath('//input[@id="mail"]').send_keys(Keys.CONTROL,'a')
                driver.find_element_by_xpath('//input[@id="mail"]').send_keys(Keys.CONTROL,'c')

                driver.switch_to_window(driver.window_handles[0])
                print('Switched to Instagram')
                sleep(3)


                e_mail_temp = pyperclip.paste()
                fullname_1 = first_name+' '+last_name
                username_1 = first_name+'_'+last_name+ynumber
                password_1 = password

                for value in e_mail_temp:
                        driver.find_element_by_xpath('//input[@aria-label="Mobile Number or Email"]').send_keys(value)
                        sleep(choice(delay_time))
                for value in fullname_1:
                        driver.find_element_by_xpath('//input[@aria-label="Full Name"]').send_keys(value)
                        sleep(choice(delay_time))
                for value in username_1:                        
                        driver.find_element_by_xpath('//input[@aria-label="Username"]').send_keys(value)
                        sleep(choice(delay_time))
                sleep(2)
                for value in password_1:
                        driver.find_element_by_xpath('//input[@aria-label="Password"]').send_keys()
                        sleep(choice(delay_time))
                sleep(4)
                driver.find_element_by_xpath('//button[@type="submit"]').click()
                sleep(10)
                
                year = list(range(1940,2002))
                month = list(range(3,9))
                day = list(range(1,28))
                
                driver.find_element_by_xpath('//select[@title="Month:"]').click()
                driver.find_element_by_xpath('//option[@value="'+str(choice(month))+'"]').click()
                sleep(choice(delay_time))

                driver.find_element_by_xpath('//select[@title="Day:"]').click()
                sleep(choice(delay_time))
                driver.find_element_by_xpath('//option[@value="'+str(choice(day))+'"]').click()
                sleep(choice(delay_time))

                driver.find_element_by_xpath('//select[@title="Year:"]').click()
                sleep(choice(delay_time))
                driver.find_element_by_xpath('//option[@value="'+str(choice(year))+'"]').click()
                sleep(1)
                
                driver.find_element_by_xpath('//button[contains(text(),"Next")]').click()
                sleep(10)

                # Enter Confirmation Code
                driver.switch_to_window(driver.window_handles[1])
                print('Switched to TempMail')
                sleep(15)

                driver.execute_script("window.scrollTo(0, 500)")
                sleep(10)
                driver.find_element_by_xpath('//a[@class="viewLink link"]/following::a/following::a/following::a/following::a').click()
                print('Clicked on the Mail')
                sleep(6)
                print('Mail is Opened')
                driver.execute_script("window.scrollTo(0, 900)")
                sleep(17)
                otp = driver.find_element_by_xpath('//td/following::td/following::td/following::td/following::td/following::td/following::td/following::td/following::td/following::td/following::td/following::td/following::td/following::td').text
                print(otp)
                driver.switch_to_window(driver.window_handles[0])
                for value in otp:
                        driver.find_element_by_xpath('//input[@aria-label="Confirmation Code"]').send_keys(value)
                        sleep(choice(delay_time))
                sleep(2)
                driver.find_element_by_xpath('//button[contains(text(),"Next")]').click()
                sleep(8)
                '''driver.find_element_by_xpath('//button[contains(text(),"Not Now")]').click()
                sleep(4)'''
                driver.find_element_by_xpath('//div[@class="recaptcha-checkbox-border"]').click()
                print('Clicked on Not-Robot checkbox')
                sleep(8)
                driver.find_element_by_xpath('//button[@title="Get an audio challenge"]').click()
                print('Clicked on Audio Button')
                '''

                # have to add reCaptcha code - going to create another folder to do a new automation of reCaptcha
                # -----------------------------------------------------------------------------------------------

                
                # Add the Files to Store the Data
                with open('Insta_Account_Details.txt', 'a') as f:
                        # e-mail,password,username
                        f.write(pyperclip.paste()+','+password+','+first_name+'_'+last_name+ynumber+'\n')

                #driver.switch_to_window(driver.window_handles[1])
                #print('Switched to TempMail')
                #driver.close()
                #print('TempMail Tab Closed')
                #sleep(2)
                #driver.switch_to_window(driver.window_handles[0])
                #sleep(3)

                sleep(6)
                random_number = random.randint(10,27)
                x_path = '//button[text()="Follow"]'


                for _ in range(random_number+1):
                        driver.find_element_by_xpath(x_path).click()
                        x_path += '/following::button'
                        print('Followed {} Person'.format(_))
                        random_time = random.randint(5,15)
                        sleep(random_time)

                driver.find_element_by_xpath('//img[@alt="{}\'s profile picture"]'.format(user_name)).click()
                print('Profile Icon Clicked')
                sleep(10)
                driver.find_element_by_xpath('//div[contains(text(),"Log Out")]').click()
                #driver.find_element_by_xpath('//button[@type="button"]').click()
                #print('Clicked on Setting\'s')
                #sleep(1)
                #driver.find_element_by_xpath('//button[contains(text(),"Log Out")]').click()
                print('Logged Out of Account')
                sleep(8)                        

                print('Insta Account Sucessfully Created')
                count+=1'''
except Exception as e:
        print(e)
'''finally:
        driver.quit()
        print('Browser Closed')'''
