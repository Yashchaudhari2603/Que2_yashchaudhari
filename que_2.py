arr = []
for i in range(3):
    arr.append(input())
    
if len(arr) == 1:
  print(arr[0])
else:
  
  arr.sort()
  result = ""
  
  for i in range(len(arr[0])):
      
      if arr[0][i] == arr[-1][i]:
          result += arr[0][i]
      else:
          break
  print(result)
