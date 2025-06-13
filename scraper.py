import requests
from bs4 import BeautifulSoup

def get_stock_data():
    url = "https://www.sgbv.dz/ar/?page=detail_creance"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    data = []
    table = soup.find("table")
    if not table:
        return []

    rows = table.find_all("tr")[1:]  # نتجاهل صف الرأس

    for row in rows:
        cols = row.find_all("td")
        if len(cols) >= 5:  # نفترض أن السعر في العمود الخامس (تأكد من الصفحة)
            company = cols[0].text.strip()
            price = cols[4].text.strip()  # عمود السعر
            data.append({
                "company": company,
                "price": price
            })

    return data
