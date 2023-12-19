from bs4 import BeautifulSoup
import requests

['mega-60', 'govisetha', 'mahajana-sampatha', 'dhana-nidhanaya', 'handahana', 'lucky-7', 'mega-power', 'jathika-sampatha']
# Set the lottery name and draw number as variables
lottery_type = "mahajana-sampatha"
draw_number = "5150"

nlbUrl = f"https://www.nlb.lk/English/results/{lottery_type}/{draw_number}"

page = requests.get(nlbUrl)

soup = BeautifulSoup(page.text, features="lxml")

numbers_list = soup.find_all('ol', class_='B')[0]

letter = ""

if lottery_type == "jathika-sampatha":
    letter = soup.find('li', class_='Zodiac').text
else:
    letter = soup.find('li', class_='Letter').text


numbers = [li.text for li in numbers_list.find_all('li', class_='Number-1')]

print("Result:", f"{letter} - {'  '.join(numbers)}")
