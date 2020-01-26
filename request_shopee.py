import requests
import const

# headers = {
#     "Referer": "https://shopee.tw/search?keyword=google%20pixel",
#     "Cookie": 'SPC_F=2c95sYFkzfWrz1RZ0pMLLlug1rPm9S0o; REC_T_ID=fc9cb468-d880-11e9-b087-f8f21e1a7612; _ga=GA1.2.741601534.1568638412; __BWfp=c1568638413405xf26e6cced; cto_lwid=b0ccf836-615e-4837-8c84-a7d7c1705a99; SPC_IA=-1; G_ENABLED_IDPS=google; _med=refer; _gcl_au=1.1.122690841.1576505462; _fbp=fb.1.1578399168664.1918442970; csrftoken=BZqH8wT7HRzYLozH9s4XC3fdPORCycaX; CTOKEN=XKUwhDh3Eeq4Y8y7%2Fl1Ysg%3D%3D; SPC_EC=-; SPC_U=-; welcomePkgShown=true; SPC_SI=v7ekrmntpmcy6h182oanzno5s0jv56xg; _gid=GA1.2.1080604625.1579443756; AMP_TOKEN=%24NOT_FOUND; SPC_T_IV="S0+KVDC4g9D9bUnaiGW91w=="; SPC_T_ID="pOZ10jzZj3tI7Su1FwDzOcACMqsiQMDpHjlyR452/wvceCNJF9/gIrGsgjRTG0tZ6plYLTmQqkmLZJA6teOCErd3TY8SjZ9yuNZ7T7uvpFo="',
#     "x-csrftoken": "BZqH8wT7HRzYLozH9s4XC3fdPORCycaX",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
# }


headers = {
    "Referer": "https://shopee.tw/search?keyword=google%20pixel",
    "Cookie": const.Cookie,
    "x-csrftoken": const.x_csrftoken,
    "User-Agent": const.User_Agent
}

res = requests.get(
    "https://shopee.tw/api/v2/search_items/?by=relevancy&keyword=google%20pixel&limit=50&newest=0&order=desc&page_type=search&version=2",
    headers=headers)

res_without_header = requests.get(
    "https://shopee.tw/api/v2/search_items/?by=relevancy&keyword=google%20pixel&limit=50&newest=0&order=desc&page_type=search&version=2"
)


print(res.text)
