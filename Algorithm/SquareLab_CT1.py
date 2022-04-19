Array Challenge
Have the function ArrayChallenge(arr) take the array of integers stored in arr,
and determine if any two numbers (excluding the first element) in the array can sum up to the first element in the array. 
For example: if arr is [7, 3, 5, 2, -4, 8, 11], then there are actually two pairs that sum to the number 7: [5, 2] and [-4, 11]. 
Your program should return all pairs, with the numbers separated by a comma, in the order the first number appears in the array. 
Pairs should be separated by a space. So for the example above, your program would return: 5,2 -4,11

If there are no two numbers that sum to the first element in the array, return -1



def ArrayChallenge(arr):
  answer = []
  comb = []
  make_number = arr[0]
  array = arr[1:]
  array_len = len(array)

  for num in array:
    if num in sum(comb, []):
      continue
    if make_number - num in array:
      remain = array[array.index(make_number - num)]
      comb.append([num, remain])

  if comb:
    for a,b in comb:
      answer.append(str(a)+','+str(b))
    return ' '.join(answer)
  else:
    return -1

# keep this function call here 
print(ArrayChallenge(input()))
