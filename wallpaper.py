from  datetime import datetime as dt
import os
import urllib.request 

from bs4 import BeautifulSoup
import requests


def change_wallpaper():
    parent_dir = os.getcwd()
    directory = 'wallpaper'
    child_dir = os.path.join(parent_dir, directory)
    if not os.path.exists(child_dir):
        os.mkdir(child_dir)


    url= "https://bing.wallpaper.pics"
    page = requests.get(url)
    if page.status_code == 200:
        soup = BeautifulSoup(page.text, 'html.parser')
        link = soup.find('a', class_="cursor_zoom") #get anchor tag element
        img = link.find('img') # get the img tag element within anchor tag
        img_link = img.get('src') # get the value of src attribute within the img tag

        #******************Download image************************
        filename = dt.now().strftime('%d-%m-%y') + '.jpg'
        filepath = os.path.join(child_dir, filename)
        urllib.request.urlretrieve(img_link, filepath)
        print(filename)
        print(filepath)
        cmd = 'gsettings set org.gnome.desktop.background picture-uri "file://'
        filepath = filepath+'"'
        COMMAND = cmd + filepath
        os.system(COMMAND)
        

change_wallpaper()
