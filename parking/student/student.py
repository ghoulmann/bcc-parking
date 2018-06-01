import string
import random

#def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
#    return ''.join(random.choice(chars) for _ in range(size))

from random import randint
class Student(str):
    def __init__(self, str):
        self.grade = randint(9, 12)
        # self.id = self.id_generator(self)
        self.name = str
        self.qualifier = {}
        self.qualifier['hardship'] = randint(0,1)
        self.qualifier['internship'] = randint(0,1)
        self.qualifier['d_enrollment'] = randint(0,1)
        self.qualifier['weekday_job'] = randint(0,1)
        self.qualifier['distance'] = randint(0,1)
        self.qualifier['athletics'] = randint(0,1)
        self.qualifier['athletics_carpool'] = randint(0,1)
        self.qualifier['athletics_captain'] = randint(0,1)
        self.qualifier['sga'] = randint(0,1)
        self.qualifier['extracurricular'] = randint(0,1)
        self.qualifier['gpa'] = randint(0,1)
        self.qualifier['attendance'] = randint(0,1)
        self.qualifier['service'] = randint(0, 1)
        self.insurance = True
        self.license = True
        self.registration = True
        self.parent_letter = True
        self.raw_score = (sum(self.qualifier.values())) * 2
	self.scaled_score = self.expo_bloom(self.qualifier, self.raw_score)

    def expo_bloom(self, dictionary, multiplier):
        if dictionary['hardship']:
	        self.scaled_score = multiplier ** 11
            self.decision = 'hardship'
        elif dictionary['internship']:
	        self.scaled_score = multiplier ** 10
            #self.decision = 'internship'
        elif dictionary['d_enrollment']:
            self.scaled_score = multiplier ** 9
            #self.decision = 'dual enrollment'
        elif dictionary['weekday_job']:
            #self.decision = 'weekday job'
            self.scaled_score = multiplier ** 8
        elif dictionary['athletics_carpool']:
            self.scaled_score = multiplier ** 7
            #self.decision = 'athletics carpool'
        elif dictionary['athletics_captain']:
            self.scaled_score = multiplier ** 6
            #self.decision = 'team captain'
        elif dictionary['athletics']:
            self.scaled_score = multiplier ** 5
            #self.decision = 'team athlete'
        elif dictionary['distance']:
            self.scaled_score = multiplier ** 4
            #self.decision = 'distance'
        elif dictionary['sga']:
            self.scaled_score = multiplier ** 3
            #self.decision = "student govenment"
        elif dictionary['extracurricular']:
            self.scaled_score = multiplier ** 2
            #self.decision = 'extracurricular activities'


	else:
	     self.scaled_score = multiplier
        return self.scaled_score

    def id_generator(self, size=6, chars=string.ascii_uppercase + string.digits):
         return ''.join(random.choice(chars) for _ in range(size))    
    