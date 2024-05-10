def minion_game(s):
    import string
    st = list(string.ascii_lowercase)
    vowels = list('aeiouAEIOU')

    consonants = [char for char in st if char not in vowels]
    players = ['Stuart', 'Kevin']
    scores = {player:0 for player in players}

    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j+1]
            if substring[0] in vowels:
                scores['Kevin'] +=1
            else:
                scores['Stuart'] += 1
                
    if scores['Kevin'] > scores['Stuart']:
        result = ("Kevin", scores['Kevin'])
    elif scores['Stuart'] > scores['Kevin']:
        result = ("Stuart", scores['Stuart'])
    else:
        result = ("Draw", scores['Kevin'])
    print(f"{result[0]} {result[1]}")


if __name__ == '__main__':
    s = input()
    minion_game(s)
    
"""
s = 'BANANA'
>>> minion_game(s)
('Stuart', 12)
>>>   
  
"""
   
