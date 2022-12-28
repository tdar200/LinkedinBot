import re
import json
import pandas as pd

cookies = 'li_sugr=f2b00637-1ddd-4f5b-9acf-45e3c8df18ac; bcookie="v=2&ffaf6781-38dd-4c34-889d-f620a557e739"; bscookie="v=1&202204240818353de76f65-7400-4480-84b9-e15a11850fedAQEzRdmV09nHS5U_nze4PmZMV3I1dQUR"; G_ENABLED_IDPS=google; li_theme=light; li_theme_set=app; aam_uuid=58885513126749314040361002239416051343; _gcl_au=1.1.165704049.1650827864; timezone=Asia/Karachi; _guid=b8306157-3b80-4093-ad06-de28fc971373; gpv_pn=www.linkedin.com/premium/survey/; s_ips=746; s_tp=746; visit=v=1&M; g_state={"i_l":0}; s_tslv=1671618823161; li_rm=AQGb85Gni02gigAAAYU8qe-nqmad4wFMfWO0uQniMLFizz0a92xoRKgcPyjPjkejCK1EoveyMMbkdSfmhyq22qIYzY-TEijZkdaL65p_8wyaKbQMbM2o0gKvjviMgobjvhN7UBIFx5p4yGCW-jKJv8h5ogmpxOAZNbUDN4ldATvmvPG84nsUUQcZNBEtm5g3aNYyzLZJsDlRcnwlQZo3gO5WXVkyAjTsjD8NNX_s5LXcsTv-mHYg76hQBOSNuWy7Vwz95WxnzyTxLiM-1FpTzMcxPT274JAzkIpeqQ_9hAK1qaFQDi3xdCV8S3pgi99bPgLO1HSIjidtqxtGq5c; AnalyticsSyncHistory=AQJyHMTAGe9xewAAAYVMH4eFDp0OPJ7AI4cT8EGsEvcfTlM6tLo8WiTLlyxDLVQBUgk7ZdC8-2tMY0QmvM_duw; lms_ads=AQGyH-CbubvvPgAAAYVMH4jQi-UlInTa9CmJea41G1hQ7UnK7KVVWZqBXkb80H3at1U4QGHkxyEsTq_qLDZsASC7GQU-AUMK; lms_analytics=AQGyH-CbubvvPgAAAYVMH4jQi-UlInTa9CmJea41G1hQ7UnK7KVVWZqBXkb80H3at1U4QGHkxyEsTq_qLDZsASC7GQU-AUMK; G_AUTHUSER_H=0; AMCVS_14215E3D5995C57C0A495C55@AdobeOrg=1; sdsc=1:1SZM1shxDNbLt36wZwCgPgvN58iw=; UserMatchHistory=AQI62Y1u50_wiAAAAYVWSTPvvHE8a-OqSoLDLzq91LWE_nzortF2C-XrksVg5lcdlz44pBUQ4FCtWy1ypqgwaag169VCdq2bQ8BdwqsCT92hrS0rA4Wg_rHKCIZGza1duqQB5f_SIAi5MY0o4X-d2ze_Uf1WLMxdoXGUdB8J0qDSDn1aFZCzR4YTvqXanz10B3950RbDtAd-tTKIxYCMYBiESb516n67ktiOZuDbuPi3gq8sZkofmivUfy3NOpszDLzX0Lm31TdS_bAqqS3rm7HP8wcg8mwFgkbGX6s; li_g_recent_logout=v=1&true; lang=v=2&lang=en-us; li_at=AQEDAS2CpzQB5l8yAAABhVZJYaAAAAGFelXloFYAq7Ll34u6uqylHo0fremif-5gqcI7sDeyyIXo8AO43DtkBvTbPc99XLbK7hkb9vwI8xhrtUcDh1f3uSE7xAH1NH_MtGLhUnFi2uYgJQwXyY6Ja9vE; liap=true; JSESSIONID="ajax:7495978248979683331"; lidc="b=VB04:s=V:r=V:a=V:p=V:g=4139:u=898:x=1:i=1672189928:t=1672262105:v=2:sig=AQFZ6MmOow0jWp8iLcgUrqtQ_NBebQkL"; AMCV_14215E3D5995C57C0A495C55@AdobeOrg=-637568504|MCIDTS|19354|MCMID|58702937013693114950418173561563338052|MCAAMLH-1672794732|3|MCAAMB-1672794732|RKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y|MCOPTOUT-1672197132s|NONE|MCCIDH|1377817735|vVersion|5.1.1'

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
with open(f"cookiesGmail.txt", 'w') as f:
    f.write(json_values)

with open(f"cookiesGmail.txt", 'r') as f:
    file_content = f.read()
    json_object = json.loads(file_content)
    # Split the line by the delimiter (comma in this case)
    # print(line)
    # Access the first element
    # print(first_element)
for cookie in json_object:
    print(cookie)
    # driver.add_cookie(cookie)