num=input()
lst=[]
for i in num:
  if(int(i)%2==1):
    lst.append(i)
print(" ".join(lst))
