import requests  
from bs4 import BeautifulSoup 
import os

def get_imdb_id(file_name):
    if 'tt' in file_name:
        return file_name.split('tt')[1][:7]
    return None

def scrape_subtitles(imdb_id, language='eng'):
    url = f'https://www.opensubtitles.org/en/search/sublanguageid-{language}/imdbid-tt{imdb_id}'
    response = requests.get(url)
    if response.status_code != 200:
        return []
    
    soup = BeautifulSoup(response.content, 'html.parser')
    subtitles = []
    for row in soup.find_all('tr', class_='change'):
        title = row.find('a', class_='bnone').text.strip()
        download_link = row.find('a', class_='bnone')['href']
        subtitles.append((title, 'https://www.opensubtitles.org' + download_link))
    
    return subtitles

def download_subtitle(download_url, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    response = requests.get(download_url)
    
    if response.status_code == 200:
        subtitle_file_name = download_url.split('/')[-1] + '.srt'
        with open(os.path.join(output_folder, subtitle_file_name), 'wb') as file:
            file.write(response.content)
        print(f"Downloaded: {subtitle_file_name}")
    else:
        print("Failed to download subtitle.")

def main():
    file_name = input("Enter the movie file name: ")
    imdb_id = get_imdb_id(file_name)
    
    if not imdb_id:
        print("IMDb ID not found in the filename.")
        return
    
    subtitles = scrape_subtitles(imdb_id)
    
    if not subtitles:
        print("No subtitles found.")
        return
    
    print("Available subtitles:")
    for idx, (title, _) in enumerate(subtitles):
        print(f"{idx + 1}. {title}")
    
    choice = int(input("Pick a subtitle to download (number): ")) - 1
    
    if 0 <= choice < len(subtitles):
        _, subtitle_link = subtitles[choice]
        download_subtitle(subtitle_link, './subtitles')
    else:
        print("Invalid choice.")

if __name__ == '__main__':
    main()
