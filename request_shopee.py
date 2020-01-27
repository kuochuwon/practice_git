import requests
import json
import const


headers = {
    "referer": "https://shopee.tw/search?keyword=google%20pixel",
    "Cookie": const.Cookie,
    "User-Agent": const.User_Agent,
    'if-none-match-': '55b03-84f97a9961b9a98a415af2b114498793'
}

res = requests.get(
    "https://shopee.tw/api/v2/search_items/?by=relevancy&keyword=google%20pixel&limit=50&newest=0&order=desc&page_type=search",
    headers=headers,
    allow_redirects=False)


json_file = res.json()

# all items found by keyword
total_item = json_file.get("items")

for items in total_item:
    item_name = items.get("name")
    max_price = items.get("price_max")
    min_price = items.get("price")
    print(item_name, max_price, min_price)

if __name__ == if __name__ == "__main__":
