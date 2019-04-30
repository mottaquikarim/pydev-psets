"""
Weddings III - Record Shower & Bachelorette RSVP
"""

# Create two methods in Bridesmaid to record a the bridesmaid's rsvp to the bridal shower and the bachelorette party. You can call them "record_shower_rsvp()" and "record_bachelorette_rsvp()". They will work just like the general "record_rsvp()" except there will be no plus ones or diet questions. Their rsvp answers should be stored in instance attributes with the same name (i.e. shower_rsvp & bachelorette_rsvp).

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
        self.invite_sent = False
        self.diet = None
        self.rsvp = None
        self.plus_one = None
        self.plus_one_name = None
        self.plus_one_diet = None
        self.shower_rsvp = None
        self.bachelorette_rsvp = None

    def record_shower_rsvp(self, rsvp):
        if rsvp == 'no' or rsvp == 'No':
            self.shower_rsvp = False
        elif rsvp == 'yes' or rsvp == 'Yes':
            self.shower_rsvp = True
        return None

    def record_bachelorette_rsvp(self, rsvp):
        if rsvp == 'no' or rsvp == 'No':
            self.bachelorette_rsvp = False
        elif rsvp == 'yes' or rsvp == 'Yes':
            self.bachelorette_rsvp = True
        return None


angelika = Bridesmaid('Angelika Vasilieva', 2019352087)

# Angelika can't make it to the bridal shower, but will be at the bachelorette party.
angelika.record_shower_rsvp('no')
print(angelika.shower_rsvp)

angelika.record_bachelorette_rsvp('Yes')
print(angelika.bachelorette_rsvp)