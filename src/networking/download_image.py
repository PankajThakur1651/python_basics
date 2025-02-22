import urllib.request

url = "https://example.com/image.jpg"
filename = "downloaded_image.jpg"

try:
    urllib.request.urlretrieve(url, filename)
    print(f"Image downloaded successfully as {filename}")
except Exception as e:
    print(f"Error downloading image: {e}")
