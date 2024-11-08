players = ["Horse", "Gorilla", "Dishpod", "Wolf", "Headphones"]

phrases = ["CS", "is", "cooler", "than", "chemistry", "hi", "yo"]

t = 0

while len(players) > 1:

    print(players)

    for i in phrases:
        t = (t+1) % len(players)

    players.remove(players[t])

print(players)
