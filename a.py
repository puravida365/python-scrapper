from lxml import html
import requests
import sys

def scrape(argv):
    page = requests.get(argv)
    tree = html.fromstring(page.content)
    # container = tree.xpath('//div[@class="container"]/text()')
    container = tree.xpath('//h1/text()')
    print 'Payload: ', container

if __name__ == "__main__":
    try: 
        arg1 = sys.argv[1]
    except IndexError:
        print "Usage: myprogram.py <arg1>"
        sys.exit(1)

    # start the program
    scrape(arg1)

'''
$python a.py http://josuemora.com/index.php
Payload:  ['Web and App Developer']

'''