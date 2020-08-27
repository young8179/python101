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

Ramit_email = ramit['email']
print(Ramit_email)

Ramit_interest = ramit['interests'][0]
print(Ramit_interest)

jasmine_email = ramit['friends'][0]['email']
print(jasmine_email)

jan_interest = ramit['friends'][1]['interests']
print(jan_interest)