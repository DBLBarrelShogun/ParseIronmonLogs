import os
import re

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
            if pline.startswith("--Randomized Evolutions--"):
                startParse = True
                continue
            if startParse and pline != "":
                '''
                pokemon = pline.split(" and ",1)
                pokemon = pokemon[0].replace(" ","").split("->")
                '''
                pokemon = pline.replace("  ","").split("->")
                if pline.startswith("--Pokemon Base Stats & Types--"):
                    startParse = False
                    break
                elif pline.startswith("Pikachuc") or pline.startswith("Pikachup"):
                    # Required here to prevent these clashing with standard Pikachu
                    pokeevo = ",".join(pokemon)
                    print(seedString.rstrip() + "," + pokeevo.rstrip())
                elif pline.startswith("Pikachu"):
                    pokeSplit = re.split(r"and(?= )", pokemon[1])
                    print(seedString.rstrip() + ",Pikachu(Raichu)," + pokeSplit[0].rstrip())
                    print(seedString.rstrip() + ",Pikachu(RaichuA)," + pokeSplit[1].rstrip())
                    
                elif pline.startswith("Gloom"):
                    pokeSplit = re.split(r"and(?= )", pokemon[1])
                    print(seedString.rstrip() + ",Gloom(Vileplume)," + pokeSplit[0].rstrip())
                    print(seedString.rstrip() + ",Gloom(Bellossom)," + pokeSplit[1].rstrip())
                    
                elif pline.startswith("Poliwhirl"):
                    pokeSplit = re.split(r"and(?= )", pokemon[1])
                    print(seedString.rstrip() + ",Poliwhirl(Poliwrath)," + pokeSplit[0].rstrip())
                    print(seedString.rstrip() + ",Poliwhirl(Politoed)," + pokeSplit[1].rstrip())
                elif pline.startswith("Slowpokeg"):
                    pokeSplit = re.split(r"and(?= )", pokemon[1])
                    print(seedString.rstrip() + ",Slowpoke(SlowbroG)," + pokeSplit[0].rstrip())
                    print(seedString.rstrip() + ",Slowpoke(SlowkingG)," + pokeSplit[1].rstrip())
                    
                elif pline.startswith("Slowpoke"):
                    pokeSplit = re.split(r"and(?= )", pokemon[1])
                    print(seedString.rstrip() + ",Slowpoke(Slowbro)," + pokeSplit[0].rstrip())
                    print(seedString.rstrip() + ",Slowpoke(Slowking)," + pokeSplit[1].rstrip())
                    
                elif pline.startswith("Exeggcute"):
                    pokeSplit = re.split(r"and(?= )", pokemon[1])
                    print(seedString.rstrip() + ",Exeggcute(Exeggutor)," + pokeSplit[0].rstrip())
                    print(seedString.rstrip() + ",Exeggcute(ExeggutorA)," + pokeSplit[1].rstrip())
                    
                elif pline.startswith("Koffing"):
                    pokeSplit = re.split(r"and(?= )", pokemon[1])
                    print(seedString.rstrip() + ",Koffing(Weezing)," + pokeSplit[0].rstrip())
                    print(seedString.rstrip() + ",Koffing(WeezingG)," + pokeSplit[1].rstrip())
                    
                elif pline.startswith("Scyther"):
                    pokeSplit = re.split(r"and(?= )", pokemon[1])
                    print(seedString.rstrip() + ",Scyther(Scizor)," + pokeSplit[0].rstrip())
                    print(seedString.rstrip() + ",Scyther(Kleavor)," + pokeSplit[1].rstrip())
                    
                elif pline.startswith("Eeveep"):
                    # Required here to prevent this clashing with standard Eevee
                    pokeevo = ",".join(pokemon)
                    print(seedString.rstrip() + "," + pokeevo.rstrip())
                elif pline.startswith("Eevee"):
                    eevos = pokemon[1].split(",")
                    print(seedString.rstrip() + ",Eevee(Jolteon)," + eevos[0].rstrip())
                    print(seedString.rstrip() + ",Eevee(Vaporeon)," + eevos[1].rstrip())
                    print(seedString.rstrip() + ",Eevee(Flareon)," + eevos[2].rstrip())
                    print(seedString.rstrip() + ",Eevee(Espeon)," + eevos[3].rstrip())
                    print(seedString.rstrip() + ",Eevee(Umbreon)," + eevos[4].rstrip())
                    print(seedString.rstrip() + ",Eevee(Leafeon)," + eevos[5].rstrip())
                    eevGlace = eevos[6].split("and",1)
                    print(seedString.rstrip() + ",Eevee(Glaceon)," + eevGlace[0].rstrip())
                    print(seedString.rstrip() + ",Eevee(Sylveon)," + eevGlace[1].rstrip())
                elif pline.startswith("Quilava"):
                    pokeSplit = re.split(r"and(?= )", pokemon[1])
                    print(seedString.rstrip() + ",Quilava(Typhlosion)," + pokeSplit[0].rstrip())
                    print(seedString.rstrip() + ",Quilava(TyphlosionH)," + pokeSplit[1].rstrip())
                    
                elif pline.startswith("Tyrogue"):
                    pokeSplit = re.split(r"and(?= )", pokemon[1])
                    tyrSplit = pokeSplit[0].split(",")
                    print(seedString.rstrip() + ",Tyrogue(Hitmonchan)," + tyrSplit[0].rstrip())
                    print(seedString.rstrip() + ",Tyrogue(Hitmonlee)," + tyrSplit[1].rstrip())
                    print(seedString.rstrip() + ",Tyrogue(Hitmontop)," + pokeSplit[1].rstrip())
                    
                elif pline.startswith("Wurmple"):
                    pokeSplit = re.split(r"and(?= )", pokemon[1])
                    print(seedString.rstrip() + ",Wurmple(Silcoon)," + pokeSplit[0].rstrip())
                    print(seedString.rstrip() + ",Wurmple(Cascoon)," + pokeSplit[1].rstrip())
                    
                elif pline.startswith("Kirlia"):
                    pokeSplit = re.split(r"and(?= )", pokemon[1])
                    print(seedString.rstrip() + ",Kirlia(Gardevoir)," + pokeSplit[0].rstrip())
                    print(seedString.rstrip() + ",Kirlia(Gallade)," + pokeSplit[1].rstrip())
                    
                elif pline.startswith("Nincada"):
                    pokeSplit = re.split(r"and(?= )", pokemon[1])
                    print(seedString.rstrip() + ",Nincada(Ninjask)," + pokeSplit[0].rstrip())
                    print(seedString.rstrip() + ",Nincada(Shedinja)," + pokeSplit[1].rstrip())
                elif pline.startswith("Snorunt"):
                    pokeSplit = re.split(r"and(?= )", pokemon[1])
                    print(seedString.rstrip() + ",Snorunt(Glalie)," + pokeSplit[0].rstrip())
                    print(seedString.rstrip() + ",Snorunt(Froslass)," + pokeSplit[1].rstrip())
                    
                elif pline.startswith("Clamperl"):
                    pokeSplit = re.split(r"and(?= )", pokemon[1])
                    print(seedString.rstrip() + ",Clamperl(Huntail)," + pokeSplit[0].rstrip())
                    print(seedString.rstrip() + ",Clamperl(Gorebyss)," + pokeSplit[1].rstrip())
                    
                elif pline.startswith("Burmys"):
                    pokeSplit = re.split(r"and(?= )", pokemon[1])
                    print(seedString.rstrip() + ",Burmys(Mothim)," + pokeSplit[0].rstrip())
                    print(seedString.rstrip() + ",Burmys(WormadanS)," + pokeSplit[1].rstrip())
                    
                elif pline.startswith("Burmyt"):
                    pokeSplit = re.split(r"and(?= )", pokemon[1])
                    print(seedString.rstrip() + ",Burmyt(Mothim)," + pokeSplit[0].rstrip())
                    print(seedString.rstrip() + ",Burmyt(WormadanT)," + pokeSplit[1].rstrip())
                    
                elif pline.startswith("Burmy"):
                    pokeSplit = re.split(r"and(?= )", pokemon[1])
                    print(seedString.rstrip() + ",Burmy(Mothim)," + pokeSplit[0].rstrip())
                    print(seedString.rstrip() + ",Burmy(Wormadan)," + pokeSplit[1].rstrip())
                    
                elif pline.startswith("Mime Jr"):
                    pokeSplit = re.split(r"and(?= )", pokemon[1])
                    print(seedString.rstrip() + ",Mime Jr(Mr. Mime)," + pokeSplit[0].rstrip())
                    print(seedString.rstrip() + ",Mime Jr(Mr. MimeG)," + pokeSplit[1].rstrip())
                    
                elif pline.startswith("Dewott"):
                    pokeSplit = re.split(r"and(?= )", pokemon[1])
                    print(seedString.rstrip() + ",Dewott(Samurott)," + pokeSplit[0].rstrip())
                    print(seedString.rstrip() + ",Dewott(SamurottG)," + pokeSplit[1].rstrip())
                    
                elif pline.startswith("Petilil"):
                    pokeSplit = re.split(r"and(?= )", pokemon[1])
                    print(seedString.rstrip() + ",Petilil(Lilligant)," + pokeSplit[0].rstrip())
                    print(seedString.rstrip() + ",Petilil(LilligantH)," + pokeSplit[1].rstrip())
                    
                elif pline.startswith("Espurr"):
                    pokeSplit = re.split(r"and(?= )", pokemon[1])
                    print(seedString.rstrip() + ",Espurr(Meowstic)," + pokeSplit[0].rstrip())
                    print(seedString.rstrip() + ",Espurr(MeowsticF)," + pokeSplit[1].rstrip())
                    
                elif pline.startswith("Doublade"):
                    pokeSplit = re.split(r"and(?= )", pokemon[1])
                    print(seedString.rstrip() + ",Doublade(Aegislash)," + pokeSplit[0].rstrip())
                    print(seedString.rstrip() + ",Doublade(AegislashB)," + pokeSplit[1].rstrip())
                    
                elif pline.startswith("Goomy"):
                    pokeSplit = re.split(r"and(?= )", pokemon[1])
                    print(seedString.rstrip() + ",Goomy(Sliggoo)," + pokeSplit[0].rstrip())
                    print(seedString.rstrip() + ",Goomy(SliggooH)," + pokeSplit[1].rstrip())
                    
                elif pline.startswith("Bergmite"):
                    pokeSplit = re.split(r"and(?= )", pokemon[1])
                    print(seedString.rstrip() + ",Bergmite(Avalugg)," + pokeSplit[0].rstrip())
                    print(seedString.rstrip() + ",Bergmite(AvaluggH)," + pokeSplit[1].rstrip())
                    
                elif pline.startswith("Dartrix"):
                    pokeSplit = re.split(r"and(?= )", pokemon[1])
                    print(seedString.rstrip() + ",Dartrix(Decidueye)," + pokeSplit[0].rstrip())
                    print(seedString.rstrip() + ",Dartrix(DecidueyeH)," + pokeSplit[1].rstrip())
                    
                elif pline.startswith("Rockruff"):
                    pokeSplit = re.split(r"and(?= )", pokemon[1])
                    rocSplit = pokeSplit[0].split(",")
                    print(seedString.rstrip() + ",Rockruff(LycanrocM)," + rocSplit[0].rstrip())
                    print(seedString.rstrip() + ",Rockruff(Lycanroc)," + rocSplit[1].rstrip())
                    print(seedString.rstrip() + ",Rockruff(LycanrocD)," + pokeSplit[1].rstrip())
                    
                elif pline.startswith("Cosmoem"):
                    pokeSplit = re.split(r"and(?= )", pokemon[1])
                    print(seedString.rstrip() + ",Cosmoem(Solgaleo)," + pokeSplit[0].rstrip())
                    print(seedString.rstrip() + ",Cosmoem(Lunala)," + pokeSplit[1].rstrip())
                    
                elif pline.startswith("Applin"):
                    pokeSplit = re.split(r"and(?= )", pokemon[1])
                    appSplit = pokeSplit[0].split(",")
                    print(seedString.rstrip() + ",Applin(Appletun)," + appSplit[0].rstrip())
                    print(seedString.rstrip() + ",Applin(Flapple)," + appSplit[1].rstrip())
                    print(seedString.rstrip() + ",Applin(Dipplin)," + pokeSplit[1].rstrip())
                    
                elif pline.startswith("Toxel"):
                    pokeSplit = re.split(r"and(?= )", pokemon[1])
                    print(seedString.rstrip() + ",Toxel(Toxtricity)," + pokeSplit[0].rstrip())
                    print(seedString.rstrip() + ",Toxel(ToxtricityL)," + pokeSplit[1].rstrip())
                    
                elif pline.startswith("Kubfu"):
                    pokeSplit = re.split(r"and(?= )", pokemon[1])
                    print(seedString.rstrip() + ",Kubfu(UrshifuR)," + pokeSplit[0].rstrip())
                    print(seedString.rstrip() + ",Kubfu(Urshifu)," + pokeSplit[1].rstrip())
                    
                elif pline.startswith("Lechonk"):
                    pokeSplit = re.split(r"and(?= )", pokemon[1])
                    print(seedString.rstrip() + ",Lechonk(Oinkologne)," + pokeSplit[0].rstrip())
                    print(seedString.rstrip() + ",Lechonk(OinkologneF)," + pokeSplit[1].rstrip())
                    
                elif pline.startswith("Charcadet"):
                    pokeSplit = re.split(r"and(?= )", pokemon[1])
                    print(seedString.rstrip() + ",Charcadet(Ceruledge)," + pokeSplit[0].rstrip())
                    print(seedString.rstrip() + ",Charcadet(Armarouge)," + pokeSplit[1].rstrip())
                    
                elif pline.startswith("Basculinw"):
                    pokeSplit = re.split(r"and(?= )", pokemon[1])
                    print(seedString.rstrip() + ",Basculinw(Basculegion)," + pokeSplit[0].rstrip())
                    print(seedString.rstrip() + ",Basculinw(BasculegionF)," + pokeSplit[1].rstrip())
                    
                else:
                    pokeevo = ",".join(pokemon)
                    print(seedString.rstrip() + "," + pokeevo.rstrip())
            
            if pline.startswith("--Pokemon Base Stats & Types--"):
                startParse = False
                break
            