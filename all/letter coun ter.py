from time import *
import string
times = perf_counter()
text = open('HW.txt')
letters = string.ascii_lowercase
for i in text:
  text_lower = i.lower()
  text_nospace = text_lower.replace(" ", "")
  text_nopunctuation = text_nospace.strip(string.punctuation)
  for a in letters:
    if a in text_nopunctuation:
      num = text_nopunctuation.count(a)
      print(a, num)
print(perf_counter() - times)
