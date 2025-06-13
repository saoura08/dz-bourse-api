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

    rows = table.find_all("tr")[1:]  # نتجاهل العنوان

    for row in rows:
        cols = row.find_all("td")
        if len(cols) >= 12:  # عدد الأعمدة الكلي
            data.append({
                "company": cols[0].text.strip(),
                "symbol": cols[1].text.strip(),
                "price_open": cols[2].text.strip(),
                "price_close": cols[3].text.strip(),
                "change_percent": cols[4].text.strip(),
                "monthly_change": cols[5].text.strip(),
                "yearly_change": cols[6].text.strip(),
                "pe_ratio": cols[7].text.strip(),
                "net_yield": cols[8].text.strip(),
                "volume": cols[9].text.strip(),
                "turnover": cols[10].text.strip()
            })

    return data
