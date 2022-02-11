import urllib.request
import requests
from typing import List

# replace string
def replace_string(txt, x, y):
    z = txt.replace(x,y)
    print(z)

#using args*, **kwargs

def args_kwargs_1(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)

#copy image from url

def copy_image():
    link = input("Enter Image url:")
    new_file_name = "image1.jpg"
    urllib.request.urlretrieve(link, new_file_name)

def count_all_lines_in_file(file_x):
    num_lines=len(open(file_x).readline())
    return num_lines

#uniquify

def uni_qify1(seq):
    hash_ = {}
    [hash_.__setitem__(x,1) for x in seq]
    h= hash_.keys()
    print(h)
    for x in h:
        print(x, end=" " )# print on the same line with space btween elements
        # to add remove space, remove the space btween " ". to add a sign btw
        # the characters just add the sign between the " "
    print('\n')

def uni_qify2(seq):
    seq = seq.lower()#set to lowercase
    seq = seq.replace(" ", "") # remove spaces
    keys = {}
    for e in seq:
        keys[e] = 1
        j= keys.keys()
    print(j)
    for e in j:
        print (e,end=" ")

def davidodhiambo_web():
    x = requests.get('https://www.davidodhiambo.com')
    print(x.text)

# write data to file
def read_and_write_data():
    file_path = input("Enter File path:")
    with open(file_path, 'r') as r:
        count = 0
        for line in r:
            count +=1
            if count %2==0:
                with open(file_path, 'w') as f:
                    f.write(line.to_string())