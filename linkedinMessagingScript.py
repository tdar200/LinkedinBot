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


def sleep_time():
    time_random = random.randint(7, 12)
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

with open("cookies.txt", 'r') as f:
    file_content = f.read()
    print(file_content, "file")
    json_object = json.loads(file_content)

    print(json_object, "json")

for cookie in json_object:
    print(cookie)
    driver.add_cookie(cookie)

driver.refresh()

time.sleep(sleep_time() + 10)

df = pd.read_excel('CompaniesMessaging.xlsx')

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
            df.to_excel('CompaniesMessaging.xlsx', index=False)
            print(df.head(5))
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
        for recruiter in new_recruiter_array:
            driver.get(recruiter.split('"')[1])
            time.sleep(sleep_time())
            try:
                button_tabs = driver.find_element("css selector",
                                                  ".entry-point")

                link_within_tab = button_tabs.find_element("css selector", "a")
                href_value_within_tab = link_within_tab.get_attribute("href")
                driver.get(href_value_within_tab)

                time.sleep(sleep_time())

                recruiter_name = driver.find_element(
                    "css selector", ".msg-compose__profile-link")

                message_box = driver.find_element(
                    "css selector", "[aria-label='Write a message…'")
                submit_button = driver.find_element("css selector",
                                                    "[type='submit']")
                message_box.click()
                message_box.send_keys(
                    f"Hello {recruiter_name.text}, I noticed that you are a recruiter. I wanted to reach out to discuss potentially working together. I’m a Full-Stack Developer with 5 years of experience working on technologies such as React, Node, React Native and I’m currently seeking new opportunities."
                )

                time.sleep(sleep_time() - 5)
                submit_button.click()

            except NoSuchElementException:
                print("this one is hitting")
                continue

    except IndexError:
        continue

    # df = df.drop(df.index[0])
    # df.to_excel('CompaniesMessaging.xlsx', index=False)
