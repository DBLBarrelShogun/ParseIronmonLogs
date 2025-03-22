import os

msg = "Starting parse"
print(msg)

lineCount = 1
startParse = "N"
endParse = "N"
seedString = ""

for logfile in os.listdir("logs"):
    print(os.fsdecode(logfile))
    with open("logs/"+logfile, "r") as f:
        for line in f:
            pokemon = []
            pline = line.rstrip()
            if pline.startswith("Random Seed:"):
                seedString = pline.replace("Random Seed: ","")
            
            if pline.startswith("--Randomized Evolutions--"):
                startParse = "Y"
                endParse = "N"
                continue
            if pline.startswith("--Pokemon Base Stats & Types--"):
                startParse = "N"
                endParse = "Y"
                break
            if startParse == "Y" and pline != "":
                pokemon = pline.split(" and ",1)
                pokemon = pokemon[0].replace(" ","").split("->")
                pokeevo = ",".join(pokemon)
                print(seedString.rstrip() + "," + pokeevo.rstrip())
            '''
            if pline.startswith("--Pokemon Movesets--"):
                startParse = "Y"
                endParse = "N"
                continue
            if pline.startswith("--TM Moves--"):
                startParse = "N"
                endParse = "Y"
                break
            if startParse == "Y" and "->" in pline:
                pokemon = pline.replace(" ","").split("->")
                pokeevo = ",".join(pokemon)
                print(seedString.rstrip() + "," + pokeevo.rstrip())
            '''