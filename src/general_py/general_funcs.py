import heapq
import json
import csv
import statistics
from statistics import mode
import functools
import linecache
import urllib.request
import requests
from typing import List
from typing import Dict
import sys
from functools import lru_cache
from functools import cache
from typing import Generator
from secrets import token_bytes
from typing import Tuple


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

#memoization using python dictionary
# python does automatic memoization using lru_cache from function tools

@lru_cache(maxsize=None)
def fib3(n: int) -> int:
    if n < 2:
       return n
    return fib3(n-2) + fib3(n-1) #recursive case

def fib4(n: int)->int:
    if n == 0: return n # special case
    last: int =0 # initially set to fib(0)
    next: int =1 # initially set fib(1)

    for _ in range (1, n):
        last, next = next , last + next
    return  next

#printing the fibonacci numberss

# we use the yield
# import generator
#from typing import Generator
def fib5(n: int)->Generator[int, None, None]:
    yield 0 # special case
    if n > 0: yield 1 #special case
    last = 0
    next: int = 1 # initially set to fib(1)
    for _ in range(1,n):
        last, next = next, last + next
        yield next
@cache
def factorial(n):
    return n * factorial(n-1) if n else 1


#unbreakable encryption
# from secrets import token_bytes
# from typing import Tuple.

def random_key(length: int) -> int:
    #generate length random bytes
    tb: bytes = token_bytes(length)
    #convert those bytes into a bit string and return it
    # .
    return int.from_bytes(tb, "big")
#combining the dummy data with the original data?
# This is where the XOR come in
#XOR returns true only and only if one of the operands is true the
# XOR operand in python is ^ and returns 0 or 1
# A^B = C
# C^B = A
# C^A = B
# XOR an int representing the byte in the original str with a
# randomly generated int of the same bit length.
def encrypt(original: str)->Tuple[int, int]:
    original_bytes: bytes = original.encode()
    dummy: int = random_key(len(original_bytes))
    original_key: int = int.from_bytes(original_bytes, "big")
    encrypted: int = original_key ^ dummy #XOR
    return dummy, encrypted
# to decrypt, recombine the key pair that was generated with the encrypt()
# by doing the XOR operation between each and every bit in the two keys
# then the ultimate output converted back to str
# .
def decrypt(key1: int, key2: int) -> str:
    decrypted: int = key1 ^ key2 # XOR
    temp: bytes = decrypted.to_bytes((decrypted.bit_length()+ 7) // 8, "big")
    #We add 7 b4 dividing by 8 to ensure 'rounding up' to avoid an off-by-one error

    print(temp.decode())
    return temp.decode()

def calculate_pi(n_terms) -> float:
    numerator= 4.0
    denominator= 1.0
    operation= 1.0
    pi = 0.0
    for _ in range(n_terms):
        pi += operation * (numerator / denominator)
        denominator +=2.0
        operation *= -1.0
    return pi
###counting vowels

@lru_cache
def count_vowels(sentence):
    return sum(sentence.count(vowel) for vowel in 'AEIOUaeiou')

#BinarySearch

def binary_contains(searchGroup, searchItem):
    low = 0
    high = len(searchGroup)-1


    while low <= high:
        mid = (low + high) // 2
        if searchGroup[mid] < searchItem:
            low = mid + 1
        elif searchGroup[mid] > searchItem:
            high = mid - 1
        else:
            return True
    return False

def kth_largest(k, stream):
    try:
        List = list(map(int, stream.split(',')))
        print(List)
        List.sort()
        print(List)

        if k > len(List) or k<=0:
            print('Value of k is out of bounds for this stream', sep="")
        else:
            print(k, 'th largest number of the stream is : ' , List[-k], sep="")
    except:
        print('please use the correct format comma separated')

def merge_lists(*args):

   new_list = sorted(list(heapq.merge(*args)))
   print(new_list)

def create_list(*args,**kwargs):
    my_list = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
    print('\n The original list is ', my_list)
    a = mode(my_list)
    b = my_list.sort()
    c = my_list.count('apple')

    print('\n Use mode to print the most reccuring object in the list e.g mode(my_list) ' , 'returns  \'',a,'\'')
    print('\n Use sort() to sort the list e.g: my_list.sort() will sort the list. \n  ', my_list, '\n '
          '\n Count the number of a particular object in the list and print out the result using count() like below: ')
    print('\n my_list.count(\'apple\') returns ',  c )

    print('\n my_list.append(\'grape\') adds grape to the end of the list ', my_list.append('grape',), my_list.extend('blueberries''pineaple''greenberries' '' ))
    print('\n We can now check is the list contains the item by my_list.__contains__(\'grape\'), it returns True or False, in this case it\'s ',my_list.__contains__('grape') )

    print('Other functions include:  my_list.index(), my_list.copy(), my_list.pop(), my_list.remove(), my_list.clear(), my_list.extend(), my_list.reverse(), my_list and more')
def roman_to_int(s: str) -> int:
    # Dictionary of roman numerals
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    # Length of the given string
    n = len(s) #eg 'IX' IS 2
    # This variable will store result
    num = roman_map[s[n - 1]] #the last character
    # Loop for each character from right to left
    for i in range(n - 2, -1, -1): #class range(start, stop[, step])
        # Check if the character at right of current character is bigger or smaller
        if roman_map[s[i]] >= roman_map[s[i + 1]]:
            #in roman numbers if smaller number is on the right, you add
            num += roman_map[s[i]]
        else:
            # in roman numerals if smaller is before larger subtract
            num -= roman_map[s[i]]
    print(num)
    return num


def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []

    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        for row in csvReader:
            jsonArray.append(row)

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)


if __name__ == '__main__':
    #davidodhiambo_web()
    #uni_qify2("fariba")
    #replace_string("fariba","f","F")

    #for i in fib5(0):
        #print(i)

    #encrypt("David")
    #print(factorial(5))

   # print(calculate_pi(64))
   # print(count_vowels("Fariba"))

    fruits = "Alfalfa Sprouts Apple Apricot Artichoke Asian Pear Asparagus Atemoya Avocado Bamboo Shoots Banana Beans" \
             " Bean Sprouts Beets Belgian Endive Bitter Melon Bell " \
             "Peppers Blackberries Blueberries Bok Choy Boniato Boysenberries Broccoflower Broccoli Brussels Sprouts " \
             "Cabbage (green and red) Cantaloupe Carambola (star fruit or star apple) Carrots Casaba Melon Cauliflower " \
             "Celery Chayote Cherimoya (Custard Apple) Cherries Coconuts Collard Greens Corn Cranberries Cucumber Dates Dried Plums (a.k.a. prunes)" \
             "Kale Kiwifruit Kohlrabi Kumquat Leeks Lemons Lettuce (Boston, Iceberg, Leaf, Romaine) Lima Beans Limes Longan Loquat Lychee" \
             "Madarins Malanga Mandarin Oranges Mangos Mulberries Mushrooms Napa (Chinese Cabbage) Nectarines" \
             "Okra Onion (green, red, Spanish, yellow, white) Oranges Papayas Parsnip Passion Fruit Peaches Pears Peas (green, snow, sugar snap) " \
             "Peppers (bell – red, yellow, green, chili) Persimmons Pineapple Plantains Plums Pomegranate Potatoes Prickly Pear (Cactus Pear) " \
             "Prunes Pummelo (Chinese Grapefruit) Pumpkin Eggplant Endive Escarole Feijoa Fennel Figs (dry and fresh) " \
             "Garlic Gooseberries Grapefruit Grapes Green Beans Green Onions Greens (turnip, beet, collard, mustard) Guava Hominy Honeydew Melon Horned Melon" \
             "Iceberg Lettuce"

    print(fruits[2])
    create_list('orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana')

    S = [45, 9, 3, 45, 23, 9, 97, 12, 5]
    k = [-1, -4, 5, 8, 9, -5]
    L = [0, -1, 5, 3, 10, 23]
    P = [-1, 0, 1, 2, -1, -4, 5, 8, 9, -5, -12, 14, 11]
    Q = [89, -8, 6, 45, 3, 12, 2, 3]
    merge_lists(S, k, L, P, Q)

    roman_to_int("MCLXVI")
    roman_to_int("MC")
    roman_to_int("C")
    print(len("IX"))

    # driver code
    # deciding the two file paths
    csvFilePath = r'Import_User_Sample.csv'
    jsonFilePath = r'Diseases.json'

    csv_to_json(csvFilePath, jsonFilePath)
