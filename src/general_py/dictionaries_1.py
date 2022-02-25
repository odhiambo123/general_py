import time
from datetime import datetime, timedelta

def log_visitor_by():

    visitor_by_the_hour = {
            'John J': 1200,
            'Kapilio M': 1400,
            'Ben K': 1500,
            'Jamix R': 1800,
            'Roderick F': 5400
      }

    k = datetime.now() + timedelta(seconds=5)
    print(k)
    time.sleep(2)
    print(timedelta(seconds=5))
    l= time.ctime()

    print(datetime.now())
    print(l)

    print(visitor_by_the_hour.keys())
    print(visitor_by_the_hour.values())

    for i in visitor_by_the_hour.values():
        if i > 1500:
            print(i)
        continue


if __name__ == '__main__':
    log_visitor_by()