from classes.game import Person,bcolors
from classes.magic import Spell
from classes.inventory import Item
import random



print("\n\n")
print(bcolors.OKBLUE  + bcolors.BOLD+"Welcome to Game of battle"+bcolors.ENDC)
print("\n\n")







#Create black magic
fire=Spell("Fire",100,600,"black")
thunder=Spell("Thunder",124,700,"black")
blizzard=Spell("Blizzard",140,800,"black")
meteor=Spell("Meteor",180,900,"black")
quake=Spell("Quake",200,999,"black")


#Create white magic
cure=Spell("Cure",10,120,"white")
health=Spell("Health",20,200,"white")


#Create some items
potion = Item("Potion","potion","heals 50 HP",50)
hipotion = Item("Hi-Potion","potion","Heals 100 HP",100)
superpotion = Item("Super-potion","potion","Heals 200 HP ",200)
elixer = Item("Elixer","elixer","Fully restored hp/mp",1000)
hielixer = Item("Hi=Elixer","elixer","Fully restores party's gp/mp",1000)


#Heavy explosives
grenade=Item("Grenade","attack","Deals 500 damage",500)

player_spells=[fire,thunder,blizzard,meteor,cure,health]
player_items=[{"item":potion,"quantity": 15},{"item":hipotion,"quantity": 5},{"item":superpotion,"quantity": 5},
              {"item":elixer,"quantity": 5},{"item":hielixer,"quantity": 5},{"item":grenade,"quantity": 5}]


#Instantiate the players
player1 = Person("Peter:" ,3600 ,400 ,60 ,34 ,player_spells ,player_items)
player2 = Person("Valos:",4600,400,60,34,player_spells,player_items)
player3 = Person("Bruce:",4200,400,60,34,player_spells,player_items)

enemy1 = Person("Kratos",9000,420,300,20,[],[])
enemy2 = Person("Thanos",1200,150,550,200,[],[])
enemy3 = Person("Ronan",1500,180,215,235,[],[])

players = [player1,player2,player3]
enemies = [enemy1,enemy2,enemy3]

running = True

print(bcolors.FAIL + bcolors.BOLD + "THE ENEMY ATTACKS" + bcolors.ENDC)
while running:
    print("======================================")

    for player in players:
        player.get_stats()
    print("\n")
    for enemy in enemies:
        enemy.get_enemy_stats()
    for player in players:

        player.choose_action()
        choice=input("Enter your choice:")
        index=int(choice) - 1
        if index==0:
            dmg=player.generate_damage()
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(dmg)
            print("You attacked for "+ str(dmg)+" to "+enemies[enemy].name)
            if enemies[enemy].get_hp()==0:
                print(enemies[enemy].name+"Died")
                del enemies[enemy]

        elif index==1:
            player.choose_magic()
            magic_choice=(int(input("Enter your choice:"))-1)
            if magic_choice==-1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg=spell.damage_generate()
            cost=spell.cost

            current_mp=player.get_mp()

            if spell.cost> current_mp:
                print(bcolors.FAIL  +"You dont have enough mp"+bcolors.ENDC)
                continue

            player.reduce_mp(spell.cost)

            if spell.type=='white':
                player.heal(magic_dmg)
                print(bcolors.OKBLUE+ "\n"+ spell.name+" heals for"+ str(magic_dmg)+'HP'+bcolors.ENDC)

            elif spell.type=='black':
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(magic_dmg)

                print("You attacked for "+str(magic_dmg)+"with"+str(spell.name)+"spell"+" to "+enemies[enemy].name)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name + "Died")
                    del enemies[enemy]

        elif index==2:
            player.choose_item()
            item_choice=int(input("Choose items-"))-1
            if item_choice==-1:
                continue

            item=player.items[item_choice]["item"]
            if player.items[item_choice]["quantity"]==0:
                print(bcolors.BOLD+"The spell has exhausted"+bcolors.ENDC)
                continue

            player.items[item_choice]["quantity"]-=1



            if item.type=="potion":
                player.heal(item.prop)
                print(bcolors.OKBLUE+"\n"+str(item.name)+" heals for"+str(item.prop)+" HP "+bcolors.ENDC)
            elif item.type=="elixer":
                if item.name=="Hi-Elixer":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp

                player.hp=player.maxhp
                player.mp=player.maxmp
                print(bcolors.OKBLUE + "\n" + str(item.name)+" fully restored mp and hp"+bcolors.ENDC)
    #Renews ability of player.

            elif item.type=="attack":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item.prop)
                print(bcolors.FAIL+"\n"+item.name+"deals with damage of"+str(item.prop)+" to "+enemies[enemy].name)
                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name + " Died! R.I.P")
                    del enemies[enemy]




    enemy_choice=1
    target=random.randrange(0,3)

    enemy_dmg=enemies[0].generate_damage()

    players[target].take_damage(enemy_dmg)
    print("Enemy attacks for "+str(enemy_dmg))


    defeated_enemies = 0
    for enemy in enemies:
        if enemy.get_hp()==0:
            defeated_enemies+=1



    defeated_players=0
    for player in players:
        if player.get_hp()==0:
            defeated_players+=1

    if defeated_enemies==3:
        print(bcolors.OKGREEN +"You win",bcolors.ENDC)
        running=False

    elif defeated_players==3:
        print(bcolors.FAIL+"Your enemies defeated you!"+bcolors.ENDC)
        running=False
