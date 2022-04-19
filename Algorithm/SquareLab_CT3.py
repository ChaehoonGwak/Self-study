String Challenge
Have the function StringChallenge(sen) take the sen parameter being passed and return the longest word in the string. 
If there are two or more words that are the same length, return the first word from the string with that length. 
Ignore punctuation and assume sen will not be empty. Words may also contain numbers, for example "Hello world123 567"

Examples
Input: "fun&!! time"
Output: time
Input: "I love dogs"
Output: love



import re

def StringChallenge(sen):
  answer = ''
  words = sen.split(' ')
  maxlen = 0
  
  for word in words:
    w = re.sub('[^a-zA-z0-9]', '', word)
    l = len(w)
    if l > maxlen:
      maxlen = l
      answer = w

  return answer

# keep this function call here 
print(StringChallenge(input()))
