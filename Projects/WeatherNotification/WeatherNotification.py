# Import required libraries 
import requests 
from bs4 import BeautifulSoup 
from win10toast import ToastNotifier 

# Create an object for the ToastNotifier class 
n = ToastNotifier() 

# Define a function to fetch webpage content
def getdata(url): 
    r = requests.get(url) 
    return r.text 

# URL for weather data
htmldata = getdata("https://weather.com/en-IN/weather/today/l/25.59,85.14?par=google&temp=c/") 

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(htmldata, 'html.parser') 

# Extract current temperature using the data-testid attribute
current_temp_element = soup.find("span", {"data-testid": "TemperatureValue"}) 
current_temp = current_temp_element.text if current_temp_element else "N/A"

# Extract air quality index using the data-testid attribute
air_quality_element = soup.find("text", {"data-testid": "DonutChartValue"}) 
air_quality = air_quality_element.text if air_quality_element else "N/A"

# Format the result string
result = f"Current temperature: {current_temp} in Talcher, Odisha\nAir Quality Index: {air_quality}"

# Display the result using a desktop notification
n.show_toast("Live Weather Update", result, duration=10)
