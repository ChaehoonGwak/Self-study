String Challenge
Have the function StringChallenge(str) take the str parameter being passed and return the first word with the greatest number of repeated letters. 
For example: "Today, is the greatest day ever!" should return greatest because it has 2 e's (and 2 t's) and it comes before ever which also has 2 e's. 
If there are no words with repeating letters return -1. Words will be separated by spaces.

Examples
Input: "Hello apple pie"
Output: Hello
Input: "No words"
Output: -1



from collections import Counter

def StringChallenge(strParam):
  answer = ''
  words = strParam.split(' ')
  max_repeat = 0
  
  for word in words:
    cnt_word = Counter(word)
    repeat = max(cnt_word.values())
    if repeat > max_repeat and repeat > 1:
      max_repeat = repeat
      answer = word

  return answer if max_repeat > 1 else -1

# keep this function call here 
print(StringChallenge(input()))
