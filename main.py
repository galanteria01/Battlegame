from classes.game import Person,bcolors


magic=[{'name':'fire','cost': 10,'dmg': 60}
      ,{'name':'thunder','cost': 15,'dmg': 80}
      ,{'name': 'wind','cost': 18,'dmg': 100}]

player = Person(600,65,60,34,magic)
enemy = Person(1200,65,30,20,magic)

running = True

print(bcolors.FAIL + bcolors.BOLD + "THE ENEMY ATTACKS" + bcolors.ENDC)
while running:
    print("======================================")
    player.choose_action()
    choice=input("Enter your choice:")
    index=int(choice) - 1
    if index==0:
        dmg=player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for "+ str(dmg) +" Enemy hp: "+str(enemy.get_hp()))
    elif index==1:
        player.choose_magic()
        magic_choice=(int(input("Enter your choice:"))-1)
        magic_dmg=player.spell_generate_damage(magic_choice)
        spell = player.get_spell_name(magic_choice)
        cost = player.get_spell_cost(magic_choice)
        current_mp=player.get_mp()

        if cost> current_mp:
            print(bcolors.FAIL  +"You dont have enough mp"+bcolors.ENDC)
            continue

        player.reduce_mp(cost)

        enemy.take_damage(magic_dmg)
        print(bcolors.OKBLUE +player.get_spell_name(magic_choice)+bcolors.ENDC)
        print("You attacked for "+str(magic_dmg)+"Enemy's hp:"+str(enemy.get_hp()))

    enemy_choice=1

    enemy_dmg=enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for "+str(enemy_dmg) + " Player hp: "+ str(player.get_hp()))

    if enemy.get_hp()==0:
        print(bcolors.OKGREEN +"You win",bcolors.ENDC)
        running=False
    elif player.get_hp()==0:
        print(bcolors.FAIL+"You loose"+bcolors.ENDC)
        running=False
