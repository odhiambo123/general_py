import requests
from bs4 import BeautifulSoup
import sys

def text(url):
    # the target page.
    #open with GET Method
    resp = requests.get(url)

    # check if everything went OK
    if resp.status_code == 200:
        print("success opening")
        print("this is the output: \n")

        # using the builtin python HTML parser in python
        soup = BeautifulSoup(resp.text, 'html.parser')

        l = soup.find("ul",{"class":"searchNews"})

        for i in l.find("a"):
            print(i.text)
        else:
            print("Error")
if __name__== '__main__':

    text('https://www.hindustantimes.com/top-news')




