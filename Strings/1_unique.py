#Determine if all characters in string is unique

def isunique(x):
  d = {}
  for i in x:
    if i not in d:
      d[i] = 1
    else:
      return False
  return True

print(isunique(input()))
