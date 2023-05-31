import csv
import requests
from bs4 import BeautifulSoup


url = "https://dressup.ge/ka/"
response = requests.get(url)


if response.status_code == 200:

    soup = BeautifulSoup(response.content, "html.parser")


    title = soup.title.text


    links = [link.get("href") for link in soup.find_all("a")]


    filename = "data.csv"
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["title", "link"])
        writer.writerow([title, ""])
        for link in links:
            writer.writerow(["", link])
    print("information saved successfully", filename)

else:
    print("Error while sending response", response.status_code)