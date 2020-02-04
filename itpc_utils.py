from selenium import webdriver
import time


home_url = ''


def follow_menu(browser, link_list):
    # Follows a series of sub-menus provided by the list link_list.
    for i in range(0, len(link_list)):
        submit_button = browser.find_elements_by_link_text(link_list[i])
        submit_button[-1].click()
    return browser


def submit_field(browser, key_list, key_val_list):
    # Sets values of fields in key_list to corresponding values in key_val_list.
    # The length of key_val_list is one less than the length of key_list. The
    # last value of key_list is the submit button.
    for i in range(0,len(key_list)-1):
        ele = browser.find_element_by_id(key_list[i])
        ele.send_keys(key_val_list[i])
    button = key_list[-1]
    try:
        submit_button = browser.find_element_by_link_text(button)
    except:
        submit_button = browser.find_element_by_id(button)
    submit_button.click()
    return browser


def download_exg_list(browser, exg_name):
    # Downloads a list (.csv) corresponding to a particular exchange given by the argument exg_name.
    # It skims through pagination of list of exchanges to find the given exchange and initiates download.
    innerHTML = browser.execute_script("return document.body.innerHTML")
    while innerHTML.find(exg_name) == -1:
        submit_button_list = browser.find_elements_by_xpath("//a[@class='t20pagination']")  # Pending Faults Details
        # print(len(submitButtonList))
        if len(submit_button_list) == 1:
            submit_button_list[0].click()
        else:
            submit_button_list[1].click()
        innerHTML = browser.execute_script("return document.body.innerHTML")
    exg_list = browser.find_elements_by_xpath("//td[@headers='EXCHANGE_NAME']")
    flt_list = browser.find_elements_by_xpath("//a")
    flt_list = flt_list[4:]
    k = 0
    for exg in exg_list:
        if exg.text == exg_name:
            break
        else:
            k += 1
    item = 0
    '''for flt in exg_list:
        print('Item no.:{}, {}, {}'.format(item, exg_list[item].text, flt_list[item].text))
        item += 1'''

    submit_button = flt_list[k]
    submit_button.click()
    buttons = browser.find_elements_by_xpath("//a")
    dl_button = buttons[1]
    dl_button.click()
    time.sleep(10)
    return browser


def download_list(browser):
    # Downloads the list.
    buttons = browser.find_elements_by_xpath("//a")
    for button in buttons:
        if button.get_attribute('href').find("FLOW_EXCEL_OUTPUT") > -1:
            button.click()
            time.sleep(10)
            break
    return browser


def dl_ftth_faults(username, password):
    browser = login(username, password)
    link_list = ["Bharat Fiber", "Faults", "Pending Complaints"]
    browser = follow_menu(browser, link_list)
    key_list = ["P2_CIRCLE", "P2_SSA", "P2_GO"]
    key_val_list = ["KL", "THIRUVANANTHAPURAM"]
    browser = submit_field(browser, key_list, key_val_list)
    browser = download_list(browser)
    browser.get(home_url)
    return browser



def dl_ll_faults(username, password, browser):
    # browser = login(username, password)
    link_list = ["Faults", "Details", "Pending Faults Details"]
    browser = follow_menu(browser, link_list)
    key_list = ["P1_CIRCLE", "P1_SSA", "ENTER_PENDING_IN_DAYS", "P1_LL_BB", "P1_REPORT", "Go"]
    key_val_list = ["KL", "THIRUVANANTHAPURAM", "0", "0", "Details"]
    browser = submit_field(browser, key_list, key_val_list)
    browser = download_list(browser)
    browser.get(home_url)
    return browser


def login(username, password):
    url = 'http://10.196.215.54:7777/pls/apex/'
    browser = webdriver.Chrome()
    browser.get(url + 'f?p=204:1')  # navigate to the page
    username_field = browser.find_element_by_id("P101_USERNAME")  # username form field
    password_field = browser.find_element_by_id("P101_PASSWORD")  # password form field
    username_field.send_keys(username)
    password_field.send_keys(password)
    submit_button = browser.find_element_by_link_text("Login")
    submit_button.click()
    home_url = browser.find_elements_by_tag_name("a")[-1].get_attribute('href')
    return browser
