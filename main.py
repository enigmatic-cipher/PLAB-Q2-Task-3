"""
Count digits and alphabets in input string. Assume string contains only alphabets and digits.
Note: Input string can contain letters in both the cases.
Input-> "MostWanted50"
Output-> 
Digits-2 
Alphabets-10
"""

st = "MostWanted50"
ln = len(st)
alpha = 0
dig = 0
for i in range(0,ln):
  ch = st[i]
  if (ch>="0" and ch<="9"):
    dig = dig + 1
  elif (ch>="a" and ch<="z") or (ch>="A" and ch<="Z"):
    alpha = alpha + 1
print(f"Digits:{dig}")
print(f"Alphabets:{alpha}")
