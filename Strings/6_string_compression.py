def string_compression(s):
  l = []
  count = 0
  for i in range(len(s)-1):
    if s[i] == s[i+1]:
      count += 1
    else:
      l.append(s[i] + str(count+1))
      count = 0
  l.append(s[-1] + str(count+1))
  result = ''.join(l)
  if len(result) < len(s):
    return result
  return s


print(string_compression(input("Enter the string:  ")))
