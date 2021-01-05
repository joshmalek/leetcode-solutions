# Link: https://www.pramp.com/challenge/pK6A4GA5YES09qKmqG33
def find_largest_smaller_key(self, num):
  key = -1
  rootNode = self.root
  while(rootNode):
    if(rootNode.key < num):
      key = rootNode.key
      rootNode = rootNode.right
    else:
      rootNode = rootNode.left

  return key
