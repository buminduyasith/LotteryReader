from bs4 import BeautifulSoup
import requests
from Lottery import Lottery
import time
nlbLotteryTypes = ['mega-60', 'govisetha', 'mahajana-sampatha', 'dhana-nidhanaya', 'handahana', 'lucky-7', 'mega-power', 'jathika-sampatha']

# Set the lottery name and draw number as variables
""" lottery_type = "mahajana-sampatha"
draw_number = "5280" """
# Creating an array (list) of Lottery objects
lottery_list = []

# Adding instances of Lottery to the list
lottery_list.append(Lottery("mahajana-sampatha", 5300))
lottery_list.append(Lottery("mahajana-sampatha", 5301))
lottery_list.append(Lottery("govisetha", 3575))
lottery_list.append(Lottery("mega-power", 1653))
lottery_list.append(Lottery("jathika-sampatha", 1600))
lottery_list.append(Lottery("dhana-nidhanaya", 1363))
lottery_list.append(Lottery("lucky-7", 159))
lottery_list.append(Lottery("handahana", 642))

def GetLotteryWinningResult(lotteryType, drawNumber):
    
    #Todo: show date and draw number

    nlbUrl = f"https://www.nlb.lk/English/results/{lotteryType}/{drawNumber}"
    
    page = requests.get(nlbUrl)

    soup = BeautifulSoup(page.text, features="lxml")

    numbers_list = soup.find_all('ol', class_='B')[0]

    letter = ""
    
    numbers = []
    
    time.sleep(2)
    
    if lotteryType == "jathika-sampatha":
        letter = soup.find('li', class_='Zodiac').text
        numbers = [li.text for li in numbers_list.find_all('li', class_='Number-1')]
        print("Result:", f"{letter} - {'  '.join(numbers)}")
        
    elif lotteryType == "govisetha" or lotteryType == "mega-power":
        letter = soup.find('li', class_='Letter').text
        numbers = [li.text for li in numbers_list.find_all('li', class_='Number-2')]
        print("Result:", f"{letter} - {'  '.join(numbers)}")
        numbers_list = soup.find_all('ol', class_='B')[1]
        numbers = [li.text for li in numbers_list.find_all('li', class_='Number-1')]
        print("LAKSHAPATHI:", f"{'  '.join(numbers)}")
        
    elif lotteryType == "dhana-nidhanaya":
        letter = soup.find('li', class_='Letter').text
        numbers = [li.text for li in numbers_list.find_all('li', class_='Number-2')]
        print("Result:", f"{letter} - {'  '.join(numbers)}")
        numbers_list = soup.find_all('ol', class_='B')[1]
        numbers = [li.text for li in numbers_list.find_all('li', class_='Number-2')]
        print("LAKSHAPATHI:", f"{'  '.join(numbers)}")
        
    elif lotteryType == "handahana":
        letter = soup.find('li', class_='Zodiac').text
        numbers = [li.text for li in numbers_list.find_all('li', class_='Number-2')]
        print("Result:", f"{letter} - {'  '.join(numbers)}")
        numbers_list = soup.find_all('ol', class_='B')[1]
        numbers = [li.text for li in numbers_list.find_all('li', class_='Number-2')]
        print("DHANAYOGAYA:", f"{'  '.join(numbers)}")
        numbers_list = soup.find_all('ol', class_='B')[2]
        numbers = [li.text for li in numbers_list.find_all('li', class_='Number-2')]
        print("DAIWAANKAYA:", f"{'  '.join(numbers)}")
        
    else:
        letter = soup.find('li', class_='Letter').text
        numbers = [li.text for li in numbers_list.find_all('li', class_='Number-1')]
        print("Result:", f"{letter} - {'  '.join(numbers)}")


for lottery in lottery_list:
    print(f"Lottery Type: {lottery.type}, Draw Number: {lottery.draw_number}")
    GetLotteryWinningResult(lottery.type, lottery.draw_number)
    print("-------------------------------------------------------------------\n")