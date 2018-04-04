init python:
    def dungeon_combat(mob_id, sound=None):

        hero_team = hero.team
        len_ht = len(hero.team)
        lvl_ht = hero.team.get_level()

        enemy_team = Team(name="Enemy Team", max_size=3)
        levels = randint(lvl_ht-2, lvl_ht+5)
        for i in range(max(3, len_ht+randint(0, 1))):
            mob = build_mob(id=mob_id, level=levels)
            mob.controller = Complex_BE_AI(mob)
            enemy_team.add(mob)

        place = "content/gfx/bg/be/b_dungeon_1.jpg"
        result = run_default_be(enemy_team, background=place, slaves=False, prebattle=False, death=True)

        if result is True:
            exp = exp_reward(hero.team, enemy_team)
            if persistent.battle_results:
                renpy.show_screen("give_exp_after_battle", hero.team, exp)
            return
            # hero.say("Serves you right!")
        else:
            # Hero is dead, right?
            # Should just be the game over screen.
            return

    def dungeon_grab_item(item, sound=None):
        if sound is not None:
            filename, channel = sound
            renpy.play(filename, channel=channel)
        item = store.items[item]
        hero.inventory.append(item)
        dungeon.say([hero.name, "{}! This will come useful!".format(item.id)])
        # hero.say("{}!".format(item.id))
        # hero.say("This can proof useful!")
        return
