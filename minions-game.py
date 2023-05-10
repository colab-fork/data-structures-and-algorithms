import string

input1 = 'BANANA'
players = ['Stuart', 'Kevin']
scores = {player: 0 for player in players}

# Create list of alphabets, vowels and consonants
all_letters = list(string.ascii_lowercase)
vowels = ['a', 'e', 'i', 'o', 'u']
consonants = [x for x in all_letters if x not in vowels]

# Iterate over all possible substrings
for i in range(len(input1)):
    for j in range(i, len(input1)):
        substring = input1[i:j+1]
        if substring[0] in vowels:
            scores['Kevin'] += 1
        else:
            scores['Stuart'] +=1

# Print the winner and their score
if scores['Kevin'] > scores['Stuart']:
    print('Kevin', scores['Kevin'])
elif scores['Stuart'] > scores['Kevin']:
    print('Stuart', scores['Stuart'])
else:
    print('Draw')

