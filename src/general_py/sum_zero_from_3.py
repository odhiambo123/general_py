def sum_zero(nums,sum):
    #sort the numbers
    #the first number be nums[i]
    #the second number be nums[j]
    #the third number be
    nums.sort()
    #define an array result
    result = []

    for i in range(len(nums)-2):
        for j in range(0, len(nums)-1):
            #look for the third number
            for k in range(j +1, len(nums)):
                if nums[i]+nums[j]+nums[k]==sum:
                    print(nums[i], " ,",nums[j]," ,",nums[k])
                    return True
    print("no match")
    return False
if __name__ == '__main__':
    nums = ([-1, 0, 1, 2, -1, -4,5,8,9,-5,-12,14,11])
    print(sum_zero(nums,5))



