'''
  Check whether the strings entered are one or zero edit away.
  Edits performed are: 
    insert a character, 
    remove a character, 
    or replace a character
'''

def single_edit(s1, s2):
  if s1 == s2:
    return True
  if abs(len(s1) - len(s2)) > 1:
    return False
  short_str = s1 if len(s1) < len(s2) else s2
  long_str = s1 if len(s1) > len(s2) else s2
  len_short_str = len(short_str)
  len_long_str = len(long_str)
  index1, index2 = 0, 0
  found = False
  while index2< len_long_str and index1 < len_short_str:
    if short_str[index1] != long_str[index2]:
      if found:
        return False
      found =True
      if len_short_str == len_long_str:
        index1 += 1
    else:
      index1 += 1
    index2 += 1
  return True


s1 = input("Enter first string:  ")
s2 = input("Enter second string:  ")
print(single_edit(s1, s2))
