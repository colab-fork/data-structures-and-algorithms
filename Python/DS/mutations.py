def mutate_string(string, position, character):
    for i in range(0, len(string)-1,1):
        if i== position:
            ret = string[:i]+ character+ string[i+1:]
            return ret
    

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
