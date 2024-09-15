#Write a Python program to grab links from a list of URLs and extract video URLs ending with ‘.mp4’ and photo URLs ending with ‘orig’. The list of URLs should be read from ‘urls.txt’ file.

import requests
from bs4 import BeautifulSoup

def grab_links(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all anchor tags with href attribute
    links = [a['href'] for a in soup.find_all('a', href=True)]
    
    return links

def filter_links(links):
    video_links = [link for link in links if link.endswith('.mp4')]
    photo_links = [link for link in links if link.endswith('orig')]
    
    return video_links, photo_links

# Read URLs from 'urls.txt' file
with open('urls.txt', 'r') as file:
    urls = file.read().splitlines()

all_video_links = []
all_photo_links = []

# Process each URL
for url in urls:
    links = grab_links(url)
    video_links, photo_links = filter_links(links)
    
    all_video_links.extend(video_links)
    all_photo_links.extend(photo_links)

# Print the extracted video and photo links
print("Video Links:")
for link in all_video_links:
    print(link)

print("\nPhoto Links:")
for link in all_photo_links:
    print(link)
