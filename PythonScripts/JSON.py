#add information about game players in JSON format
import json #import libary json
filename = "player_settings.txt"
myfile = open(filename, mode='w', encoding='utf_8')

player1 = {
    'playername': "Zbych",
    'score': 300,
    'avards': ["1 class", "2nd class", "1st winner"]

}

player2 = {
    'playername': "Zdislaw",
    'score': 250,
    'avards': ["1 places", "2nd places", "1st fly"]
}

myplayers = []
myplayers.append(player1)
myplayers.append(player2)

#---- save by JSON----

json.dump(myplayers, myfile)

myfile.close()

#---load file with JSON---

myfile = open(filename, mode='r', encoding='utf_8')
loaded_data = json.load(myfile)

for user in loaded_data:
    print("player name: " + str(user['playername']))
    print("score is: "  + str(user['score']))
    print("avard n1 : " + str(user['avards'][0])) #printing about 1st medal
    print("avard n2: " + str(user['avards'][1]))
    print("avard n3 : " + str(user['avards'][2]))
    print("-----\n\n")
