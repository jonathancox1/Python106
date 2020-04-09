class Character():
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
    
    def status(self):
        print(f'{self.name}')
        print(f'Health : {self.health}')
        print(f'Strength : {self.strength}')

    def heal(self):
        if self.health <= 100:
            self.health += 5
        else:
            pass
        print(f'{self.name} has been healed')
        print(f'their heath is now {self.health}')


    def attack(self, target):
        print(f'{self.name} is attacking {target.name}')
        target.health -= self.strength
        print(f'{target.name}\'s health has dropped to {target.health}')

    
#Create characters with arugments
dale_cooper = Character('Dale Cooper', 100, 4)
bob = Character('BOB', 100, 10)

#Characters attack one another
dale_cooper.attack(bob)
bob.attack(dale_cooper)

#Display a characters status
bob.status()
dale_cooper.status()

#Character heals health +5
dale_cooper.heal()
dale_cooper.status()

