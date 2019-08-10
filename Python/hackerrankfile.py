# re in python is the regular expression library. This helps me find strings that
# are formatted in a very specific way.
import re

txt = """unicomp6.unicomp.net - - [01/Jul/1995:00:00:06 -0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985
burger.letters.com - - [01/Jul/1995:00:00:11 -0400] "GET /shuttle/countdown/liftoff.html HTTP/1.0" 304 0
burger.letters.com - - [01/Jul/1995:00:00:12 -0400] "GET /images/NASA-logosmall.gif HTTP/1.0" 304 0
burger.letters.com - - [01/Jul/1995:00:00:12 -0400] "GET /shuttle/countdown/video/livevideo.gif HTTP/1.0" 200 0
d104.aa.net - - [01/Jul/1995:00:00:13 -0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985
unicomp6.unicomp.net - - [01/Jul/1995:00:00:14 -0400] "GET /shuttle/countdown/count.gif HTTP/1.0" 200 40310
unicomp6.unicomp.net - - [01/Jul/1995:00:00:14 -0400] "GET /images/NASA-logosmall.gif HTTP/1.0" 200 786
unicomp6.unicomp.net - - [01/Jul/1995:00:00:14 -0400] "GET /images/KSC-logosmall.gif HTTP/1.0" 200 1204
d104.aa.net - - [01/Jul/1995:00:00:15 -0400] "GET /shuttle/countdown/count.gif HTTP/1.0" 200 40310
d104.aa.net - - [01/Jul/1995:00:00:15 -0400] "GET /images/NASA-logosmall.gif HTTP/1.0" 200 786"""


dict = {}
# use the regular expression library to find all parts of txt where it starts with '[' and
# ends with ']'. We don't care what's in between because we assume dates will be between the [].
# this regular expression parses the txt and will return ALL matches to this regular expression string
data_list = re.findall(r'\[(.*?)\]', txt)


# hackerrank is looking for the results in a format of [DD/MMM/YYYY:HH:MM:SS], but the txt has
# the data formatted like [DD/MMM/YYYY:HH:MM:SS -0400], so we use the .split() function on each
# string which will split each word in the string into an array. The string is split based on
# spaces in the string. So when we save a date, the .split() function will store
# DD/MMM/YYYY:HH:MM:SS into array[0] and -0400 into array[1]. We want element [0]. Next, we search
# to see if this data is already in our map/dictionary called dict. If this element is already a key
# in dict, we increase the value by one then continue to the next iteration. If this element is not
# a key in dict, we set the value to 1. Map/Dictionaries are Key-Value pairs. The key is our date
# string, and the value is the number of times it is present in the string.
for data in data_list:
    data = data.split()[0]
    if data in dict:
        dict[data] += 1
        continue
    dict[data] = 1

# the hackerrank required me to write the results to a new file. So i created a file called
# 'req_file' with write permissions.
req_file = open('reqfile', 'w')

# this is a list comprehension which can be interpreted as "create a new list called dup_dates
# and store every element x in our dict if dict[x] is greater than 1. In other words, store
# every element in our list if the element shows up more than once in the string.
dup_dates = [x for x in dict if dict[x] > 1]
for date in dup_dates:
    #print(date) #for debugging purposes
    req_file.write(date)
    req_file.write('\n') #hackerrank required all entries to be on their own line
