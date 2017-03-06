import urllib2
from bs4 import BeautifulSoup

webpage="https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

#query the website..
data = urllib2.urlopen(webpage)
'''
print data
for i in data:
	print i
'''

get_parsed_data  = BeautifulSoup(data)
#print get_parsed_data.prettify().encode('utf8')
print get_parsed_data.title.string
get_href= get_parsed_data.find_all("a")
for i in get_href:
	print i.get("href")

