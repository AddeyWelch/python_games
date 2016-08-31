import random


class Gladiator:
    """ A person with strong attributes such as powerful rage and healing. """

    def __init__(self, health, rage, low_d, high_d):
        self.health = health
        self.rage = rage
        self.low_d = low_d
        self.high_d = high_d

    def attack(self, other):
        hits = random.randint(self.low_d, self.high_d)
        if self.rage > random.randint(0, 100):
            hits *= 2
            self.rage = 0
        else:
            self.rage += 15
        # deliever the blow
        other.health -= hits

    def heal(self):
        if self.health > 0 and self.health < 100:
            if self.rage >= 10:
                self.health += 5
                self.rage -= 10

    def is_dead(self):
        if self.health < 1:
            return True
        else:
            return False

    def __str__(self):
        return '{0}, {1}, {2}, {3}'.format(self.health, self.rage, self.low_d,
                                           self.high_d)

    def __repr__(self):
        return 'Gladiator({0}, {1}, {2}, {3})'.format(self.health, self.rage,
                                                      self.low_d, self.high_d)
