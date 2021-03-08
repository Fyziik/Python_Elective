# 1. Create an application that asks for an url.
# 2. Then Download that html page, and its images, icons etc. and change it so it will work locally on your computer. Locally means that you should be able to cut your internet connection and still have a functionig html page.
# 3. When done push all files to you github account. (you are allowed to manualy create an online repo and feed the clone url to your program. but the rest should be done through python).
# You will have to use the requests module, the OS module and the subprocesses module for this taks.


import requests
import os

# fetch the html from a url
req = requests.get('https://clbokea.github.io/exam/assignment_2.html')
text = req.text

img_url_list = [] 

text_list = text.split('img')

def locate_image(e):
    i = e.find('"')

    # cut after  'src="' to end of the img_url  
    img_url = e.split('"')
    img_url = img_url[1]
    img_url_list.append(img_url)


for e in text_list:
    if 'src' in e:
        locate_image(e)

# print(img_url_list)

# Create a src directory for the images
os.mkdir('src')
os.chdir('src')

for i in img_url_list:
    # get the image
    req = requests.get(f'https://clbokea.github.io/exam/{i}', stream=True)

    # write image to file
    with open(i[4:], 'wb') as f:
        for chunk in req:
            f.write(chunk)

os.chdir('..')

with open('index.html', 'w') as f:
    f.write(text)