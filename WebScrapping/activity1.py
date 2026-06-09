import requests
from bs4 import BeautifulSoup

## Fetched all the pages
page_count = 1
final_quotes = []
while True:
    url = f"https://quotes.toscrape.com/page/{page_count}/"
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, "lxml")
    
    div = soup.select("div.quote")
    for divQuotes in div:
        tags = divQuotes.select("a")
        for tagsText in tags:
            if tagsText.text == "life":
                quote = divQuotes.select("span.text")[0].text
                final_quotes.append(quote)
    if not div:
        print("no valid pages anymore...")
        break
    
    # with open(f"scrapped_data/quotes{page_count}.html", "w", encoding="utf-8") as f:
    #     f.write(response.text)
    #     print(f"Succesfully downloaded data from page{page_count}")
    print(f"Page {page_count} stolen")
    page_count += 1

print()
print()
print("There are total",len(final_quotes), "quotes with life Tags")