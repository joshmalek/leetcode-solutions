#Link: https://www.pramp.com/challenge/W5EJq2Jld3t2ny9jyZXG
import string 
from collections import OrderedDict
def word_count_engine(document):
  no_punc = ""
  for c in document:
    if(c not in string.punctuation):
      no_punc += c
  word_split = no_punc.split()
  for i in range(0,len(word_split)):
    word_split[i] = word_split[i].lower()
  count = OrderedDict()
  for word in word_split:
    count[word] = word_split.count(word)
  count = OrderedDict(sorted(count.items(), key=lambda kv: kv[1], reverse=True))
  ret = []
  for key in count:
    ret.append([key,str(count[key])])
  print(ret)
  return ret
document = "Practice makes perfect. you'll only get Perfect by practice. just practice!"
word_count_engine(document)