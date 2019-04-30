"""
Weddings II - Record RSVPs
"""

# Create a method in Guest to record a guests's rsvp to your invitation. It should record whether they have any dietary restrictions (e.g. vegetarian, kosher, halal, etc.) and whether they're bringing a plus one. If they are bringing a plus one, it should record the name of the plus one and his/her dietary restrictions if any. These values should be stored in instance attributes.

# Try out this method on at least one instance of Guest and at least one instance of Bridesmaid.

class Guest():
    def __init__(self, name, phone, invite_sent = False):
        self.name = name
        self.phone = phone
        self.invite_sent = invite_sent
        self.diet = None
        self.rsvp = None
        self.plus_one = None
        self.plus_one_name = None
        self.plus_one_diet = None

    def send_invite(self):
        self.invite_sent = True
        return None

    def record_rsvp(self, rsvp, diet, plus_one, plus_one_name = None, plus_one_diet = None):
      if rsvp == 'no' or rsvp == 'No':
        self.rsvp = False
      elif rsvp == 'yes' or rsvp == 'Yes':
        self.rsvp = True
        self.diet = diet
        if plus_one == 'no' or plus_one == 'No':
          self.plus_one = False
        elif plus_one == 'yes' or plus_one == 'Yes':
          self.plus_one = True
          self.plus_one_name = plus_one_name
          self.plus_one_diet = plus_one_diet


class Bridesmaid(Guest):
    def __init__(self, name, phone, invite_sent = False):
        self.name = name
        self.phone = phone
        self.invite_sent = invite_sent
        self.diet = None
        self.rsvp = None
        self.plus_one = None
        self.plus_one_name = None
        self.plus_one_diet = None


klauss = Guest('Klauss Wagner', 3748807716)
michelle = Guest('Michelle Addison', 9205150102)
angelika = Bridesmaid('Angelika Vasilieva', 2019352087)

# Klauss is a vegetarian, and his plus one Vincent keeps halal.
klauss.record_rsvp('yes', 'Vegetarian', 'Yes', 'Vincent Ahmad', 'Halal')
print('Klauss')
print(klauss.rsvp)
print(klauss.diet)
print(klauss.plus_one)
print(klauss.plus_one_name)
print(klauss.plus_one_diet)
print('\n')

# Michelle has no dietary restrictions and is not bringing a plus one.
michelle.record_rsvp('Yes', None, 'No')
print('Michelle')
print(michelle.rsvp)
print(michelle.diet)
print(michelle.plus_one)
print(michelle.plus_one_name)
print(michelle.plus_one_diet)
print('\n')

# Angelika keeps kosher, but her plus one Claude has no dietary restrictions.
angelika.record_rsvp('Yes', 'Kosher', 'yes', 'Claude Dupont', None)
print('Angelika')
print(angelika.rsvp)
print(angelika.diet)
print(angelika.plus_one)
print(angelika.plus_one_name)
print(angelika.plus_one_diet)


