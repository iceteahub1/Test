# Test
Got it! Here's an updated version of the Python program that reads URLs from a file named `urls.txt` and extracts video URLs ending with `.mp4` and photo URLs ending with `orig`:

1. **Create `urls.txt`**: Make sure you have a file named `urls.txt` with the list of URLs (e.g., `https://twitter.com/somepage`, `https://x.com/anotherpage`).

2. **Python Program**: "app.py"
```

### Steps to Run the Program:
1. **Create `urls.txt`**: Add your Twitter or X URLs to a file named `urls.txt`, each URL on a new line.
2. **Install Required Libraries**: Ensure you have the `requests` and `beautifulsoup4` libraries installed:
   ```sh
   pip install requests beautifulsoup4
   ```
3. **Run the Program**: Execute the Python script.

This program will read the URLs from `urls.txt`, grab all the links from each page, filter them to find video links ending with `.mp4` and photo links ending with `orig`, and then print them out.
