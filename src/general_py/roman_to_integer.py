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

if __name__=='__main__':
    roman_to_int("MCLXVI")
    roman_to_int("MC")
    roman_to_int("C")
    print(len("IX"))