import re
import json
import pandas as pd

cookies = 'li_sugr=f2b00637-1ddd-4f5b-9acf-45e3c8df18ac; bcookie="v=2&ffaf6781-38dd-4c34-889d-f620a557e739"; bscookie="v=1&202204240818353de76f65-7400-4480-84b9-e15a11850fedAQEzRdmV09nHS5U_nze4PmZMV3I1dQUR"; G_ENABLED_IDPS=google; li_theme=light; li_theme_set=app; aam_uuid=58885513126749314040361002239416051343; _gcl_au=1.1.165704049.1650827864; timezone=Asia/Karachi; _guid=b8306157-3b80-4093-ad06-de28fc971373; visit=v=1&M; li_rm=AQGb85Gni02gigAAAYU8qe-nqmad4wFMfWO0uQniMLFizz0a92xoRKgcPyjPjkejCK1EoveyMMbkdSfmhyq22qIYzY-TEijZkdaL65p_8wyaKbQMbM2o0gKvjviMgobjvhN7UBIFx5p4yGCW-jKJv8h5ogmpxOAZNbUDN4ldATvmvPG84nsUUQcZNBEtm5g3aNYyzLZJsDlRcnwlQZo3gO5WXVkyAjTsjD8NNX_s5LXcsTv-mHYg76hQBOSNuWy7Vwz95WxnzyTxLiM-1FpTzMcxPT274JAzkIpeqQ_9hAK1qaFQDi3xdCV8S3pgi99bPgLO1HSIjidtqxtGq5c; gpv_pn=www.linkedin.com/learning/paths/explore-app-development-with-the-mern-stack; s_tp=3958; s_tslv=1672268000377; s_ips=750.8000001907349; AnalyticsSyncHistory=AQKjrcmQT-vfUQAAAYVfPg0el-KJiVyPWXJ2Igr1mouztYdGxAb2uXbNwhLcvD5jolURKTFOMdJwfkHx0pQHOA; lms_ads=AQFjJo8O_P6iUAAAAYVfPg7-XPzo2_3Uk5itWaaKVSI1e5iN57EaxGN9ad-1NYZ8khml3614FZnq7yrIqUn7tK_l8aLAi8XP; lms_analytics=AQFjJo8O_P6iUAAAAYVfPg7-XPzo2_3Uk5itWaaKVSI1e5iN57EaxGN9ad-1NYZ8khml3614FZnq7yrIqUn7tK_l8aLAi8XP; g_state={"i_l":2,"i_p":1672432772020}; AMCVS_14215E3D5995C57C0A495C55@AdobeOrg=1; ln_or=eyI0MzQ2MTM3IjoiZCJ9; sdsc=22:1,1672360809272~JAPP,05lBGq69mSt0mpg1bs8koN3AHRWA=; li_g_recent_logout=v=1&true; lang=v=2&lang=en-us; G_AUTHUSER_H=0; li_at=AQEDARAjYeQDWkd3AAABhWT8QhMAAAGFiQjGE00AokaPDCsFeXN71tSMQobikQp22EcqLFv8PbHlHx5ujtoP1dXXJxOrtgwBWXkgTDmQnu90qisW8ZEfZx34Si8uXt9Nzjsr3qBpsuFg5U2bguKRqW4M; liap=true; JSESSIONID="ajax:2385058414579874882"; UserMatchHistory=AQJ6yDOJ6R8JkAAAAYVk_EsCA6sudmfP0JYtaYHqknV10ia8UNQPePduUUJkwosA60Byfwp4bV8V81g3aY4UEEiSLaTzt_ZTIkPWoh4-gPrzyTGbk5FuytjdgarCwA9S40Q-oLJPXLrHdxC5535WyR1DsgWY2dYC6eQyhilP2GHKr3XsIPd5NdI_OylpOEusOJFN-En8y0UuWY1XbE_WsIEniC-U5RkfzaUHSSNmk6DUpp_HnkWqUHtDZvbZoI1B3fqLO3kY3SdprYx0iO6GsTplQLhuu-VJJMtVVgU; AMCV_14215E3D5995C57C0A495C55@AdobeOrg=-637568504|MCIDTS|19356|MCMID|58702937013693114950418173561563338052|MCAAMLH-1673041335|3|MCAAMB-1673041335|RKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y|MCOPTOUT-1672443735s|NONE|MCCIDH|1469005175|vVersion|5.1.1; lidc="b=OB76:s=O:r=O:a=O:p=O:g=2550:u=6:x=1:i=1672436566:t=1672522932:v=2:sig=AQEOcLhbjF5gn7o9YZl30JO87ZgyLk3b"'

arr = []


def cookies_split(c):
    splitted = re.split(r'=("[^"]*"|[^\s]+)', c)
    obj = {
        "name": splitted[0].lstrip(),
        "value": splitted[1],
        "domain": ".www.linkedin.com"
    }
    return obj


cookie_arr = cookies.split(";")

for i in cookie_arr:
    i.lstrip()
    arr.append(cookies_split(i))

json_values = json.dumps(arr)
with open(f"cookies.txt", 'w') as f:
    f.write(json_values)

with open(f"cookies.txt", 'r') as f:
    file_content = f.read()
    json_object = json.loads(file_content)
    # Split the line by the delimiter (comma in this case)
    # print(line)
    # Access the first element
    # print(first_element)
for cookie in json_object:
    print(cookie)
    # driver.add_cookie(cookie)