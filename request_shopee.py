import requests
import json
import const


# headers = {
#     "Referer": "https://shopee.tw/search?keyword=google%20pixel",
#     "Cookie": const.Cookie,
#     "x-csrftoken": const.x_csrftoken,
#     "User-Agent": const.User_Agent
# }

headers = {
    "x-requested-with": "XMLHttpRequest",
    "x-api-source": "pc",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "if-none-match": "55b03-84f97a9961b9a98a415af2b114498793",
    "Referer": "https://shopee.tw/search?keyword=google%20pixel",
    "Cookie": 'SPC_IA=-1; SPC_F=cmPGQEkj3WT2dcc9bXDcnfKKLMcqJgeJ; REC_T_ID=8b48ea62-403f-11ea-9828-f8f21e1acf22; SPC_SI=ervkg693h4v8eyc4tnjiv34mf6vw0pb1; _gcl_au=1.1.282669583.1580045228; AMP_TOKEN=%24NOT_FOUND; _ga=GA1.2.25875737.1580045230; _gid=GA1.2.670385486.1580045230; csrftoken=o2gocEPfPFiYC3yjCIEJ31bV0rqafADX; __BWfp=c1580045288082x599da8f71; G_ENABLED_IDPS=google; SPC_EC="YAVjQjaX+/J89lW+oyW/dpTskCB8IM1H4zAuE8xr4g14MpoXF+0W+dsFBpDKwKxogXM8X/ysrH2JUlL1FvN5Q4H3y9zMO7pWOI5yqvVSd1Oe/1znxLn5bA6Ys+Fk2cylwJr6cC+d4jy9eiWZFCfot3b3Lg6zN81srYIZx8VHe2s="; SPC_U=50301774; CTOKEN=8fvOaEBBEeq%2FETQea1w0tg%3D%3D; SPC_T_IV="swdTCsjhkoxvigz2+VZEEQ=="; SPC_T_ID="om3c9JnoIL5oc8EkPA+tgkz5hIULALB9CcmIXAouKcLRXAzG2/dd4DERQfdIItfFBk4zy3UYRknbmQkBvxcPAqdv++ZdMNjnFt///QEc3xc="',
    "x-csrftoken": "o2gocEPfPFiYC3yjCIEJ31bV0rqafADX",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}


# res = requests.get(
#     "https://shopee.tw/api/v2/search_items/?by=relevancy&keyword=google%20pixel&limit=50&newest=0&order=desc&page_type=search&version=2",
#     headers=headers)

res = requests.get(
    "https://shopee.tw/api/v2/search_items/?by=relevancy&keyword=google%20pixel&limit=50&newest=0&order=desc&page_type=search&version=2",
    headers=headers)


# res_text = json.loads(res.text)
# pretty_res = json.dumps(res_text, indent=4)
# print(pretty_res)

json_file = res.json()

# all items found by keyword
total_item = json_file.get("items")

for items in total_item:
    item_name = items.get("name")
    max_price = items.get("price_max")
    min_price = items.get("price")
    print(item_name, max_price, min_price)
