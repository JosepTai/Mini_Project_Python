# import required libraries
import re
import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

# create an object to ToastNotifier class
n = ToastNotifier()


# define a function
def getdata(url):
    r = requests.get(url)
    return r.text


# Get data in html tag
def fill_data(data):
    data_find = str(data)
    regex = r"\>(.+)?\<"
    result = re.findall(regex, data_find, re.DOTALL)
    return result[0]


htmldata = getdata("https://weather.com/en-IN/weather/today")

soup = BeautifulSoup(htmldata, 'html.parser')

location = fill_data(soup.find_all("h1", class_="CurrentConditions--location--kyTeL"))

current_temp = fill_data(soup.find_all("span", class_="CurrentConditions--tempValue--3a50n"))

result = str(f"Location: {location}\nTemp: {current_temp}")
n.show_toast("Live Weather update",
             result, duration=5)
