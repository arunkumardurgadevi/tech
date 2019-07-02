str=input()
len1=len(str)
mid=int((len1- 1)/2)
if(len1%2!=0):
    print(str[0:mid]+'*'+str[mid+1:])
else:
    print(str[0:mid]+'**'+str[mid+2:])
