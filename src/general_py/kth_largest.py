def kth_largest(k, stream):
    try:
        List = list(map(int, stream.split(',')))
        List.sort()
        if k > len(List) or k<=0:
            print('Value of k is out of bounds for this stream', sep="")
        else:
            print(k, 'th largest number of the stream is : ' , List[-k], sep="")
    except:
        print('please use the correct format comma separated')

if __name__=='__main__':
    kth_largest(-0,"0,-1,5,3,10,23,45,9,3,45,23,9,97,12,5")
    #kth_largest(8, "1,5,3,10,23,45,9,3,45,23,9,97,12,5")
