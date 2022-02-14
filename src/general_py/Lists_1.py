import heapq
import statistics
from statistics import mode

def create_list(*args, **kwargs):
    my_list =  list(args,**kwargs)
    #fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
    print('\n The original lisst is ', my_list)
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

def merge_lists(*args):

   new_list = sorted(list(heapq.merge(*args)))
   print(new_list)


if __name__ == '__main__':
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

    S = [45,9,3,45,23,9,97,12,5]
    k = [-1, -4,5,8,9,-5]
    L = [0, -1,5,3,10,23]
    P = [-1, 0, 1, 2, -1, -4,5,8,9,-5,-12,14,11]
    Q = [89,-8,6,45,3,12,2,3]
    merge_lists(S,k,L,P,Q)