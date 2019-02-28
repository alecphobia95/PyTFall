init 5 python:
    class TheEye(BusinessUpgrade):
        SORTING_ORDER = 1
        COMPATIBILITY = [ExplorationGuild]

        NAME = "The Eye"
        IMG = "content/buildings/upgrades/the_eye.webp"
        MATERIALS = {}
        temp = []
        temp.append("The Eye of Sauron!")
        temp.append("Powerful energy field with powerful effects.")
        temp.append("(+Exploration never falls below 50%)")
        temp.append("(+Reveals information about unexplored areas)")
        DESC = "\n".join(temp)
        del temp
        COST = 500000
        IN_SLOTS = 5
        EX_SLOTS = 20
        CAPACITY = 0

        EXP_CAP_IN_SLOTS = 0
        EXP_CAP_EX_SLOTS = 0
        EXP_CAP_COST = 0

        def __init__(self, **kwargs):
            super(TheEye, self).__init__(**kwargs)
            self.expands_capacity = False # Force the matter.


    class GuildStables(BusinessUpgrade):
        SORTING_ORDER = 5
        COMPATIBILITY = [ExplorationGuild]

        NAME = "Stables"
        IMG = "content/buildings/upgrades/stables.webp"
        MATERIALS = {"Bricks": 20, "Stone": 10,
                     "Steel": 10, "Wood": 50}
        temp = []
        temp.append("Stables.")
        temp.append("A man on a horse is spiritually, as well as physically, bigger then a man on foot.")
        temp.append("(+50% Traveling Speed)")
        DESC = "\n".join(temp)
        del temp
        COST = 10000
        IN_SLOTS = 2
        EX_SLOTS = 10
        CAPACITY = 0

        EXP_CAP_IN_SLOTS = 0
        EXP_CAP_EX_SLOTS = 0
        EXP_CAP_COST = 0

        def __init__(self, **kwargs):
            super(GuildStables, self).__init__(**kwargs)
            self.expands_capacity = False # Force the matter.
