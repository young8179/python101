'''3. Friend counter
Using the dictionary from the Nested dictionaries exercise above,
write a function countFriends() that accepts a dictionary as an argument 
and returns a new dictionary that includes a new key friends_count:
'''


ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

def countFriends(ramit_dict):
    ramit_dict['friends_count'] = len(ramit_dict['friends'])
    return ramit

result = countFriends(ramit)
print(result)