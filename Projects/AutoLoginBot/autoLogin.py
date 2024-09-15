from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def startBot(username, password, url):
    path = r"C:\path\to\your\chromedriver.exe"
    
    # Initialize the Chrome WebDriver with the correct service path
    service = Service(executable_path=path)
    driver = webdriver.Chrome(service=service)
    
    # Opening the website in Chrome
    driver.get(url)
    
    # Find the username field and input the username
    driver.find_element(By.NAME, "email").send_keys(username)
    
    # Find the password field and input the password
    driver.find_element(By.NAME, "pass").send_keys(password)
    
    # Find and click on the login button
    driver.find_element(By.NAME, "login").click()

    # Wait for user input to close the browser
    input("Press Enter to close the browser...")

# Driver Code
username = "your_email@example.com"  # Replace with your email or username
password = "your_password"  # Replace with your password
url = "https://www.facebook.com/"  # URL of the login page

# Call the function
startBot(username, password, url)
