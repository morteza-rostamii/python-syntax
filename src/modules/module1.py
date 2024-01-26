from typing import List
from typing import Tuple
import copy
import logging

def aboutString(): 

  # strings next to each other auto concate
  text: str = 'ali' 'reza'

  # strings are indexed
  cha1: str = text[0] # a

  username: str = "angelina"
  # slice
  # -1 index is excluded
  res: str = username[0:-1] # angelin

  # from: 0 to end
  res = username[0:] # angelina

  # from 0 to -1
  res = username[:-1]

  # the whole thing
  res = username[:] # angelina

  #==============================

  # reference or value copy

  a: List[int] = [1, 2, 3]
  b = a

  a[0] = 12

  # point to the same memory address
  a_memory_address = id(a) # 139710357175104
  b_memory_address = id(b) # 139710357175104

  #===============================

  # shallow copy:

  arr1: List[int] = [4, 5, 6]
  shallow_copy: List[int] = copy.copy(arr1)

  arr1[0] = 90
  
  #==============================

  # deep copy:

  # meaning: copy the values of nested objects

  ar1: List[any] = [1, 2, ['a', 'b']]
  ar2: List[any] = copy.deepcopy(ar1)

  ar1[2][0] = 'google'

  # [1, 2, ['google', 'b']] [1, 2, ['a', 'b']]

  # f-string
  name: str = 'sara'
  fool: str = F"your name is: {name}"

  print(fool)

def aboutControlFlow():

  username: str = 'Asara lover'
  message: str = ''

  if len(username) < 5:
    message = "username must be more than 5 chars"
  elif username[0].isupper():
    message = "username must be lowercase"
  elif username.startswith('a'):
    message = "username can't starts with 'a'"
  else:
    message = "i love this username"

  # range function
  
  # start, stop, step
  # stop: is not included
  #for i in range(0, 5, 1):
    #print(i)

  # create a list and loop through it 
  scores: List[float] = list(range(10))
  names: List[str] = list(map(lambda x: 'ali', scores))

  #================================

  # for & while loops =: have else clause

  # else: runs after loop is done
  # if: break out of the loop =: else never runs

  """
  for i in range(1, 5):
    for j in range(1, 2):
      print(i, j)
      # if i % j == 0:
      #   print("even")
      #   break
    
    else:
      print("runs at end of each i loop")
  
  """

  #================================
      
  # match statement

  status: int = 500
  msg: str = ""
   
  match status:
    case 400: 
      msg = "bad request"
    case 404 | 500:
      msg = "not found"
    # default case
    case _:
      msg = "somthing else happend"

  print(msg)

def aboutList():
  
  # list comprehension
  fruits: List[str] = ["apple", "orange", "banana", "kiwi", "mango"]

  # create a list of all items that have letter 'a'
  newList: List[str] = [x for x in fruits if "a" in x]

  # print([item for item in fruits if "a" in item])

  # create a new list: 0 to 9
  numbers: List[int] = [x for x in range(10)]

  # numbers lower than 5
  numbers = [x for x in range(10) if x < 5]
  # [0, 1, 2, 3, 4]

  # do some thing to the result of each iteration
  results: List[str] = [current.upper() for current in fruits] 
  # ['APPLE', 'ORANGE', 'BANANA', 'KIWI', 'MANGO']



  print(results)

def aboutTuples():
  result: any = None

  # ordered
  # unchangeable: can't add or remove items
  # allow duplicate values
  # indexed
  
  the_tuple: Tuple(str) = ("ali", "rezq", "sara")

  #result = the_tuple

  # result = len(the_tuple)

  # tuple with one item =: needs a comma
  one_item = ("love", )

  #result = one_item

  # create tuple using constructor
  my_tuple: Tuple(any) = tuple(("whatever", 34))

  # result = my_tuple 

  # access tuple item
  result = my_tuple[0]

  # check if item is in tuple
  if 34 in my_tuple:
    result = "yes!!"

  # convert tuple to list and change it's values
  
  names: Tuple(str) = ("sara", "john", "ali")

  namesList: List[str] = list(names)

  namesList[0] = "angelina"

  # convert back to tuple
  names = tuple(namesList)

  result = names

  #-=============================

  # merge tuples 

  tuple_one = ("bombs", "weapons", "airplanes")
  tuple_two = ("love", "money")

  result = tuple_one + tuple_two

  #=============================
  
  # unpack tuple

  cities = ("new york", "tehran", "berlin")

  (city1, city2, city3) = cities

  result = city2

  # get the rest

  (city1, *rest) = cities

  result = rest # ['tehran', 'berlin']

  print(result)

def aboutSet():
  result = None

  # unordered, unchangeable*, and un-indexed
  # no duplicate
  # can add and remove new items
  # 1 and True =: are duplicate
  # 0 and False =: are also duplicate

  cars = {"bmw", "mvm", "benz", "toyota", "bmw"}
  another_set = {"google", "alexa"}

  # add item
  cars.add("love")

  # merge
  cars.update(another_set)

  # remove
  # if: element not in set throws exception
  try:
    cars.remove("bmw")
  except Exception as error:
    print('-------')
    #print("Error happened:: ", error)
    logging.error("error: ", exc_info=True)
  else: 
    print("no error!")
  finally:
    print('runs anyways!')

  result = cars

  print(result)

def main():
  print("================================\n\n")
  #aboutString()
  #aboutControlFlow()
  #aboutList()
  #aboutTuples()
  aboutSet()
  print("\n\n================================")

if __name__ == '__main__':
  main()


