# general_py

## Python:
- Is general purpose programing language used for:
  - Web development server side
  - software development and workflows, data management
  - mathematics
  - system scripting
  - [src](https://www.w3schools.com/python/python_intro.asp).
- Python:
  - has a simple syntax that allows you to program in fewer lines of code.
  - is easy to learn
  - it can be both either functional and object-oriented
  - it is ideal for data mining and data facilitation
  - good community support
- Installation and setup:
  - Download [anaconda](https://www.anaconda.com/products/individual)
-Data Type:
  - Text type: str
  - Numeric Types: int, float, complex
  - Sequence Type: list, tuple, range
  - Mapping Type: dict
  - Set type: bool
  - Binary Types: bytes, bytearray, memoryview
  - [reference](https://docs.python.org/3/library/stdtypes.html?highlight=data%20types)
    - To get the datatype, use the type() function.
- Structure:
  - Python lets us split the program into modules that can be reused.
  - It is interpreted
  - It is extensible
- Start:
  - start by checking if you have python installed properly
  - `python --version`
  - `python` will launch python
  - to quit , type `quit()`
- Implementations:
  - CPython - written in C
  - JPython - Written in Java
  - Python for .NET - written in C but is a managed .NET application
  - IronPython - an alternative to Python.NET, providing availability to .NET libraries, also generate IL and compiles pyton code directly to .NET assemblies.
  - PyPy - written completely in Python.
- Notation:
  - modified BNF grammar notation
    - [BNF](http://www.cs.umsl.edu/~janikow/cs4280/bnf.pdf) or Backus-Naur Form is used to define syntax using:
      - a set of terminal symbols
      - a set of non-terminal symbols
      - a set of production rules of the form `Left-Hand-Side ::= Right-Hand-Side`
        - Left-hand side contains non terminal 
        - Right-hand side contains either terminal or non-terminal or both.
        
          - left-hand side can be replaced by the right-hand expression
          - syntactical correct sentences follow the above-mentioned order.
          - if a parse tree cannot be built to show the sentence derives from the production rules, the sentence is deemed syntactically incorrect.
          
  ####  Grammar:
      - A sentence can be well-formed but still meaningless.
      - Semantics will define the meaning.
    - [sources](https://docs.python.org/3/reference/introduction.html#implementations)
  #### Example
        - A grammar that recognizes exactly two strings `things are getting better` and `things are getting worse`
    
        ```
      
      
        things ::= "things are" condition
           condition ::= "getting better" | "getting worse"  
                           things
                           /     \
                          /       \
            "things are"          "condition"
                                       |
                                  "getting better"
      
      
        ```
        
```
car     ::= make
         |  car ", " make
make ::= "Ford" | "Toyota" | "BMW"
The string "Ford, Toyota, BMW, Toyota, Ford" is in the language because of the following parse tree:

                                 ________ car __________
                                /                \      \
                    _________ car ________        |    make
                   /               \      \       |      |
           ______ car _______       |      make   |      |
          /           \      \      |      |      |      |
     __ car __         |   make     |      |      |      |
    /    |    \        |      |     |      |      |      |
  car    |   make      |      |     |      |      |      |
   |     |      |      |      |     |      |      |      |
make     |      |      |      |     |      |      |      |
   |     |      |      |      |     |      |      |      |
"Ford" " , " "Toyota" ", " "BMW" ", " "Toyota" ", " "Ford"

```
#### Grammar for Empty language
`empty ::= `

#### Grammar for "olingthi"
- "olingthi" only takes an empty string as the only valid sentence in this language.

 `olingthi ::= ""`
 
- notice the difference between empty language and the empty string.

#### Grammar for a letter language

  `letter ::= "a" | "b" | "c" | "d" | ... | "z"`

```
letter ::= "a"
letter ::= "b"
letter ::= "c"
letter ::= "d"
...
letter ::= "z"
```
#### Defining a grammar for the word language
  `word ::= letter | word letter`

In this grammar featuring recursive rule, "water" is in this language
- "w" is a word (a sentence in the word language) because it is a letter 
- `word ::= letter`
- "wa" is a word because "w" is a word and "a" is a letter
- `word ::= word letter`
- "wat" is a word because "wa" is a word and "t" is a letter
- "wate" is a word because "wat" is a word and "e" is a letter
- ...

[reference](https://github.com/cs61)

- learn the [shell](https://linuxcommand.org/lc3_learning_the_shell.php)
- Bash Reference [Manual](https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html)
- 
#### Interpreter and its environment
- source files are treated as UTF-8 by default
- to change from  default encoding use: `-*- coding: encoding -*-` replacing 'encoding' with one of the valid [codecs](https://docs.python.org/3/library/codecs.html#standard-encodings)
- [Argument Passing](https://docs.python.org/3/tutorial/interpreter.html#argument-passing)
- script's name and its arguments are converted into a list and stored in the `argv` variable inside the `sys`
module `sys.argc[]`

#### Objects:
- used for data abstraction in Python
- abstraction is used as a productivity enhancer
#### Von Neumann model
- Is a form of computer organization based on the stored-program concept, it comprises the following components:
  - memory
  - CPU
  - Input
  - Output
  - Control unit
- Computer systems are organized as systemic set of transformations that brings a problem described in human language to the transistors that actually execute it.
  - you have a problem statement that explains what the issue is.
  - You then transform that into an algorithm
    - Procedural steps that ensure/guarantee precise execution by a computer.
    - The procedure must eventually terminate.
  - Algorithm is transformed into a computer program
  - ISA is the instruction set architecture available in every computer. It is a list of all instruction that a computer can execute and different computers might have different ISA. An example of ISA is x86.
  - A high level programming language such as Python is translated into specific ISA using a translating program called a compiler.
  - Low level programs written in low-level computer specif assembly language is translated using assembler
- Micro-architecture or the microprocessor architecture is a specific implementation if ISA in a given processor depending on the intended goals. For instance the x86 has been implemented slightly differently in Intel and AMD.
- List of Intel CPU [microarchitectures](https://en.wikipedia.org/wiki/List_of_Intel_CPU_microarchitectures)
- List of AMD [microarchitectures](https://en.wikichip.org/wiki/amd/microarchitectures)

At the root of the microarchitecture is the simple [logic circuit](https://circuitverse.org/simulator). You can learn more about logic gates [here](https://www.electronics-tutorials.ws/logic/logic_1.html)

It is also helpful to be have some knowledge of [binary numbers](https://www.electronics-tutorials.ws/binary/bin_1.html) and other [digital circuit Number Systems](https://drive.google.com/file/d/19G_eiyZ9HarpjZPlEYui4TGyVu4Ol_D1/view?usp=sharing)

AND `output = input1 ∧ input2` both are true
OR  `output = input1 ∨ input2` one or both are true

NOT `output = ∼ input1` the output is opposite of the input

![alt oneGate.png](img/oneGate.PNG)
<br>

![alt twoGateSeries](img/twoGateSeries.PNG)
<br> 

![alt twoGatesparallel](img/twoGateParallel.PNG)
<br>

![alt threeGatesParallelAndSeries](img/threeGatesParallelAndSeries.PNG)
<br>

![alt Circuit1](img/Circuit-1.PNG)
<br>

![alt Circuit2](img/Circuit-2.PNG)
<br>

![alt AND](img/AND.PNG) AND `output = input1 ∧ input2` both are true
<br>

![alt OR](img/OR.PNG) OR  `output = input1 ∨ input2` one or both are true
<br>

![alt NOT](img/NOT.PNG) NOT `output = ∼ input1` the output is opposite of the input.
<br>

# Libraries.
### Machine learning
- [Federeted Learnig](https://federated.withgoogle.com/)
- [Scikit-Learn](https://scikit-learn.org/stable/index.html)
- [TensorFlow](https://www.tensorflow.org/)
- [Pytorch](https://pytorch.org/tutorials/)
- [Theano](https://pypi.org/project/Theano/)
<br>

### Web Development
- [Django](https://www.djangoproject.com/)
- [Flask](https://palletsprojects.com/p/flask/)
- [Gunicorn](https://gunicorn.org/)
- [Celery](https://docs.celeryproject.org/en/stable/getting-started/introduction.html)
- [Bottle](https://bottlepy.org/docs/dev/)
- [Web2py](http://www.web2py.com/books/default/chapter/29/01/introduction)
- [Pyramid](https://trypyramid.com/)
- [FastAPI](https://fastapi.tiangolo.com/)
<br>

### Ethical Hacking

- [IMPacket](https://www.secureauth.com/labs/open-source-tools/impacket/)
- [Cryptography](https://cryptography.io/en/latest/)
- [Scapy](https://scapy.readthedocs.io/en/latest/)
- [pwntools](https://python3-pwntools.readthedocs.io/en/latest/)
- [Nmap](https://nmap.readthedocs.io/en/latest/nmap.html)
<br>

### Scraping

- [Scrapy](https://docs.scrapy.org/en/latest/intro/overview.html)
- [BeautifulSoup](https://beautiful-soup-4.readthedocs.io/en/latest/)
- [Selenium](https://selenium-python.readthedocs.io/)
- [Requests](https://docs.python-requests.org/en/master/index.html)
- [PyRobot](https://pyrobot.org/docs/overview)
- [Newspaper3k](https://newspaper.readthedocs.io/en/latest/)
<br>

### Game Development

- [Pygame](https://www.pygame.org/wiki/about)
- [Pyglet](https://docs.pyglet.org/en/latest/modules/pyglet.html)
- [Cocos2d](https://docs.cocos.com/creator/manual/en/)
- [panda3D](https://docs.panda3d.org/1.10/python/index)
<br>

### Image Processing

- [Pillow](https://pillow.readthedocs.io/en/stable/)
- [Scikit-Image](https://scikit-image.org/)
- [OpenCV](https://docs.opencv.org/4.x/d1/dfb/intro.html)
- [Pytesseract](https://github.com/madmaze/pytesseract)
<br>

### Mobile Development

- [Kivy](https://kivy.org/doc/stable/)
- [BeeWare](https://beeware.org/)
<br>

### Data Science

- [Scikit-Learn](https://scikit-learn.org/stable/index.html)
- [Theano](https://en.wikipedia.org/wiki/Theano_(software))
- [Scipy](https://scipy.org/)
- [Numpy](https://numpy.org/)
- [Pandas](https://pandas.pydata.org/)
- [Scrapy](https://docs.scrapy.org/en/latest/intro/tutorial.html)
<br>

### Desktop Applications

- [wxPython](https://wiki.wxpython.org/)
- [PyQT5](https://www.riverbankcomputing.com/software/pyqt/)
- [Pyside](https://wiki.qt.io/Qt_for_Python)
- [PySimpleGUI](https://pysimplegui.readthedocs.io/en/latest/)
<br>

### BioInformatics

- [BioPython](https://biopython.org/)
- [ProDy](http://prody.csb.pitt.edu/)
- [SciKit-Bio](http://scikit-bio.org/)
- [Pyensembl](https://pyensembl.readthedocs.io/en/latest/pyensembl.html)
- [PySB](https://pysb.org/)
<br>

### Mathematics and Computation

- [Theano](https://www.tutorialspoint.com/theano/index.htm)
- [Scipy](https://docs.scipy.org/doc/scipy/reference/)
- [Numpy](https://numpy.org/)
- [Statsmodels](https://www.statsmodels.org/stable/index.html)
- [CuPy](https://cupy.dev/)
- [SymPy](https://www.sympy.org/en/index.html)
<br>

### Testing and Automation

- [Robotframework](https://robotframework.org/)
- [Automate](https://automate.io/)
- [Pytest](https://docs.pytest.org/en/6.2.x/)
- [Nose](https://nose.readthedocs.io/en/latest/)
<br>

### Astronomy

- [SpacePy](https://github.com/spacepy/spacepy)
- [Astropy](https://docs.astropy.org/en/stable/)
- [SunPy](https://docs.sunpy.org/en/stable/)
<br>

### Data Visualization

- [Matplotlib](https://matplotlib.org/stable/index.html)
- [Seaborn](https://seaborn.pydata.org/)
- [Plotly](https://plotly.com/)
- [Bokeh](https://bokeh.org/)
- [Pydot](https://github.com/pydot/pydot)
<br>

### Robotics

- [RobotFramework](https://robotframework.org/)
- [Pydy](https://www.pydy.org/)
- [PyBotics](https://pybotics.readthedocs.io/en/latest/)
<br>

### Cryptocurrency

- [BitCoinLib](https://bitcoinlib.readthedocs.io/en/latest/index.html)
- [CCXT](https://docs.ccxt.com/en/latest/manual.html)
<br>

### Data Mining

- [Scrapy](https://scrapy.org/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Selenium](https://www.selenium.dev/documentation/)
<br>

### Computer Vision

- [OpenCV](https://opencv.org/opencv-free-course/)
- [Mahotas](https://mahotas.readthedocs.io/en/latest/)
- [SimpleCV](http://simplecv.org/)
<br>

### Quantum Computing

  - [QuTiP](https://qutip.org/)
  - [PyQuil](https://pyquil-docs.rigetti.com/en/stable/compiler.html)
  - [Cirq](https://quantumai.google/cirq)
  - [Qiskit](https://qiskit.org/)
<br>
  
### Statistical Computation

- [Pandas](https://pandas.pydata.org/)
- [Statsmodels](https://www.statsmodels.org/stable/index.html)
<br>

### Command Line Applications

- [Typer](https://typer.tiangolo.com/tutorial/first-steps/)
- [cmd2](https://cmd2.readthedocs.io/en/stable/)
- [Click](https://click.palletsprojects.com/en/7.x/)
<br>

### Signal Processing

- [Scipy](https://docs.scipy.org/doc/scipy/reference/tutorial/index.html)
- [PyWavelets](https://pywavelets.readthedocs.io/en/latest/)
<br>

### Interactive Computing

- [IPython](https://ipython.org/)
- [Jupyter Notebook](https://jupyter.org/)
<br>

### Deep Learning

- [TensorFlow](https://www.tensorflow.org/learn)
- [PyTorch](https://pytorch.org/)
- [Keras](https://keras.io/)
- [Chainer](https://chainer.org/)
<br>

### Geographic Processing

- [GeoPandas](https://geopandas.org/en/stable/)
- [Shapely](https://shapely.readthedocs.io/en/stable/project.html)
<br>

### Sciences

- [Scipy](https://scipy.org/)
- [Statsmodels](https://www.statsmodels.org/stable/index.html)
- [CuPy](https://cupy.dev/)
- [PsychoPy](https://www.psychopy.org/)
<br>

### Natural Language Processing

- [NLTK](https://www.nltk.org/)
- [TextBlob](https://pypi.org/project/textblob/)
- [Stanza](https://stanfordnlp.github.io/stanza/)
- [spaCY](https://spacy.io/)
- [Gensim](https://pypi.org/project/gensim/)
<br>

### Cybersecurity

- [IMPacket](https://www.kali.org/tools/impacket/)
- [Cryptography](https://cryptography.io/en/latest/)
- [Scrapy](https://pypi.org/project/Scrapy3/)
- [Twisted](https://pypi.org/project/Twisted/)
- [Faker](https://faker.readthedocs.io/en/master/)

### certifications
 - [Terraform](https://learn.hashicorp.com/collections/terraform/certification)
 - [Kubernetes](https://kubernetes.io/docs/tutorials/)
 - [Orchestration](https://www.redhat.com/en/topics/automation/what-is-orchestration)

### references
- [Digital circuits and Number Systems](https://www.math.umd.edu/~immortal/CMSC250/notes/notes_2.pdf)
- [programming and machine organization](https://cs61.seas.harvard.edu/site/2021/)
- [Introduction to Computing systems](https://users.ncsa.illinois.edu/kindr/teaching/ece190_sp11/lectures/)
- [MATHEMATICAL SYMBOLS](https://en.wikipedia.org/wiki/Glossary_of_mathematical_symbols)
- [Bit Twiddling Hacks](https://graphics.stanford.edu/~seander/bithacks.html)
- [Algorythm Types](https://1drv.ms/p/s!AsTcf-RoH_KDn2ntJVdYcXgYZgbN?e=DVwUmG)
- 
- <br>

# DATA STRUCTURES IN PYTHON:
### Main refference : [Python std library](https://docs.python.org/3/library/)
- Lists; other languages use arrays 
- Set 
- Tuples
- Dictionary

### LIST
- indexed 0 based
- changeable by adding removing 
  - new items add to the end
    - allow duplicate values
        ```
        my_list = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
        the_list = ['school', 'is'. 'good']
        name = ['Mr', 'Steele']
  
        functions include:  
      my_list.index(), 
      my_list.copy(), 
      my_list.pop(), 
      my_list.remove(), 
      my_list.clear(), 
      my_list.extend(),
      my_list.reverse(), 
      ' '.join(the_list)
      '. '.join(name)
      
      slicing a list:
      some_list[start:end:step]
      
      first_list = [1, 2, 3, 4, 5, 6]

      first_list[1::2] # [2, 4, 6]

      first_list[::2] # [1, 3, 5]
    
        ```
      <br>

### Tuples
- defined order of items unchangeable
- allow duplicates
- indexed 0 based
- can contain different data types

  Make a tuple using the function
       tuple()
     
       For example:
       my_tuple = tuple(("abc", 34, True, 40, "male","apple", "banana", "cherry"))

### Dictionaries

- Also called hash tables, hash, hash map, map, unordered map.
- Stores data in kte:value pairs
- declared inside curly brackets
  - O(1) lookups
  - no duplicates
  - slow worst case lookup O(n)
  - not cache friendly
  - create using curly braces of the dict() function
  - iterate over using key() values() and items()
  - using methods like get ensures more graceful handling of the errors
  ```
      visitor_by_the_hour = {
            'John J': 1200,
            'Kapilio M': 1400,
            'Ben K': 1500,
      }
  
      
  
      instructor = {
              "name": "Colt",
              "owns_dog": True,
              "num_courses": 4,
              "favorite_language": "Python",
              "is_hilarious": False,
              44: "my favorite number!"
      }
    To access all the values in a disctionary we use .values() operator
    
    for value in instructor.values():
    print(value)

    # "Colt"
    # True
    # 4
    # "Python"
    # False
    # "my favorite number!"

    To access all the Key in the dictionary we use the .key() method
  
    for key in instructor.keys():
    print(key)

    # name
    # owns_dog
    # num_courses
    # favorite_language
    # is_hilarious
    # 44
  
  To access all keys and values use the .items()
    for key,value in instructor.items():
    print(key,value)

    # name "Colt"
    # owns_dog True
    # num_courses 4
    # favorite_language "Python"
    # is_hilarious False
    # 44 "my favorite number!"
  
  To check is a particular key is on the dictionary
    "name" in instructor # True
    "awesome" in instructor # False
  
  To check if a value is in the dictionary
  
    "Colt" in instructor.values() # True
    "Nope!" in instructor.values() # False
  ```
  -Major operations include

  ```
    clear()   : clears all the keys and values in the dictionary,
    copy()    : makes a copr of the dictionary
    fromkeys(): creates a key value pair from comaseparated values
    values()  :  
    update(), : updates keys and values in the dictionary with another set of key-value pairs 
    get(),    : Retrieves key in an object and return non instead of an error if the key does not exist
    items(),  :
    keys(), 
    pop(),    : accepts one argument and removes the that key value pair from the dictionary
    popitem().: takes no arguments and removes a random key from the dictionary
    
    Dictionary Comprehension:
    { ____:____ for ___ in ____} iterates over values by using the .items()
    numbers = dict(first=1, second=2, third=3)
  
    squared_numbers = {key: value ** 2 for key,value in numbers.items()}
    print(squared_numbers) # {'first': 1, 'second': 4, 'third': 9}
    
    {num: num**2 for num in [1,2,3,4,5]}
  
    str1 = "ABC"
    str2 = "123"
    combo = {str1[i]: str2[i] for i in range(0,len(str1))} 
    print(combo) # # {'A': '1', 'B': '2', 'C': '3'}
  
  Conditional logics with dictionaries:
  
    num_list = [1,2,3,4]
    { num:("even" if num % 2 == 0 else "odd") for num in num_list }
    # {1: 'odd', 2: 'even', 3: 'odd', 4: 'even'}
  
  ```


###SET
  - A Set is like a hash map except it only stores keys , without values
    - tracking groups of items
    - nodes visited
    - characters seen
    - colors used in neighbor nodes
    ```
      visitor_by_the_hour = set()
    
      visitor_by_the_hour.add('John J')
      visitor_by_the_hour.add(Kapilio M')
      visitor_by_the_hour.add('Ben K)
    
      'John M' in visitor_by_the_hour # True
    
    ```
    Major Operations in set include:
      ```add(), update(), discard(), remove(), pop(),clear().```
## Keywords in python
  - Python has 3 Keywords
```
False	      def	if	        raise
None	      del	import	        return
True	      elif	in	        try
and	      else	is	        while
as	      except	lambda	        with
assert	      finally	nonlocal        yield
break	      for	not	
class	      from	or	
continue      global	pass	

```

  [Python Tokens](https://github.com/python/cpython/blob/3.10/Grammar/Tokens)
  [Python Grammar Specification](https://github.com/python/cpython/blob/3.10/Grammar/python.gram)

### Algorithms

- Types of algorithms include:
  - Backtracking algorithms
  - Branch and bound 
  - Bruteforce
  - Divide and Conquer
  - Dynamic programming
  - Greedy 
  - Randomized
  - Simple recursive 

### Efficiency in storage:
  - If an integer is never going to be greater than 65,535, then it can be store as a 16-bit unsigned integer
  - In python there is no 16-bit or 64-bit unsigned integer, instead there is just an int type that can store numbers to arbitrary precision.
  - to get the size of an object in memory, you can use sys.getsizeof()

## Questions

1. Given a list or an array of numbers, how do you find three that add up to a given number? [sol =>](https://github.com/odhiambo123/general_py/blob/main/src/general_py/sum_zero_from_3.py)
2. How do you find the K'th largest number from a stream of numbers? [sol =>](https://github.com/odhiambo123/general_py/blob/main/src/general_py/kth_largest.py)
3. How to copy an image from a webpage [sol =>](https://github.com/odhiambo123/general_py/blob/main/src/general_py/files_txt_str.py)
4. String replacement [sol =>](https://github.com/odhiambo123/general_py/blob/main/src/general_py/files_txt_str.py)
5. Count the numbe of lines in a file [sol =>](https://github.com/odhiambo123/general_py/blob/main/src/general_py/files_txt_str.py)
6. How to uniqify a sequence [sol =>](https://github.com/odhiambo123/general_py/blob/main/src/general_py/general_funcs.py)
7. Get website's html [sol =>](https://github.com/odhiambo123/general_py/blob/main/src/general_py/general_funcs.py)
8. Read and write data from and to a file [sol =>](https://github.com/odhiambo123/general_py/blob/main/src/general_py/general_funcs.py)
9. Find the most common word
10. What is s bottleneck in the algorithm
11. given a smaller string a and a larger string b, design an algorithm to find all the permutations of string 'a' in string 'b'.
12. Build an algorithm to print [all permutations of a string]()
13. How would you keep track of numbers that are randomly generated and stored in an expanding array
14. How to keep [track of all unique visitors]() who came in the last 10 minutes.
15. From a positive integer n Generate a quare matrix filled with elements from 1 to n^2 in spiral order
16. convert roman numbers to integers
17. Convert integers to roman numbers.
18. From a 2d grid map of 0's(water) and 1's(land). count the number of islands
19. Finds the shortest path from one node to all other nodes in a weighted graph[Dijkstra's Algorithm]()
20. Arranges the nodes in a directed, acyclic graph in a special order based on incoming edges.[Topological Sort]()
21. Finds the cheapest set of edges needed to reach all nodes in a weighted graph[Minimum Spanning Tree]()
22. Find out if a binary tree is balanced[BFS]()
23. Where each stone has a weight(integer) and a value(dollars) for example (5,210) for five pounds and 210 dollars. write a function max_fit()
    to find the correct combination list/tuple of stones to fill the bag with maximum value. [Combinatorial Optimization]()
24. Show some [bit manipulations](https://graphics.stanford.edu/~seander/bithacks.html)
25. Given an integer num, return three consecutive integers(as a sorted array) that sum to num. If num cannot be expresses as the sum of three consecutive integers, return an empty array.[Sol](https://gist.github.com/1628842308132c770453d6f490854800)
26. Given an integer num, rearrange the digits of num such that its value is minimized, and it does not contain any leading zeros. return the rearranged number with minimal value. note: The sign should not change. constraints -10^15<=num<10^15 [Sol](https://gist.github.com/4dea14c275dd825eee8f7aa945b7a46c)
27. create JSON from CSV [code](https://gist.github.com/e16806d7db55e6bcc431a378d4e8999c)
28. Text to speech[code](https://gist.github.com/odhiambo123/d0153691b23e6f678ea4953cccf56b39)
29. 