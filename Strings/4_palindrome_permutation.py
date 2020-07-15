#Check whether given string is a permutation of a palindrome


def palin_perm(s):
  d = {}
  odd = 0
  for i in s:
    if i != " ":
      if i not in d:
        d[i] = 1
      else:
        d[i] += 1
  for key,value in d.items():
    if value%2 != 0:
      odd += 1
  if len(s) %2 == 0:
    return odd == 0
  else:
    return odd == 1

s = input("Enter the string: ")
print(palin_perm(s.replace(" ","")))
