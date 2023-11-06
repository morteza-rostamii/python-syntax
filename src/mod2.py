from functools import reduce


def chap1():
  res = None

  # get user input
  #res = input('please enter something: ')

  # conditionals

  age = 19

  if (age == 18):
    res = 'you are 18'
  elif (age > 18):
    res = 'you are older than 18'
  else:
    res = 'you are younger than 18'

  # data types:

  # even primitive are objects
  num: int = 23
  res = type(num) # <class 'int'>

  print(res)

# about functions 
def funcTut():
  res = None

  # return multiple values from a function
  def returnMulti(a: int, b: int):
    sum = a + b
    sub = a - b

    return sum, sub

  res = returnMulti(2, 2)

  # retunrs a tuple:  (4, 0)
  #print(type(res))

  #---------------------------------------

  # key-word args

  def createUser(username: str, age: int):
    pass
    #print(f'username: {username} and age: {age}')

  createUser(age=20, username='ali')

  #---------------------------------------

  # defautl args
  def defaultArgs(a: int, b: int=10):
    return a * b

  res = defaultArgs(2) # 20

  #---------------------------------------

  # variable-length arguments
  # get multiple args
  def sumup(*args):
    total = 0

    for x in args:
      total += x
    
    return total

  res = sumup(2, 2, 2, 2) #8

  #---------------------------------------

  # Anonymous/Lambda Function

  # add to multiple of 10
  def addToMultiple(a: int):
    num = a * 10

    return lambda b: b + num

  func = addToMultiple(a=2)

  res = func(b=5) # 25

  #---------------------------------------

  # some build-in functions

  # filter()

  nums = [-10, 5, 12, -78, 6, -1, -7, 9]

  # return all positives
  # args: condition_function, iterable
  positives = filter(lambda x: x > 0, nums)

  # returns: an object! so: convert to list
  res = list(positives) # [5, 12, 6, 9]
   
  #---

  # map()

  prices = [10, 20, 30, 40, 50]

  # square each element
  res = list(map(lambda x: x ** 2, prices))
  # [100, 400, 900, 1600, 2500]

  #---

  # reduce() =: import from functools

  # create 1 value out of all values: for example: sum

  counts = [1, 2, 3, 4, 5, 6]

  # args: accumulator, current value
  # return value goes to accum
  def sumIt(accum:int, current:int):
    print(accum)
    return accum + current

  res = reduce(sumIt, counts)

  print(res)

# about dictionaries
def dicTut(): 
  res = None

  #---------------------------------------
  
  # define a dictionary
  myDic: dic = {
    "username": 'sara',
    "email": 'sara@gmail.com'
  }

  res = myDic

  #---------------------------------------

  print(res)

def main():
  print('--------------------')
  #chap1()
  dicTut()
  #funcTut()
  print('--------------------')

if __name__ == '__main__':
  main()
