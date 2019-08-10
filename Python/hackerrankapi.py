import sys
import os
import urllib.request
import json
import re

def getTopicCount(topic):

    # hackerrank required me to access the url below and they would pass in a parameter,
    # which I would format into my url in order to pull up the correct page that they wanted
    # me to parse. I use the .format() function on the string which allows me to pass the 'topic'
    # parameter into the string where you see the '{}' at the end of the string. This is similar
    # to the %s string format specifier in C Programming.

    search_url = 'https://en.wikipedia.org/w/api.php?action=parse&section=0&prop=text&format=json&page={}'.format(topic)

    # urllib is python's library for sending HTTP Requests. This question required me to send
    # a GET request in order to access the page. The .urlopen() function performs a GET on the
    # url provided. The .read() function allows the HTTPResponse to be read as bytes so that we can
    # pass it to json.loads to be converted into a dictionary.
    r = urllib.request.urlopen(search_url).read()

    # json.loads() function converts the JSON string into a python dictionary so that I can search
    # for specific values.
    data = json.loads(r)

    # uncomment this print statement if you want to see what JSON data looks like. If you do this,
    # I suggest you copy and past the data into this website:
    # https://www.freeformatter.com/json-formatter.html
    # the JSON data will be much easier to read once it's formatted correctly.
    #print(data)

    # The actual text that we need is embedded in the JSON text. This is how we access the text.
    text = data['parse']['text']['*']


    #print(re.findall(r'{}'.format(topic), text, re.IGNORECASE)) # Finds ALL occurrances of 'topic'
    #count = len(re.findall(r'{}'.format(topic), text, re.IGNORECASE))

    #finds EXACT match of 'topic' parameter
    count = len(re.findall(r'{}'.format(topic), text))


    # code below is how I would solve this problem by using a for-loop rather than using
    # regular expressions.

    # count = 0
    # for i in range(len(text)):
    #     if text[i:i+(len(topic))].lower() == topic:
    #         count += 1
    print(count)
    #print(text)

getTopicCount('pizza')
