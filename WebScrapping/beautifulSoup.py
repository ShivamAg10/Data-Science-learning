from bs4 import BeautifulSoup

with open("scrapped_data/data1.html", "r") as f:
    html_content = f.read()
# print(html_content)
soup = BeautifulSoup(html_content, "lxml")
# print(soup.find_all("div"))
# print(soup.find("h1"))
all_h3 = soup.find_all("h3")
for h3s in all_h3:
    # print(h3s.get_text(strip=True))
    ctry_infor = h3s.find_next("div").select("span.country-population")[0].get_text(strip = True)
    # print(ctry_infor)