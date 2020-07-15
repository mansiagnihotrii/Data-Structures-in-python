#Check if s1 is permutation of s2

def permutation(s1, s2):
  d = {}
  if len(s1) != len(s2):
    return False
  for i in s1:
    if i not in d:
      d[i] = 1
    else:
      d[i] += 1
  for i in s2:
    if i in d:
      d[i] -= 1
      if d[i]<0:
        return False
    else:
      return False
  return True


s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print(permutation(s1, s2))
