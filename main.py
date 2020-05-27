from classes.game import Person,bcolors
from classes.magic import Spell
from classes.inventory import Item


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
player1 = Person("Peter:",3600,150,60,34,player_spells,player_items)
player2 = Person("Valos:",4600,144,60,34,player_spells,player_items)
player3 = Person("Bruce:",4200,132,60,34,player_spells,player_items)
enemy = Person("Kratos",9000,2420,3000,20,[],[])

players=[player1,player2,player3]

running = True

print(bcolors.FAIL + bcolors.BOLD + "THE ENEMY ATTACKS" + bcolors.ENDC)
while running:
    print("======================================")

    for player in players:
        player.get_stats()
    print("\n")
    enemy.get_enemy_stats()
    for player in players:

        player.choose_action()
        choice=input("Enter your choice:")
        index=int(choice) - 1
        if index==0:
            dmg=player.generate_damage()
            enemy.take_damage(dmg)
            print("You attacked for "+ str(dmg) +bcolors.OKGREEN+" Enemy hp: "+str(enemy.get_hp())+bcolors.ENDC)
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
                enemy.take_damage(magic_dmg)

                print("You attacked for "+str(magic_dmg)+"with"+str(spell.name)+"spell"+bcolors.OKGREEN+"Enemy's hp: "+str(enemy.get_hp())+bcolors.ENDC)
            print(bcolors.FAIL  +"Enemy's hp: "+str(enemy.get_hp())+ bcolors.ENDC)
            print( bcolors.OKBLUE+ "Your mp:" +str(player.get_mp())+bcolors.ENDC)

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
                player.hp=player.maxhp
                player.mp=player.maxmp
                print(bcolors.OKBLUE + "\n" + str(item.name)+" fully restored mp and hp"+bcolors.ENDC)
    #Renews ability of player.

            elif item.type=="attack":
                enemy.take_damage(item.prop)
                print(bcolors.FAIL+"\n"+item.name+"deals with damage of"+str(item.prop))




    enemy_choice=1

    enemy_dmg=enemy.generate_damage()
    player1.take_damage(enemy_dmg)
    print("Enemy attacks for "+str(enemy_dmg) + bcolors.OKGREEN+" Player hp: "+ str(player1.get_hp())+bcolors.ENDC)



    if enemy.get_hp()==0:
        print(bcolors.OKGREEN +"You win",bcolors.ENDC)
        running=False
    elif player1.get_hp()==0:
        print(bcolors.FAIL+"You loose"+bcolors.ENDC)
        running=False
