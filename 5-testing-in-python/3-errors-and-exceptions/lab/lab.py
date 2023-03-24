my_list = [27, 5, 9, 6, 8]

def RemoveValue(myVal):
  my_list.remove(myVal)
  return my_list

print(RemoveValue(27)) # [5, 9, 6, 8]
print(RemoveValue(27)) # ValueError: list.remove(x): x not in list


### To fix the above error messaging and pre-empt this error:

def RemoveValueFixed(myVal):
  if myVal not in my_list:
    raise ValueError("Value must be in the given list")
  else:
    my_list.remove(myVal)
  return my_list

print(RemoveValueFixed(27))
print(RemoveValueFixed(27)) # ValueError: Value must be in the given list


#############################################################################################################################
#############################################################################################################################


my_word_list = ['east', 'after', 'up', 'over', 'inside']

def OrganizeList(myList):
    myList.sort()
    return myList

print(OrganizeList(my_word_list)) # ['after', 'east', 'inside', 'over', 'up']

my_new_list = [6, 3, 8, "12", 42]
print(OrganizeList(my_new_list)) # TypeError: '<' not supported between instances of 'str' and 'int'


### To fix the above error messaging and pre-empt this error:

def OrganizeListFixed(myList):
  for item in myList:
    assert type(item) == int, "Word list must be a list of strings" # Assert keyword verifies if a conditional expression is true; if false, raises AssertionError (produce a message when a conditional is false)
  myList.sort()
  return myList

print(OrganizeListFixed(my_new_list)) # AssertionError: Word list must be a list of strings


#############################################################################################################################
#############################################################################################################################

import random

participants = ['Jack','Jill','Larry','Tom']

'''Takes a list of participants, assigns each a random number from 1 to 9, and stores this information in a dictionary with the participant name as the key
It then returns True if Larry was assigned the number 9 and False if this was not the case'''
def Guess(participants):
  my_participant_dict = {}
  for participant in participants:
    my_participant_dict[participant] = random.randint(1, 9)
  if my_participant_dict['Larry'] == 9:
    return True
  else:
    return False
  
print(Guess(participants)) # False

new_participants = ['Cathy','Fred','Jack','Tom']
print(Guess(new_participants)) # KeyError: 'Larry'


### To fix the above error messaging and pre-empt this error:

def GuessFixed(participants):
  my_participant_dict = {}
  for participant in participants:
    my_participant_dict[participant] = random.randint(1, 9)
  try:
    if my_participant_dict['Larry'] == 9:
      return True
  except KeyError:
    return None
  else:
    return False

print(GuessFixed(new_participants)) # None