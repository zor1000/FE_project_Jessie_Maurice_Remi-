import requests
import urllib.request
from bs4 import BeautifulSoup

headers = {'User-Agent':
'Mozilla/5.0 Chrome/39.0.2171.95 Safari/537.36'}
url = "https://en.wikipedia.org/wiki/Main_Page"
reg = requests.get(url, headers=headers)
text = reg.text



headers = {'User-Agent':
'Mozilla/5.0 Chrome/39.0.2171.95 Safari/537.36'}
url = "https://en.wikipedia.org/wiki/Main_Page"
soup = BeautifulSoup(reg.content, 'html.parser')

# Finding annd printing all <title> tags
for x in soup.find_all("title"):
    print(x.text) # .text to get just the text part of the tag
# Finding and printing specific <div> with id 'articlecount'
for x in soup.find_all("div", {"id": "articlecount"}):
    print (x.text)

# 1) Get data from a simple website!
headers = {'User-Agent':
'Mozilla/5.0 Chrome/39.0.2171.95 Safari/537.36'}

# Step 1: URL to fetch
url = "https://www.thomas-renault.com/side/ex1.html"

# Step 2: Send a GET request to the URL
# Step 3: PArse the HTML content of the page with BeatifulSoup
soup = BeautifulSoup(reg.content, 'html.parser')

# Extracting and printing all text from the webpage
text = soup.get_text(strip = True)
print(text)


# 2) Get specific data from a simple website

headers = {'User-Agent':
'Mozilla/5.0 Chrome/39.0.2171.95 Safari/537.36'}



# Step 1 : get to the URL below
url = "https://www.thomas-renault.com/side/ex2.html"

# Step 2 : get only web links from this webpage
soup = BeautifulSoup(reg.content, 'html.parser')

# 1st method
for link in soup.find_all('a', href=True):
  print(link['href'])

## 2nd Method
# # Finding all <a> tags ti extract href attibutes
# links = soup.find_all('a')
#
# # Interating over each link and printing the URL found in the href attribute
# for link in links:
#     href = link.get('href')
#     if href: # ensuring the href attribute is present
#         print (href)

# Objective : Webscrapping a real website


















# 1. pip install selenium pandas openpyxl

# 2. Set up Selenium with ChromeDriver:
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd

# Path to your ChromeDriver
s = Service('/Applications/Google Chrome.app')

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Running in headless mode
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=s, options=chrome_options)

# Path to your ChromeDriver
driver = webdriver.Chrome(executable_path='/path/to/chromedriver', options=chrome_options)


# 3. Access the website and navigate to the archives:

# Suppose you've navigated to the page or you have the direct URL
driver.get("https://www.wsj.com/news/archive/20220224")
time.sleep(5)  # Wait for the page to load completely

# Find all links within article summaries
article_links = driver.find_elements_by_xpath('//a[contains(@href, "/articles/")]')
links = [link.get_attribute('href') for link in article_links]

# 4. Visit each article and extract required details:

articles_data = []

for link in links:
    driver.get(link)
    time.sleep(3)

    try:
        title = driver.find_element_by_tag_name('h1').text
        content = driver.find_element_by_css_selector('div.article-content').text
        articles_data.append({'Date': '2022-02-24', 'Title': title, 'Content': content})
    except Exception as e:
        print(f"Failed to process {link}: {str(e)}")


# Create a DataFrame and save as an Excel file:

df = pd.DataFrame(articles_data)
df.to_excel('wsj_articles_20220224.xlsx', index=False)
print("Data saved to Excel.")

# Close the browser:

driver.quit()
