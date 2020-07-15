#Replace all spaces in string given, with '%20'

def urlify(s,n):
  a = ['']*n
  for i in range(n):
    if s[i] == " " :
      a[i] = "%20"
    else:
      a[i] = s[i]
  return ''.join(a)


s = input("Enter the string:  ")
n = int(input("Enter string size:  "))
print(urlify(s, n))
