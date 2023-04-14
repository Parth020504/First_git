s1={1,2,3,4,5}
s2={4,5,6,7,8}

print("Intersection of sets ",(s1 & s2))
print("Union of sets ",(s1 | s2))
print("Set difference ",(s1-s2))
print("Symmetric difference ",(s1^s2))
s1.clear()
print("After clearing set 1", s1)