ab=list(input())
lst=[]
for i in ab:
  if i not in lst:
    lst.append(lst)
if(ab==lst):
  print("Yes")
else:
  print("No")
