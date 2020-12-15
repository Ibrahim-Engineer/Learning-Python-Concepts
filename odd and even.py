original_list = [234,3423,5,46,54]
print("original list")
print(original_list)
print("")



#print odd indeces of list
def odd(lst):
    newlst = []
    for i, e in enumerate(lst):
        if i%2 !=0:
            newlst.append(e)
    return newlst
print("odd index values")
print(odd(original_list))
print("")

#print even indeces of list
def even(lst):
    newlsttwo = []
    for i, e in enumerate(lst):
        if i%2 ==0:
            newlsttwo.append(e)
    return newlsttwo
print("even index values")
print(even(original_list))
print("")
#print odd numbers of list

def evennum(lst):
    evenlst = []
    for i in lst:
        if i%2 ==0:
            evenlst.append(i)
    return evenlst
print("even numbers")
print(evennum(original_list))
print("")
#print even numbers of list
def oddnum(lst):
    oddlst = []
    for i in lst:
        if i%2 !=0:
            oddlst.append(i)
    return oddlst
print("odd numbers")
print(oddnum(original_list))
print("")