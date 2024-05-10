def bonAppetit(bill, k, b):
    total = sum(bill)//2
    i=0
    while i <= k:
        if i == k:
            bill.remove(bill[i])
        i += 1    
    anna = sum(bill)//2
    if anna != b:
        ret = abs(anna-b)
        print(ret)
    else:
        print('Bon Appetit')
        
bonAppetit(bill, k, b)

"""
k = 1
bill = [3, 10, 2, 9]
b = 7

>>> %Run -c $EDITOR_CONTENT
Bon Appetit
>>> 


"""
