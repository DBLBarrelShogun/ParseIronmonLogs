import os

msg = "Starting parse"
print(msg)

for logfile in os.listdir("logs"):
    print(os.fsdecode(logfile))
    with open("logs/"+logfile, "r") as f:
        startParse = False
        seedString = ""
        for line in f:
            pokemon = []
            pline = line.rstrip()
            if pline.startswith("Random Seed:"):
                seedString = pline.replace("Random Seed: ","")
            '''
            if pline.startswith("--Pokemon Movesets--"):
                startParse = "Y"
                endParse = "N"
                continue
            if startParse == "Y" and "->" in pline:
                pokemon = pline.replace(" ","").split("->")
                pokeevo = ",".join(pokemon)
                print(seedString.rstrip() + "," + pokeevo.rstrip())
            if pline.startswith("--TM Moves--"):
                startParse = "N"
                endParse = "Y"
                break
            '''
            if pline.startswith("--Randomized Evolutions--"):
                startParse = True
                continue
            if startParse and pline != "":
                pokemon = pline.split(" and ",1)
                pokemon = pokemon[0].replace(" ","").split("->")
                pokeevo = ",".join(pokemon)
                print(seedString.rstrip() + "," + pokeevo.rstrip())
            
            if pline.startswith("--Pokemon Base Stats & Types--"):
                startParse = False
                break
            