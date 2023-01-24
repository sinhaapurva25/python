class Enemy:
    life = 3
    def attack(self): #use something from the same class
        print("ouch")
        self.life = self.life-1
    def checkLife(self):
        if (self.life) <=0:
            print("i am dead")
        else:
            print(str(self.life)+" life left")
    def anotherfunc(x):
        return x

enemy1= Enemy()
enemy2= Enemy()

print("Enemy1")
enemy1.attack()
enemy1.attack()
enemy1.checkLife()
print(enemy1.anotherfunc(5))

print("Enemy2")
enemy2.attack()
enemy2.checkLife()