"""
Dogs IV - Tricks (CHALLENGE!)
""" 

# Many dogs know how to do common tricks or follow common commands. You could create methods for each trick/command in the Dog parent class, but the problem is that not all dogs know all tricks/commands. 

# However, it would be inefficient to define a custom set of instance methods for tricks/commands every time you instantiate a unique Collie (or SiberianHuskey or Pekingese etc.).

# Find an efficient way to specify which tricks each unique dog knows and to call them. You can use "roll_over", "fetch", "shake_hands", and "spin". Secondly, find a way to teach a dog new trick from this set.

class Dog():
    def __init__(self, name):
        self.name = name
        self.tricks = {'shake_hands': False, 'fetch': False, 'spin': False, 'roll_over': False}

    domesticated = True

    def bark(self):
        print('Woof!')

    def learn_trick(self, trick):
        self.tricks.update({trick: True})

    def shake_hands(self):
      if self.tricks['shake_hands'] == True:
          print('Shake hands? Done - treat please!')
      elif self.tricks['shake_hands'] == False:
                print('Shake hands? I don\'t know that trick.')

    def fetch(self):
      if self.tricks['fetch'] == True:
          print('Fetch? Done - treat please!')
      elif self.tricks['fetch'] == False:
                print('Fetch? I don\'t know that trick.')

    def spin(self):
      if self.tricks['spin'] == True:
          print('Spin? Done - treat please!')
      elif self.tricks['spin'] == False:
                print('Spin? I don\'t know that trick.')
    
    def roll_over(self):
      if self.tricks['roll_over'] == True:
          print('Roll over? Done - treat please!')
      elif self.tricks['roll_over'] == False:
                print('Roll over? I don\'t know that trick.')


class Collie(Dog):
    def __init__(self, name, age, gender, shake_hands = False, fetch = False, roll_over = False, spin = False):
        self.name = name
        self.age = age
        self.gender = gender
        self.tricks = {'shake_hands': shake_hands, 'fetch': fetch, 'spin': spin, 'roll_over': roll_over }

    breed = 'collie'
    temperament = ['devoted', 'graceful', 'athletic', 'intelligent']

    def herd_the_kids(self):
        print('Here are your children!')


class SiberianHusky(Dog):
    def __init__(self, name, age, gender, shake_hands = False, fetch = False, roll_over = False, spin = False):
        self.name = name
        self.age = age
        self.gender = gender
        self.tricks = {'shake_hands': shake_hands, 'fetch': fetch, 'spin': spin, 'roll_over': roll_over }

    breed = 'husky'
    temperament = ['outgoing', 'independent', 'loyal', 'mischevious']

    def pull_sled(self):
        print('I\'m mushing already!')

class Pekingese(Dog):
    def __init__(self, name, age, gender, shake_hands = False, fetch = False, roll_over = False, spin = False):
        self.name = name
        self.age = age
        self.gender = gender
        self.tricks = {'shake_hands': shake_hands, 'fetch': fetch, 'spin': spin, 'roll_over': roll_over }

    breed = 'pekingese'
    temperament = ['affectionate', 'calm', 'loyal']

    def bark(self):
        print('Yap!')


lassie = Collie('Lassie', 3, 'female', fetch = True, spin = True)
aiden = SiberianHusky('Aiden', 5, 'male', fetch = True, roll_over = True, spin = False)
cameron = Pekingese('Cameron', 8, 'female', roll_over = True)


print(f'\n{lassie.name}')
lassie.fetch()
lassie.shake_hands()
lassie.learn_trick('shake_hands')
lassie.shake_hands()

print(f'\n{aiden.name}')
aiden.roll_over()
aiden.spin()
aiden.learn_trick('spin')
aiden.spin()

print(f'\n{cameron.name}')
cameron.roll_over()
cameron.fetch()
cameron.learn_trick('fetch')
cameron.fetch()
