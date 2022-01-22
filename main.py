import requests
from bs4 import BeautifulSoup

url = 'https://www.reddit.com/r/memes/comments/s9asbs/boys_with_editing_skills/'


# Download videos from reddit using redditsave.com (Non-Existing Api :p)
def redditDownload(redditUrl):
    redditsave_api = 'https://redditsave.com/info?url=' + redditUrl
    reqs = requests.get(redditsave_api)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    title = soup.find(class_="text-center text-truncate").text.split()
    for link in soup.find_all('a'):
        if "https://sd.redditsave.com/download.php" in link.get('href', []):
            return (" ".join(title)), (link.get('href'))


# Function that handles downloading, renaming and saving the files in local storage
def downloadFile(file_name, file_url):
    file_object = requests.get(file_url)
    with open((file_name + ".mp4"), 'wb') as local_file:
        local_file.write(file_object.content)


downloadFile(redditDownload(url)[0], redditDownload(url)[1])
