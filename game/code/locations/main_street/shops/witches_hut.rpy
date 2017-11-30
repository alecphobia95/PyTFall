label witches_hut:
    if not "shops" in ilists.world_music:
        $ ilists.world_music["shops"] = [track for track in os.listdir(content_path("sfx/music/world")) if track.startswith("shops")]
    if not global_flags.has_flag("keep_playing_music"):
        play world choice(ilists.world_music["shops"]) fadein 1.5

    hide screen forest_entrance

    scene bg witches_hut
    with dissolve

    show expression npcs["Abby_the_witch"].get_vnsprite() as npc
    with dissolve

    $ w = npcs["Abby_the_witch"].say

    if global_flags.flag('visited_witches_hut'):
        w "Welcome Back!"
    else:
        $ w = Character("???", color=orange, what_color=yellow, show_two_window=True)
        $ global_flags.set_flag('visited_witches_hut')
        w "New Customer!"
        extend " Welcome to my Potion Shop!"
        w "I am Abby, the Witch, both Cool and Wicked. You'll never know what you run into here!"
        $ w = npcs["Abby_the_witch"].say
        w "Oh, and I also know a few decent {color=[orangered]}Fire{/color} and {color=[lime]}Air{/color} spells if you're interested."
        w "Check out the best home brew in the realm and some other great items in stock!"

    $ pytfall.world_quests.run_quests("auto")
    $ pytfall.world_events.run_events("auto")

label witch_menu:
    show screen witch_shop
    with dissolve
    while 1:
        $ result = ui.interact()

label witches_hut_shopping:
    w "Sweet!"
    python:
        witches_hut = ItemShop('Witches Hut', 18, ['Witches Hut'], sells=["amulet", "restore", "smallweapon"])
        focus = False
        item_price = 0
        filter = "all"
        amount = 1
        shop = pytfall.witches_hut
        shop.inventory.apply_filter(filter)
        char = hero
        char.inventory.set_page_size(18)
        char.inventory.apply_filter(filter)

    show screen shopping(left_ref=hero, right_ref=shop)

    with dissolve
    call shop_control

    $ global_flags.del_flag("keep_playing_music")
    hide screen shopping
    with dissolve
    w "Let me know if you need anything else."
    jump witch_menu

label witches_hut_shopping_spells:
    w "Sweet!"
    python:
        witch_spells_shop = ItemShop("Witch Spells Shop", 18, ["Witch Spells Shop"], gold=5000, sells=["scroll"], sell_margin=0.25, buy_margin=5.0)
        focus = False
        item_price = 0
        filter = "all"
        amount = 1
        shop = pytfall.witch_spells_shop
        shop.inventory.apply_filter(filter)
        char = hero
        char.inventory.set_page_size(18)
        char.inventory.apply_filter(filter)

    show screen shopping(left_ref=hero, right_ref=shop)
    with dissolve
    $ pytfall.world_events.run_events("auto")
    call shop_control

    $ global_flags.del_flag("keep_playing_music")
    hide screen shopping
    with dissolve
    w "Let me know if you need anything else."
    jump witch_menu

label witch_training:
    if not global_flags.has_flag("witches_training_explained"):
        w "I will train magic, intelligence and restore some MP."
        w "I can also guarantee you agility will go up if you pay attention in class!"
        extend " That, however, is rare."
        w "Yeap! I am That good!"
        $ global_flags.set_flag("witches_training_explained")
    else:
        w "You know the deal!"

    if len(hero.team) > 1:
        call screen character_pick_screen
        $ char = _return
    else:
        $ char = hero

    if not char:
        jump witch_menu
    $ loop = True

    while loop:
        menu:
            "About training sessions":
                call about_personal_training
            "About Abby training":
                w "I will train magic, intelligence and restore some MP."
                w "I can also guarantee you agility will go up if you pay attention in class!"
                extend " That however does not often happen for reasons unknown..."
                w "Yeap! I am That good!"
            "{color=[green]}Setup sessions for [char.name]{/color}" if not char.has_flag("train_with_witch"):
                $ char.set_flag("train_with_witch")
                $ char.apply_trait(traits["Abby Training"])
                $ training_price = char.get_training_price()
                w "I will take [training_price] gold per day. Be sure to use my training only on wicked stuff!"
            "{color=[red]}Cancel sessions for [char.name]{/color}" if char.flag("train_with_witch"):
                $ char.del_flag("train_with_witch")
                $ char.remove_trait(traits["Abby Training"])
                w "Maybe next time then?"
            "Pick another character" if len(hero.team) > 1:
                call screen character_pick_screen
                if _return:
                    $ char = _return
            "Do Nothing":
                $ loop = False
    jump witch_menu

label witch_talking_menu:
    $ loop = True
    while loop:
        menu:
            w "What do you want?"
            "Abby The Witch Main":
                $ pass
            "Nevermind":
                $ loop = False
            "Leave the shop":
                $ loop = False
                jump forest_entrance
    jump witch_menu

screen witch_shop:
    frame:
        xalign 0.95
        ypos 20
        background Frame(Transform("content/gfx/frame/p_frame5.png", alpha=0.98), 10, 10)
        xpadding 10
        ypadding 10
        vbox:
            style_group "wood"
            align (0.5, 0.5)
            spacing 10
            button:
                xysize (150, 40)
                yalign 0.5
                action [Hide("witch_shop"), Jump("witches_hut_shopping")]
                text "Shop" size 15
            button:
                xysize (150, 40)
                yalign 0.5
                action [Hide("witch_shop"), Jump("witches_hut_shopping_spells")]
                text "Spells" size 15
            button:
                xysize (150, 40)
                yalign 0.5
                action [Hide("witch_shop"), Jump("witch_training")]
                text "Training" size 15
            button:
                xysize (150, 40)
                yalign 0.5
                action [Hide("witch_shop"), Jump("witch_talking_menu")]
                text "Talk" size 15
            button:
                xysize (150, 40)
                yalign 0.5
                action [Hide("witch_shop"), Jump("forest_entrance")]
                text "Leave" size 15
