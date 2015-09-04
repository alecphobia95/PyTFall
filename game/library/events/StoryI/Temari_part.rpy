init:
    $ noisedissolve = ImageDissolve(im.Tile("content/events/StoryI/noisetile.png"), 1.0, 1)
init python:
    temariquest = register_quest("Stubborn Kunoichi")
label temari_first_meeting:
    scene black
    $ t = chars["Temari"]
    $ t_spr = chars["Temari"].get_vnsprite()
    show bg hidden_village with dissolve
    show expression t.show("sfw", "rest", "outdoors", "everyday", "urban", "nature", resize=(800, 600), type="first_default") as xxx at truecenter
    "Just near the corner of the village training area you see a girl that is resting. She nods towards you."
    $ t.override_portrait("portrait", "confident")
    t.say "So, you are my mid day?"
    menu:
        "What?":
            t.say "Ok, playing dumb..."
        "Yes":
            t.say "Listen... Tsunade is nice and all, but she is a bit traditional."
        "No":
            t.say "Oh? Then I wonder why Tsunade is watching us as we speak."
    t.say "Let me be more blunt. I know she promised you something to be my first time."
    $ t.override_portrait("portrait", "indifferent")
    t.say "The old hag is not very subtle, when she drinks and then blabbers on about how traditions are important. It does not take two trips to the library to find out about their traditions. As if they were anything special or unique..."
    hide xxx with dissolve
    show expression t_spr at center
    t.say "I hate to break this to you, but I had a life before I settled here. I have two baby brothers, and even when it would break the old hags heart, a girl can only take a bath with her baby brothers for so long until she notices..."
    t.say "I have tried a thing or two with my brothers, so I'm not as inexperienced as most of the girls here. Don't look so surprised, at least I didn't jump my father, like certain people."
    t.say "I'm still technically a virgin, but I'm used to do it with my family, not complete strangers. There is nothing for you here."
    $ t.restore_portrait()
    scene black with dissolve
    $ pytfall.world_quests.get("Stubborn Kunoichi").next_in_label("You met Temari, a weird kunoichi who loves her family too much. Perhaps you have to know each other better for a start?..")
    jump hiddenVillage_entrance
    
label temari_second_meeting:
    $ t = chars["Temari"]
    $ t_spr = chars["Temari"].get_vnsprite()
    show expression t_spr at center
    $ t.override_portrait("portrait", "indifferent")
    t.say "Say, [hero.name]... Are you trying to become close to me because you are still planning to do it with me?"
    t.say "I have a proposition. How about a friendly match? If you are really want to know... there is someone that I had an eye for."
    t.say "But granny keeps that person away from me. If I do her little thing, she will no longer be able to keep doing it."
    t.say "So, yea... you would be helping me. If we just do it without a fight, it would be suspicious."
    t.say "Fighting is good for the figure, gets the blood going, and it's almost foreplay. Come on, I'll try to be gentle."
    hide expression t_spr with dissolve
    $ t.restore_portrait()
    scene black with dissolve
    $ pytfall.world_quests.get("Stubborn Kunoichi").next_in_label("Temari wants you fight her at the Training Grounds. She is going to hold back, but you still better be prepared.")
    jump hiddenVillage_entrance
    
label temari_final_meeting:
    show bg story training_ground with dissolve
    $ t = chars["Temari"]
    $ t_spr = chars["Temari"].get_vnsprite()
    $ t.disposition += 300
    show expression t_spr at center
    $ t.override_portrait("portrait", "confident")
    t.say "It wasn't.... as bad as I expected it to be. You need to work on your weapons, you need to train to get rid of the flab, and even the four year olds in the village pose more of a challenge."
    $ t.override_portrait("portrait", "happy")
    t.say "On the other side, you were pretty good with the groundwork and all. Nothing like my brothers, but... does not mean bad."
    $ t.override_portrait("portrait", "shy")
    t.say "I hope you did like it as well... Not that I particularly care, but... If you want to, I would like to train some more at a later time."
    "She blushes harder."
    t.say "The next time, at first, I can teach you a bit more about fighting, and then you can teach me a bit more about groundwork... Here, you can have my water bottle, and don't worry about the scratches."
    $ t.set_flag("quest_cannot_be_lover", value=False)
    $ t.set_flag("quest_cannot_be_fucked", value=False)
    hide expression t_spr with dissolve
    $ t.restore_portrait()
    $ pytfall.world_quests.get("Stubborn Kunoichi").next_in_label("You managed to impress her. Perhaps now she will be more appeasable?")
    scene black with dissolve
    jump hiddenVillage_entrance
    
label temari_finish_quest:
    $ t = chars["Temari"]
    "She clearly imagined her brothers instead of you while you were doing it... Never mind, important thing is that you have done it."
    $ pytfall.world_quests.get("Stubborn Kunoichi").finish_in_label("You took care of Temari's virginity. She can be hired now.", "complete")
    $ t.set_flag("quest_cannot_be_hired", value=False)
    jump hiddenVillage_entrance