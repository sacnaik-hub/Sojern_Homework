version1 = input("Enter the first version: " )
version2 = input("Enter the second version: " )

def compareVersion(version1: str, version2: str) -> int:
  #split the character in the strings based on the delimiter (.)
  l1 = version1.split(".")
  l2 = version2.split(".")

  #to traverse through the list we need length of the list
  m = len(l1)
  n = len(l2)

  #add zeros in the missing place
  for i in range(max(m,n)):
    if i < m:
      z1 = int(l1[i])
    else:
      z1 = 0
          
    if i < n:
      z2 = int(l2[i])
    else:
      z2 = 0

    #compare z1 and z2 and return the value
    if (z1 > z2):
      return 1
    if (z2 > z1):
      return -1
    else:
      return 0

ans = compareVersion(version1,version2)
print("The returned result is: ", ans)
