import urllib
def add_one(number):
    return number + 1

# String replacement
def replace_string(txt, x, y):
    print("replacing: " + x + " with " + y)
    z = txt.replace(x,y)
    print(z)

def copy_image():
    # The URL of the image to be downloaded
    link = "https://images.unsplash.com/photo-1643208932920-45a9d127d30f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1587&q=80"
    # The name of the new file
    filename = "image1.jpg"
    urllib.request.urlretrieve(link, filename)

def count_lines_1(file_x):
    print("Counting the number of lines using usm(i for _ in ")
    with open(file_x) as my_file:
        num_lines= sum(1 for _ in my_file)
        print(num_lines)