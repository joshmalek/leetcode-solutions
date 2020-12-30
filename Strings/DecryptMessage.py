#Link: https://www.pramp.com/challenge/8noLWxLP6JUZJ2bA2rnx

def decrypt(word):
  split_word = list(word)
  if(len(split_word) == 0):
    return "" 
  decrypted_word = []
  if(split_word[0] == 'a'):
    decrypted_word.append('z')
  else:
    first_letter = chr(ord(split_word[0])-1)
    decrypted_word.append(first_letter)
  for i in range(1,len(split_word)):
    diff = ord(split_word[i])-ord(split_word[i-1])
    while(diff < 97):
      diff+=26
    letter = chr(diff)
    decrypted_word.append(letter)
  return "".join(decrypted_word)