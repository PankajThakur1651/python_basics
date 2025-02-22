import urllib.request
import urllib.error
import sys

contents = ''
try:
    with urllib.request.urlopen("https://google.com/") as url:
        contents = url.read()
except urllib.error.HTTPError as e:
    print(f"Error occurred: {e}")
    sys.exit()
except urllib.error.URLError as e:
    print(f"Error occurred: {e}")
    sys.exit()

# Using 'with' to handle file writing properly
with open('python.html', 'wb') as f:
    f.write(contents)
