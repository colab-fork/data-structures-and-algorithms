def is_palindrome(string):
    for i in range(1, len(string)+1):
        if string[i-1] != string[-i]:
            result = False
        else:
            result = True
    print(result)
    
is_palindrome('racecar')



"""
>>> %Run -c $EDITOR_CONTENT
True

"""
