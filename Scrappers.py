import pyperclip, requests, os
from bs4 import BeautifulSoup


print('''WARNING!!!!
This script requires INTERNET for it to work
it will crash if you dont have internet\n''')
print("Make sure you've gat the spellings correct, otherwise it won't work \n")
#get the artist and song
artist_name = input("Enter the artist name: ")
song = input('Enter the song title: ')
lyr = artist_name + ' ' + song
print('\t Searching for lyrics... Please be patient')
lyric = '-'.join(lyr.split(' '))
page = requests.get('https://genius.com/'+ lyric + '-lyrics')
#check if conection is granted
page.raise_for_status()
#parse the site
soup = BeautifulSoup(page.content, 'html.parser')
#get the lyrics
lyrics = soup.find("div", {"class":"song_body-lyrics"}).get_text()
pyperclip.copy(lyrics)
song_lyrics = pyperclip.paste()
songName = lyr + ' lyrics.txt'
song_file = open(songName, 'w')
song_file.write(song_lyrics)
song_file.close()
print('''Done!!!
 Lyrics Downloaded''')
print("It's in ", os.path.abspath(songName))
ans = input('''
Do wanna open it (Yes/No) ''')
if ans.upper() == 'YES' or ans.upper() == 'Y':
    print('Opening lyrics')
    os.startfile(songName)
elif ans.upper() == 'NO'or ans.upper() == 'N':
    print('''You've decided not to OPEN the lyrics.''')
else:
    print('''You've decided not to OPEN the lyrics.''')
