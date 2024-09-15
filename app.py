#Write a Python program to grab links from a list of URLs and extract video URLs ending with ‘.mp4’, photo URLs ending with ‘orig’, the text of the tweet, and the date in Korean time zone. The list of URLs should be read from ‘urls.txt’ file.

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pytz

def grab_links_and_info(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all anchor tags with href attribute
    links = [a['href'] for a in soup.find_all('a', href=True)]
    
    # Find the tweet text
    tweet_text = soup.find('div', {'data-testid': 'tweetText'}).get_text(strip=True)
    
    # Find the tweet date and convert it to Korean time zone
    tweet_date_str = soup.find('time')['datetime']
    tweet_date = datetime.fromisoformat(tweet_date_str[:-1])
    korean_tz = pytz.timezone('Asia/Seoul')
    tweet_date_korean = tweet_date.astimezone(korean_tz)
    
    return links, tweet_text, tweet_date_korean

def filter_links(links):
    video_links = [link for link in links if link.endswith('.mp4')]
    photo_links = [link for link in links if link.endswith('orig')]
    
    return video_links, photo_links

# Read URLs from 'urls.txt' file
with open('urls.txt', 'r') as file:
    urls = file.read().splitlines()

all_video_links = []
all_photo_links = []
all_tweet_texts = []
all_tweet_dates = []

# Process each URL
for url in urls:
    links, tweet_text, tweet_date_korean = grab_links_and_info(url)
    video_links, photo_links = filter_links(links)
    
    all_video_links.extend(video_links)
    all_photo_links.extend(photo_links)
    all_tweet_texts.append(tweet_text)
    all_tweet_dates.append(tweet_date_korean)

# Print the extracted video and photo links, tweet texts, and dates
print("Video Links:")
for link in all_video_links:
    print(link)

print("\nPhoto Links:")
for link in all_photo_links:
    print(link)

print("\nTweet Texts:")
for text in all_tweet_texts:
    print(text)

print("\nTweet Dates (Korean Time Zone):")
for date in all_tweet_dates:
    print(date.strftime('%Y-%m-%d %H:%M:%S %Z%z'))
