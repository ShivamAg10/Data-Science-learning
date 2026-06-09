import requests

url = "https://www.scrapethissite.com/pages/simple/"
try:
    response = requests.get(url)
    # if response.status_code == 200:
    # #     # print(response.text)
    # #     # print(response.content)
    # #     print(response.headers)
    # #     end = time.time()
    # #     print(end-start)
    # # else:
    # #     print("Failed")

    # # Scrapping data into files
    # with open("scrapped_data/data3.html", "w") as f:
    #     f.write(response.headers)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Error:", e)