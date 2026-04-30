"""
zones.the_void.mobs
───────────────────
Mob templates for The Void zone.

Add an entry to TEMPLATES for every NPC type that can appear in this zone.
Call spawn(key) to get a fresh independent Mob instance — place as many
copies in rooms as you like, each is independent.
"""

from ashenmoor.world import Mob
from ashenmoor.world.zone import make_spawner

TEMPLATES: dict[str, dict] = {
    "wandering_student": {
        "name": "a wandering student",
        "key_words": ("student", "wandering"),
        "room_description": "&wA wandering student meanders about aimlessly.&N",
        "description": (
            "A student with a faraway look, clearly lost in thought.\n"
            "Or possibly just lost."
        ),
        "race": "Human",
        "class": "Student",
        "level": 1,
        "stats": [60, 65, 60, 80, 70, 75],
        "aggro": False,
        "wander": True,
    },
    "escbaalion": {
        "name": "Escbaalion",  # The c is silent
        "key_words": ("Escbaalion"),
        "room_description": "&gEscbaalion&N &wlicks his eyeball.&N",
        "description": (
            "A humanoid lizard. He is &gdark-green&N, and has a short\n"
            "&Ccyan sail&N that runs from the top of his head to the end of his tail.\n"
            "He wears an almost &Xblack cloak&N, but wears &Rno&N pants.\n"
            "A &ybrown leather satchel&N is slung over his shoulder.\n"
            "Only &ghe&N knows what is inside his &ybag&N. . . ."
        ),
        "race": "Lizaroid",
        "class": "Sorcerer",
        "level": 10,
        "stats": [80, 50, 200, 90, 90, 70],
    },
    "void_guardian": {
        "name": "the Void Guardian",
        "key_words": ("guardian", "void"),
        "room_description": ("&XThe &+WVoid Guardian&N&X stands watch, unblinking.&N"),
        "description": (
            "&XA towering figure of condensed darkness.\n"
            "Its eyes are two cold points of &+Wwhite light&N&X.&N"
        ),
        "race": "Unknown",
        "class": "Guardian",
        "level": 50,
        "stats": [120, 100, 130, 90, 110, 50],
        "aggro": False,
        "wander": False,
        "position": "standing",
    },
    # kill=False — combat system refuses killing blow on this mob.
    "moted_pc": {
        "name": "Moted",
        "key_words": ("moted", "dwarf"),
        "room_description": "&wMoted the Dwarf is here.&N",
        "description": "A weathered Dwarven shaman. Best not to cross him.",
        "race": "Dwarf",
        "class": "Shaman",
        "level": 24,
        "stats": [88, 80, 80, 80, 80, 80],
        "aggro": False,
        "wander": False,
        "kill": False,
    },
}

# Module-level spawn — rooms.py calls  M.spawn("void_guardian")
spawn = make_spawner(TEMPLATES, lambda: Mob)
