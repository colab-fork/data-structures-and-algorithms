s1 = 'listen'
s2 = 'silent'
def is_anagram(s1, s2):
    print(sorted(s1.lower()) == sorted(s2.lower()))
    
is_anagram(s1, s2)


"""
>>> %Run -c $EDITOR_CONTENT
True

"""
