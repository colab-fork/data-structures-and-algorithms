if __name__ == '__main__':
    s =input()
    i = 0
    while i < len(s):
        if s[i].isalnum() == True:
            print(True)
            break
        else:
            i += 1
            if i == len(s): 
                print(False)
                break
    j= 0
    while j < len(s):
        if s[j].isalpha() == True:
            print(True)
            break
        else:
              j += 1
              if j == len(s):
                  print(False)
                  break
    k = 0
    while k < len(s):
        if s[k].isdigit() == True:
            print(True)
            break
        else:
              k += 1
              if k == len(s):
                  print(False)
                  break
    l =0
    while l < len(s):
        if s[l].islower() == True:
            print(True)
            break
        else:
              l += 1
              if l == len(s):
                  print(False)
                  break
    m = 0
    while m < len(s):
        if s[m].isupper() == True:
            print(True)
            break
        else:
              m += 1
              if m == len(s):
                  print(False)
                  break
    

        