import random
class bcolors:                          #This is to display colors in terminal
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:                                    #displaying measurable quantity of things possessed by player
    def __init__(self,hp,mp,atk,df,magic):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkh = atk+10
        self.atkl = atk-10
        self.df = df
        self.magic = magic
        self.actions = ["attack","magic"]

    def generate_damage(self):                      #Generating random damage by hitting
        return random.randrange(self.atkl,self.atkh)
    def spell_generate_damage(self,i):              #This is because spell are in form of array so i represents index number
        mgl = self.magic[i]["dmg"] - 5
        mgh = self.magic[i]["dmg"] + 5
        return random.randrange(mgl,mgh)
    def take_damage(self,dmg):
        self.hp -= dmg
        if self.hp<0:
            self.hp=0
        return self.hp
    def heal(self):
        self.hp+=dmg
        if self.hp>self.maxhp:
            self.hp=self.maxhp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self,cost):
        self.mp -= cost

    def get_spell_name(self,i):
        return self.magic[i]["name"]

    def get_spell_cost(self,i):
        return self.magic[i]["cost"]

    def choose_action(self):
        i=1
        print("Actions")
        for item in self.actions:
            print(str(i)+':'+item)
            i+=1

    def choose_magic(self):
        i=1
        print("Magic")
        for spell in self.magic:
            print(str(i)+':'+spell['name'] , '(cost' , str(spell["cost"])+')')
            i+=1

