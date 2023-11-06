
# nice print format
from pprint import pprint

# python datatypes
def data_types():
  res: any = None
  # python datatypes

  # integer
  num: int = 12
  # fload
  num2: float = 23.44

  # string
  username: str = 'love'

  # boolean
  is_true: bool = True # or False

  # list 
  nums: list = [1, 2, 3, 4, 5]

  # tuple:
  # each element is immutable, can't be changed
  scores = (1.3, 4.5, 6.4)

  # error!!
  # scores[1] = 'ali'

  # dictionary
  # unordered collections of key-value pairs
  user: dict = {
    'id': '0',
    'username': 'sarah',
    'age': 23,
    'email': 'sarah@gmail.com'
  }

  # unordered list of items that can't be repeated
  balls: set = {1, 3, 5, 6, 6} # {1, 3, 5, 6}

  # class/object

  class Animal:
    # constructor
    def __init__(self, id: str, name: str):
      self.id = id
      self.name = name

  # create instance object
  bear: Animal = Animal('0123', 'bear')

  # print object atributes
  #print(vars(bear))
  pprint(vars(bear))

  # None
  nothing: None = None

  res = nothing
  print(res)

# operators
def operators():
  res: any = None

  # math operators

  res = 2 + 2 # 4
  res = 4 - 3 # 1
  res = 3 * 9 # 27
  res = 8 / 2 # 4 
  res = 8 % 2 # 0
  # 2^2
  res = 2 ** 2 # 4

  # division
  res = 5 / 3 # 1.6666666666666667
  
  # floor division:
  res = 7 // 2 # 3

  #----------------------------------

  # assignment ope.

  # = 
  # +=
  # -= 
  # *= 
  # /=
  # //=
  # %=
  # **=

  #----------------------------------

  # comparison ope.

  if (2 == 2):
    print('2 = 2')

  # != > < >= <=

  #----------------------------------

  # logical operators

  if (True and False):
    print('we go to the party!!')

  if (True or False):
    print('we go to the zoo!!')

  is_auth: bool = False

  if (not is_auth): 
    print('user is is not auth!!')

  #----------------------------------

  # identity operators: (is and is not)
  # comapre if opjects are the same reference wise

  user1: str = 'ali'
  user2: str = user1
  user3: str = 'ali'

  if (user2 is user1):
    print('the same objects!!')# runs!!

  # this returns True =: if: variables have the same value.
  """
  # cause:
  This is because Python optimizes the storage of strings by using a technique called interning. Interning means that Python will reuse the same string object for multiple variables if they have the same value and length. This saves memory and improves performance.
  # not guaranteed!!!:
  However, interning is not guaranteed for all strings. It depends on how the strings are created and what values they have. For example, if you create a string using an expression or a function, it will not be interned. Also, if the string is too long or contains spaces or special characters, it will not be interned.
  """
  if (user1 is user3):
    print('user1 is user3!!') 

  # get the memory location
  #print(id(user1), id(user2), id(user3))
  # 140620070849968 140620070849968 140620070850160

  #----------------------------------

  # Membership Operators

  # in and not in
  # check if an element exist 

  students: str = ['reza', 'sara', 'angelina']

  res = 'reza' in students # True

  #----------------------------------

  #----------------------------------

  #----------------------------------

  print(res)

# list
def listTut():
  res: any = None

  fruits: list = ['banana', 'orange', 'cherry', 'apple']

  # access list
  res = fruits[0]

  # assign new item
  fruits[0] = 'grapes'

  res = fruits
  # ['grapes', 'orange', 'cherry', 'apple']

  # get length of list
  res = len(fruits)# 4

  # get type
  res = type(fruits)# <class 'list'>

  # access from end
  res = fruits[-1]

  # get a range of items inside a new list
  # inx[3] not included
  res = fruits[1:3]
  # ['orange', 'cherry']

  # from inx[0] to 2
  res = fruits[:2] # ['grapes', 'orange']

  # from inx[2] to end
  res = fruits[2:] # ['cherry', 'apple']

  # negative range: start to end
  res = fruits[:-1] # ['grapes', 'orange', 'cherry']

  # ---------------------------------------------

  # check if: item exist inside of the list
  if ('apple' in fruits):
    res = 'apple is in!!'

  # ---------------------------------------------

  people = ['ali', 'sara']
  friends = ['jen', 'ross', 'joey']

  # insert item at specific index
  # shift the rest items to right
  friends.insert(1, 'angelina')
  # ['jen', 'angelina', 'ross', 'joey']

  # push item to the end
  friends.append('reza')

  # merge 2 lists
  # adds it to end of friends
  friends.extend(people)

  # remove the first occurence
  friends.remove('ali')

  # pop last item
  print(friends.pop()) # sara

  # pop a specific index
  print(friends.pop(0))# jen

  # delete element
  del friends[0]

  # delete list: remove from memory
  del friends

  # res = friends

  # ---------------------------------------------

  # loop a list

  players: list = ['cap', 'jen', 'ben', 'ali']

  #res = range(len(players)) # 0 to 4

  # loop: 0 to 3
  #for x in range(len(players)):
    #print(players[x])

  #for x in players:
    #print(x)

  # ---------------------------------------------

  # list comprehension
  #[print(x) for x in players]

  # return all items containing 'a'
  new_list = [x for x in players if 'a' in x]

  res = new_list # ['cap', 'ali']

  # only numbers less than 5
  new_nums = [(x + 1) for x in range(10) if x < 5]
  # [0, 1, 2, 3, 4]

  # do any thing with each output
  # expression can be also condition: (x if x != 'h')
  new_nums = [(x + 1) for x in range(10) if x < 5]
  # [1, 2, 3, 4, 5]

  res = new_nums

  # ---------------------------------------------

  print(res)

# list part 2
def listTut2():
  res = None

  # sort list 

  # sort alphanumerically ascending
  thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
  thislist.sort()

  nums = [12, 3, 67, 1]

  # sort numerically (acending)
  nums.sort()

  res = nums # [1, 3, 12, 67]

  # descending
  nums.sort(reverse=True)
  
  res = nums # [67, 12, 3, 1]

  # ---------------------------------------------

  # deep copy a list
  new_nums = nums.copy()

  res = nums is new_nums # False
  res = new_nums

  # ---------------------------------------------

  # concate 2 list
  list1 = [1, 2]
  list2 = [3, 4]

  res = list1 + list2 # [1, 2, 3, 4]

  # empty a list into other
  list1.extend(list2)

  res = list1

  # ---------------------------------------------
  # ---------------------------------------------
  # ---------------------------------------------
  # ---------------------------------------------
  # ---------------------------------------------

  print(res)

def main():
  print('============================')
  #data_types()
  #operators()
  #listTut()
  #listTut2()

  
  print('============================')

#main()
