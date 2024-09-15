# Test
#the Python program that grabs links from a list of URLs, extracts video URLs ending with .mp4, photo URLs ending with orig, the text of the tweet, and the date in the Korean time zone:

##Create urls.txt: Make sure you have a file named urls.txt with the list of URLs (e.g., https://twitter.com/somepage, https://x.com/anotherpage).
Python Program: app.py

##Steps to Run the Program:
Create urls.txt: Add your Twitter or X URLs to a file named urls.txt, each URL on a new line.
Install Required Libraries: Ensure you have the requests, beautifulsoup4, and pytz libraries installed:
pip install requests beautifulsoup4 pytz

Run the Program: Execute the Python script.
This program will read the URLs from urls.txt, grab all the links from each page, filter them to find video links ending with .mp4 and photo links ending with orig, and then print the tweet texts and dates in the Korean time zone.
