import csv
import heapq
import json
import os
import urllib.request
from functools import cache
from functools import lru_cache
from secrets import token_bytes
from statistics import mode
from typing import Generator
from typing import Tuple

import requests
from gtts import gTTS


def text_to_speech():
    text = input("Enter the text you want to convert to speech: ")
    language = 'en'
    speech = gTTS(text=text, lang=language, slow=False)
    speech.save("text.mp3")
    print("\n 😊Text saved as speech")
    os.system("open text.mp3")

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
    if n == 0: return n
    last: int = 0 #fib(0)
    next: int = 1 #fib(1)
    for _ in range(1, n):
        last, next = next, last + next
    return next

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

# Reading csv files into JSON
def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []

    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        for row in csvReader:
            jsonArray.append(row)

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)

def find_3_consec_nums(num):
    x=[]
    if num % 3 !=0:
        return x
    else:
        n=num//3
        m=n-1
        o=n+1
        x.append(m)
        x.append(n)
        x.append(o)
    print(x)

def rearange_to_smalest(num):

    arr = sorted(str(abs(num))) #sort and rteturn the absolute value
    if num<=0: #check if its 0 or negative
        return -int(''.join(arr[::-1])) #rearange, combine, and add the negative
    # make sure there are no leading zeroes by looping over and swaping with the 1st non-zero
    i = 0
    while arr[i] == '0':
        i +=1
    arr[0], arr[i] = arr[i],arr[0]
    return int(''.join(arr))

assert(rearange_to_smalest(-325) == -532) #check that its true

# find out if array b can be rearanged to equal array a
def can_rearrange(a,b):
    return sorted(a) == sorted(b)
#assert(can_rearrange([1,2,3],[3,2,1]) == True)

# Given two arrays A and B of length N, determine if there is a way to make A equal to B by reversing any subarrays from array B any number of times.
# Signature
# bool areTheyEqual(int[] arr_a, int[] arr_b)
# Input
# All integers in array are in the range [0, 1,000,000,000].
# Output
# Return true if B can be made equal to A, return false otherwise.
def areTheyEqual(arr_a, arr_b):
    return sorted(arr_a) == sorted(arr_b)


#There are n students, numbered from 1 to n, each with their own yearbook. They would like to pass their yearbooks
# around and get them signed by other students.
# You're given a list of n integers arr[1..n], which is guaranteed to be a permutation of 1..n (in other words, it
# includes the integers from 1 to n exactly once each, in some order).
# The meaning of this list is described below.
# Initially, each student is holding their own yearbook. The students will then repeat the following two steps each minute:
# Each student I will first sign the yearbook that they're currently holding (which may either belong to themselves or
# to another student), and then they'll pass it to student arr[i-1]. It's possible that arr[i-1] = i for any given i,
# in which case student I will pass their yearbook back to themselves. Once a student has received their own yearbook back,
# they will hold on to it and no longer participate in the passing process.
# It's guaranteed that, for any possible valid input, each student will eventually receive their own yearbook back and
# will never end up holding more than one yearbook at a time. You must compute a list of n integers output, whose
# element at i-1 is equal to the number of signatures that will be present in student I's yearbook once they receive it back
# Input
# n is in the range [1, 100,000].
# Each value arr[i] is in the range [1, n], and all values in arr[i] are distinct.
# Output
# Return a list of n integers output, as described above.

def findSignatureCounts(arr):
  n = len(arr)
  output = [1] * n  # Initialize with 1 as each student signs their own yearbook
  visited = [False] * n

  for i in range(n):
      if not visited[i]:
          current = i
          cycle = []
          while not visited[current]:
              visited[current] = True
              cycle.append(current)
              current = arr[current] - 1  # -1 because arr is 1-indexed

          cycle_length = len(cycle)
          for student in cycle:
              if arr[student] - 1 != student:  # If not passing to self
                  output[student] = cycle_length

  return output

# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

def printIntegerList(array):
  size = len(array)
  print('[', end='')
  for i in range(size):
    if i != 0:
      print(', ', end='')
    print(array[i], end='')
  print(']', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  expected_size = len(expected)
  output_size = len(output)
  result = True
  if expected_size != output_size:
    result = False
  for i in range(min(expected_size, output_size)):
    result &= (output[i] == expected[i])
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printIntegerList(expected)
    print(' Your output: ', end='')
    printIntegerList(output)
    print()
  test_case_number += 1


#Merger of two sorted arrays
# Given two sorted arrays, merge them such that the elements can be repeated
# Signature
# int[] mergeArrays(int[] a, int[] b)
# Input
# All integers in array are in the range [0, 1,000,000,000].
# Output
# Return an array containing all elements from both arrays sorted in non-decreasing order.
def mergeArrays(a, b):
    return sorted(a + b)

#You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function,
# but instead be stored inside the array nums1. To accommodate this,
# nums1 has a length of m + n, where the first m elements denote the
# elements that should be merged, and the last n elements are set to 0
# and should be ignored. nums2 has a length of n.

# Signature
# void merge(int[] nums1, int m, int[] nums2, int n)
# Input
# All integers in nums1 and nums2 are in the range [0, 1,000,000,000].
# m and n are integers in the range [0, 2000].
# Output
# None
def merge(nums1, m, nums2, n):
    nums1[m:] = nums2
    nums1.sort()


#Given an integer array nums and an integer val, remove all occurrences of val
# in nums in-place. The order of the elements may be changed. Then return the
# number of elements in nums which are not equal to val.Consider the number of
# elements in nums which are not equal to val be k, to get accepted, you need
# to do the following things: Change the array nums such that the first k elements
# of nums contain the elements which are not equal to val. The remaining elements of
# nums are not important as well as the size of nums.Return k.

# Signature
# int removeElement(int[] nums, int val)
# Input
# All integers in nums are in the range [0, 1,000,000,000].
# Output
# Return an integer k, representing the number of elements in nums which are not equal to val.
def removeElement(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k


if __name__ == '__main__':
    text_to_speech()
    #rearange_to_smalest(-63124)
    #find_3_consec_nums(12)
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

    #print(fruits[2])
    #create_list('orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana')

    S = [45, 9, 3, 45, 23, 9, 97, 12, 5]
    k = [-1, -4, 5, 8, 9, -5]
    L = [0, -1, 5, 3, 10, 23]
    P = [-1, 0, 1, 2, -1, -4, 5, 8, 9, -5, -12, 14, 11]
    Q = [89, -8, 6, 45, 3, 12, 2, 3]
    #merge_lists(S, k, L, P, Q)

    #roman_to_int("MCLXVI")
    #roman_to_int("MC")
    #roman_to_int("C")
    #print(len("IX"))

    # driver code
    # deciding the two file paths
    csvFilePath = r'Import_User_Sample.csv'
    jsonFilePath = r'Diseases.json'

    #csv_to_json(csvFilePath, jsonFilePath)


    # Test Cases
    arr_1 = [2, 1]
    expected_1 = [2, 2]
    output_1 = findSignatureCounts(arr_1)
    check(expected_1, output_1)

    arr_2 = [1, 2]
    expected_2 = [1, 1]
    output_2 = findSignatureCounts(arr_2)
    check(expected_2, output_2)

