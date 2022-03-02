class Hero:
    def __init__(self,name,place,weapon):
        self.name = name
        self.place = place
        self.weapon = weapon
    def introduce(self):
        return print("Hi, I'm {0} from {1}.".format(self.name,self.place))
    def attack(self):
        return print("Attack with {}".format(self.weapon))

class Ironman(Hero):
    def attack(self):
        return print("I'm... Iron Man.")
class Spiderman(Hero):
    def attack(self):
        return print("Psst!!!")
    def web_swing(self):
        return print("Hi, everyone!")
class Thor(Hero):
    def attack(self):
        return print("I'm Thor, god of thunder!")

hero = Hero("Doctor Strange","New York","magic")
hero.introduce()
hero.attack()

ironman = Ironman("Tony","Long Island","iron suit")
spiderman = Spiderman("Peter","Queens","web")
thor = Thor("Thor","Asgard","hammer")

ironman.introduce()
ironman.attack()

spiderman.introduce()
spiderman.attack()
spiderman.web_swing()

thor.introduce()
thor.attack()