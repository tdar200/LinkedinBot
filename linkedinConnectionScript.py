from selenium import webdriver
import time
import json
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException, ElementNotInteractableException
import pandas as pd
import random
from dotenv import load_dotenv
import os

load_dotenv()

driver = webdriver.Chrome()

# cookies = {
#     "name": "cookie1",
#     "value":
#     'li_rm=AQEMvTibtw6rygAAAYVQWm2MmG8Q2p2vJCf40i2gcS-emvB3l7qk3nUQ9Nq4jaUEtICYhJ60lQEK5IRCDVIYag1W6M6I6aJT24SgMRB7Es3xtQ5tbH1BinoT; bcookie="v=2&627c3899-6e46-4190-8ffe-139b31363ec2"; bscookie="v=1&202212262133017d74af9e-175c-4dfd-87ea-684ec1881d93AQG-iPojEdXAnZdbyDIQFXaavWYw6OKS"; lidc="b=OB76:s=O:r=O:a=O:p=O:g=2540:u=6:x=1:i=1672094645:t=1672180944:v=2:sig=AQGL5jDewLfPMHwp7JITHQ47BU6xViIt"; G_ENABLED_IDPS=google; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-637568504%7CMCIDTS%7C19353%7CMCMID%7C111246456308162389…7fGS_oIwag5oDtwTSFC4G1Ot6Xfi5lNyIW7Ka995IFoU-C0ozxW84ZJP68A; li_sugr=83642e72-eb43-4c83-bca4-12b07d24275d; _guid=67f7aaf0-b52e-4ca0-9bfc-fa1290910d06; AnalyticsSyncHistory=AQK_2WVXi2tJOgAAAYVQmgiTQLRUeYBqwbaJhXMZF6Wk8UQXvi4HLthI1Av1GQeQGLJ6vp31Oc-tlrnehhqMlg; lms_ads=AQFp63HYGwHPJAAAAYVQmgo4ILeqZC4z2t7MExJT1SlawwceBhuwpnivSvrsEuxyADstvdccfvc1CZ85tHK9LpPQHOOBvZfg; lms_analytics=AQFp63HYGwHPJAAAAYVQmgo4ILeqZC4z2t7MExJT1SlawwceBhuwpnivSvrsEuxyADstvdccfvc1CZ85tHK9LpPQHOOBvZfg; _gcl_au=1.1.1309776783.1672094603',
#     "path": "/",
#     "domain": ".linkedin.com",
#     "expiry": None
# }

# driver.add_cookie(cookies)


def sleep_time():
    time_random = random.randint(6, 12)
    return time_random


driver.execute_cdp_cmd(
    "Network.setUserAgentOverride", {
        "userAgent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    })

driver.get("https://www.linkedin.com/login")

username_input = driver.find_element("css selector", "#username")
password_input = driver.find_element("css selector", "#password")
login_button = driver.find_element("css selector", ".btn__primary--large")

email = os.environ['EMAIL']
password = os.environ['PASSWORD']

username_input.send_keys(email)
password_input.send_keys(password)
login_button.click()

time.sleep(sleep_time() + 5)

with open(f"cookies.txt", 'r') as f:
    file_content = f.read()
    json_object = json.loads(file_content)

for cookie in json_object:
    driver.add_cookie(cookie)

driver.refresh()
print("cookies added")

time.sleep(sleep_time())

df = pd.read_excel('Companies.xlsx')

for index, row in df.iterrows():

    search_box = driver.find_element("css selector",
                                     ".search-global-typeahead__input")

    company_name = row.values[0]

    search_box.send_keys(company_name)
    search_box.send_keys(Keys.RETURN)

    time.sleep(sleep_time())

    companies_tab = driver.find_elements("css selector", ".artdeco-pill")

    for tabs in companies_tab:
        tabs_text = tabs.text
        if tabs_text == "Companies":
            tabs.click()
            break

    time.sleep(sleep_time())

    all_companies = driver.find_elements("css selector", ".app-aware-link ")

    for companies in all_companies:
        href_value = companies.get_attribute("href")

        if "company" in href_value:
            driver.get(f"{href_value}/people")
            df = df.drop(df.index[0])
            df.to_excel('Companies.xlsx', index=False)
            break

    time.sleep(sleep_time())

    try:

        search_recruiters = driver.find_element("css selector",
                                                "#people-search-keywords")
        search_recruiters.send_keys("recruiter")
        search_recruiters.send_keys(Keys.RETURN)
    except NoSuchElementException:
        error_search_box = driver.find_element(
            "css selector", ".search-global-typeahead__input")
        error_search_box.clear()
        continue

    time.sleep(sleep_time())
    all_recruiters = driver.find_elements(
        "css selector", ".org-people-profile-card__profile-info")
    recruiters_links = []
    recruiters_array_length = len(all_recruiters)

    if recruiters_array_length > 0:
        for recruiter in all_recruiters:
            try:
                link = recruiter.find_element("css selector", "a")
                html_link = link.get_attribute("href")
                recruiters_links.append(html_link)
            except NoSuchElementException:
                continue

    time.sleep(sleep_time())

    json_values = json.dumps(recruiters_links)
    with open(f"{company_name}.txt", 'w') as f:
        f.write(json_values)
    with open(f"{company_name}.txt", 'r') as f:
        recruiters_array = [line.strip() for line in f]
    recruiters_array_len = len(recruiters_array[0])

    try:
        new_recruiter_array = recruiters_array[0].split(", ")
        # print(new_recruiter_array, " new array top")
        for recruiter in new_recruiter_array:
            # print(recruiter)
            driver.get(recruiter.split('"')[1])
            time.sleep(sleep_time())
            recruiter_name = driver.find_element("css selector",
                                                 ".text-heading-xlarge")
            button_tabs = driver.find_elements(
                "css selector",
                f"[aria-label='Invite {recruiter_name.text} to connect']")
            # Invite Harish Kumar to connect
            # print(recruiter_name)
            for tabs in button_tabs:
                try:
                    tabs_text = tabs.text
                    if tabs_text == "Connect":
                        tabs.click()
                        time.sleep(sleep_time())
                        try:
                            add_note_tabs = driver.find_elements(
                                "css selector", "[aria-label='Add a note']")
                            for tabs in add_note_tabs:
                                tabs_text = tabs.text
                                if tabs_text == "Add a note":
                                    tabs.click()
                                    time.sleep(sleep_time())
                                    try:
                                        message_box = driver.find_element(
                                            "css selector", "#custom-message")
                                        message_box.send_keys(
                                            f"Hello {recruiter_name.text}, I noticed that you are a recruiter. I wanted to reach out to discuss potentially working together. I’m a Full-Stack Developer with 5 years of experience working on technologies such as React, Node, React Native and I’m currently seeking new opportunities."
                                        )
                                        send_button = driver.find_element(
                                            "css selector",
                                            "[aria-label='Send now']")
                                        send_button.click()
                                        time.sleep(sleep_time())
                                    except NoSuchElementException:
                                        continue
                                    break
                        except NoSuchElementException:
                            continue
                        break
                    elif tabs_text == "Pending":
                        break

                except ElementClickInterceptedException:
                    break
    except IndexError:
        continue

    df = df.drop(df.index[0])
    df.to_excel('Companies.xlsx', index=False)
    print(df, " at the end")
