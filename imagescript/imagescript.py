#fetch images from reddit and turn it into background


#install virtual env instance in new folder
#1) pip install virtualenv
#create the virtual environment
# 2) virtualenv mypython
#activate the virtual environment
# 3) source mypython/bin/activate
#to deactivate, $deactivate

#now u can install any dependencies in this environment

#####check if python is linked? brew install python ,brew link python,
#brew link --overwrite python, brew info python

#import
import requests
import praw

#.json after link gives all data in JSON format
# reddit follows OPEN-API standard
url = 'https://www.reddit.com/r/wallpapers.json'

#my reddit personal info
##reddit = praw.Reddit(client_id  = '6ljdJ2YALa49jQ',
##                     client_secret  =  '5_7iHahDChksFgdAmlpivYNAs6Q',
##                     username  =  'yashgadodia',
##                     password  =  'sheyaruke',
##                     user_agent  =  'bebuprogrammingv1')

##response = reddit.subreddit('wallpapers').hot(limit = 1)

#requests library just simplifies the http calls for you, requests a url
#and returns a object with a bunch of info to know if the request was successful
#custom header when you request data from the API
#####  can use reddit api also (but how?)
####   WHY USER-AGENT?

response = requests.get(url, headers= {'User-agent': 'bebubotV-0.1'})

##response = requests.get(url)

if not response.ok:
    print("Error", response.status_code)
    exit()
data = response.json()['data']['children']
##print(data)

#parse data for the info we need
#get first post from an array of posts
first_post = data[1]['data']
#print(first_post)
image_url = first_post['url']
#print(image_url)


#check url and set appropriate extension for image file
if '.png' in image_url:
    extension = '.png'
elif '.jpg' in image_url or '.jpeg' in image_url:
    extension = '.jpeg'
else:
    image_url += '.jpeg'
    extension = '.jpeg'
    
#prevent thumbnails with removed images from being downloaded
image = requests.get(image_url, allow_redirects=False)

#try block lets you test a block of code of characters
#except block lets you handle the error
#finally block lets you execute the code, regardless of try-and except blocks
if(image.status_code == 200): #request is completed successfully
    try:
        #??????
        #output the file in correct folder
        output_filehandle = open(first_post['title'] + extension,mode='bx')
        output_filehandle.write(image.content)
    except:
        pass














    
