import requests
import json
import const


headers = {
    "Referer": "https://shopee.tw/search?keyword=google%20pixel",
    "Cookie": const.Cookie,
    "x-csrftoken": const.x_csrftoken,
    "User-Agent": const.User_Agent
}

# res = requests.get(
#     "https://shopee.tw/api/v2/search_items/?by=relevancy&keyword=google%20pixel&limit=50&newest=0&order=desc&page_type=search&version=2",
#     headers=headers)

res = requests.get(
    "https://shopee.tw/api/v2/search_items/?by=relevancy&keyword=google%20pixel&limit=50&newest=0&order=desc&page_type=search&version=2",
    headers=headers)


res_text = json.loads(res.text)
pretty_res = json.dumps(res_text, indent=4)
print(pretty_res)

# json_file = res.json()

# all items found by keyword
# total_item = json_file.get("items")

# for items in total_item:
#     item_name = items.get("name")
#     max_price = items.get("price_max")
#     min_price = items.get("price")
#     print(item_name, max_price, min_price)
