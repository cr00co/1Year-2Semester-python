COMBINATIONS = {
    # 1. The Spark of Life & Humanity
    frozenset({"lightning", "water"}):    "life",
    frozenset({"life", "earth"}):         "human",
    frozenset({"human", "human"}):        "family",
    frozenset({"plant", "earth"}):        "nature",
    frozenset({"life", "stone"}):         "egg",
    frozenset({"egg", "air"}):            "bird",

    # 2. Civilization & Society
    frozenset({"brick", "brick"}):        "wall",
    frozenset({"wall", "wall"}):          "house",
    frozenset({"house", "house"}):        "village",
    frozenset({"village", "village"}):    "city",
    frozenset({"house", "cloud"}):        "bed",
    frozenset({"plant", "plant"}):        "fabric",
    frozenset({"fabric", "human"}):       "outfit",
    
    # 3. Time, Space, & The Cosmos
    frozenset({"air", "cloud"}):          "sky",
    frozenset({"sky", "sky"}):            "space",
    frozenset({"sky", "fire"}):           "sun",
    frozenset({"sky", "stone"}):          "moon",
    frozenset({"sun", "moon"}):           "time",
    frozenset({"sun", "stone"}):          "shadow",
    frozenset({"plant", "sun"}):          "flower",

    # 4. Human Anatomy & Emotion
    frozenset({"human", "stone"}):        "jawline",
    frozenset({"air", "time"}):           "silence",
    frozenset({"human", "silence"}):      "eye contact",
    frozenset({"human", "flower"}):       "romance",
    frozenset({"human", "space"}):        "presence",
    frozenset({"lightning", "human"}):    "energy",
    frozenset({"human", "fire"}):         "rage",
    frozenset({"legend", "human"}):       "charisma",
    frozenset({"human", "time"}):         "gen-z",

    # 5. The Tech Tree
    frozenset({"lightning", "metal"}):    "electricity",
    frozenset({"electricity", "glass"}):  "screen",
    frozenset({"screen", "electricity"}): "computer",
    frozenset({"computer", "computer"}):  "internet",
    frozenset({"computer", "human"}):     "gamer",
    frozenset({"human", "electricity"}):  "brain",
    frozenset({"metal", "electricity"}):  "keyboard",
    frozenset({"gamer", "brick"}):        "minecraft",
    frozenset({"glass", "glass"}):        "lens",
    frozenset({"lens", "screen"}):        "camera",

    # 6. Modern Economics
    frozenset({"plant", "stone"}):        "paper",
    frozenset({"paper", "metal"}):        "money",
    frozenset({"money", "city"}):         "bank",
    frozenset({"bank", "human"}):         "bank account",
    frozenset({"house", "money"}):        "rent",
    frozenset({"money", "fire"}):         "loss",
    frozenset({"money", "internet"}):     "shopping",
    frozenset({"shopping", "time"}):      "mail",

    # 7. Abstract Internet Concepts
    frozenset({"brain", "computer"}):     "logic",
    frozenset({"brain", "cloud"}):        "delusion",
    frozenset({"brain", "time"}):         "attention span",
    frozenset({"human", "internet"}):     "opinion",
    frozenset({"internet", "family"}):    "group chat",
    frozenset({"internet", "bird"}):      "twitter",
    frozenset({"water", "internet"}):     "leak",
    frozenset({"internet", "camera"}):    "video",
    frozenset({"human", "shadow"}):       "sus",

    # 8. The Mathematics & Numbers Forge
    frozenset({"logic", "human"}):        "math",
    frozenset({"math", "human"}):         "problem",
    frozenset({"loss", "math"}):          "negative",
    
    # How to craft the meme numbers:
    frozenset({"math", "water"}):         "6",
    frozenset({"math", "fire"}):          "7",
    frozenset({"math", "air"}):           "10",
    
    # Scaling up for the 67 combinations
    frozenset({"10", "10"}):              "20",
    frozenset({"20", "10"}):              "30",
    frozenset({"30", "10"}):              "40",
    frozenset({"40", "10"}):              "50",
    
    # Adding the 7s for the odd numbers
    frozenset({"10", "7"}):               "17",
    frozenset({"20", "7"}):               "27",
    frozenset({"30", "7"}):               "37",
    frozenset({"40", "7"}):               "47",
}