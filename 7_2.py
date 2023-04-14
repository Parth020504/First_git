t=(1,2,3,2,4,5,4)
r=()

print("Tuple= ",t)
for i in t:
    if t.count(i)>1 and i not in r:
        r+=(i,)
print("Repeated items= ",r)