d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3 = {}
d3.update(d1)
d3.update(d2)
print("Dic1 : ",d1)
print("Dicq2 : ",d2)
for key in d1:
    if key in d2:
        d3[key]=d2[key]+d1[key]
print("After adding the values having same key : ",d3)
print("Performed by Parth and Dhruv")