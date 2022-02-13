text = str(input("text\n"))
string = str(input("string\n"))
found = 0
def shift(strin1, i=0):
  return strin1[i::] + strin1[:i:]
for s in range(len(string)):
  final_str = shift(string, s)
  if final_str in text:
    found +=1
    print("yes")
    print(final_str)
    break
if found ==0:
  print("no")
