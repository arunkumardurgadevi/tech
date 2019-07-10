ab=list(input())
lst=[]
for i in ab:
  if i not in lst:
    lst.append(lst)
if(ab==lst):
  print("yes")
else:
  print("no")
