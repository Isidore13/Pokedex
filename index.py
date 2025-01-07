#coding:utf-8
import cgi
import sqlite3
import csv
import random
import os
import json

conn = sqlite3.connect('pokedex.db')
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS POKEDEX")
cur.execute("CREATE TABLE IF NOT EXISTS POKEDEX(ID_Interne INT, Number INT, Name TEXT, Type1 TEXT, Type2 TEXT, Total INT, HP INT, Attack INT, Defense INT, Sp_Atk INT, Sp_Def INT, Speed INT, Generation INT, Legendary BOOLEAN, Artwork TEXT, Icone TEXT)")

datas = []
with open("./Pokedex2.csv","r") as csvfile:
    contenu = csv.reader(csvfile, delimiter=";")
    next(contenu)
    for ligne in contenu:
        datas.append(ligne)
csvfile.close()

cur.executemany("INSERT INTO POKEDEX(ID_Interne, Number, Name, Type1, Type2, Total, HP, Attack, Defense, Sp_Atk, Sp_Def, Speed, Generation, Legendary, Artwork, Icone) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", datas)
conn.commit()

Mega = [4,8,9,13,20,24,72,88,125,138,142,155,165,166,197,225,230,233,249,269,276,280,284,307,328,330,334,337,340,350,355,367,388,394,398,410,414,419,421,427,477,495,499,512,527,592,797]
Interdit = [717, 617, 751]

def Hazard(c) :
    RandID=[]
    RandTeam=[]
    if c <= 6 :
        m = 0
        pg = 0
        pk = 0
        while len(RandID) < c:
            random_id = random.randint(1, 800)
            if m == 0 and random_id not in Interdit and random_id not in {423,425} and random_id not in Mega :
                RandID.append(random_id)
            if m == 1 :
                if random_id not in Mega and random_id not in Interdit and random_id not in {423,425}:
                    RandID.append(random_id)
            if random_id in Mega and m == 0 and random_id not in Interdit and random_id not in {423,425}:
                    RandID.append(random_id)
                    m = m+1
            if random_id == 423 or 425 :
                if pk == 0 and random_id == 423 :
                    pk = pk +1
                    RandID.append(random_id)
                if pg == 0 and random_id == 425 :
                    pg = pg +1
                    RandID.append(random_id)
                if pk == 1 and random_id == 423 or pg == 1 and random_id == 425 :
                    pk == pk
                    pg == pg
        for i in range (len(RandID)) :
            cur.execute("SELECT Name FROM POKEDEX WHERE ID_Interne = ?", (RandID[i],))
            result = cur.fetchone()
            if result:
                RandTeam.append(result[0])
            else:
                print(f"The pokemon wasn't found :(")
        return RandTeam
    else :
        print("Too much pokemon ! You can only carry 6 pokemon at the same time.")

TableAttack = dict()
TableAttack['Normal'] = [1,1,1,1,1,1,1,1,1,1,1,1,1/2,0,1,1,1/2,1]
TableAttack['Fire'] = [1,1/2,1/2,1,2,2,1,1,1,1,1,2,1/2,1,1/2,1,2,1]
TableAttack['Water'] = [1,2,1/2,1,1/2,1,1,1,2,1,1,1,2,1,1/2,1,1,1]
TableAttack['Electric'] = [1,1,2,1/2,1/2,1,1,1,0,2,1,1,1,1,1/2,1,1,1]
TableAttack['Grass'] = [1,1/2,2,1,1/2,1,1,1/2,2,1/2,1,1/2,2,1,1/2,1,1/2,1]
TableAttack['Ice'] = [1,1/2,1/2,1,2,1/2,1,1,2,2,1,1,1,1,2,1,1/2,1]
TableAttack['Fighting'] = [2,1,1,1,1,2,1,1/2,1,1/2,1/2,1/2,2,0,1,2,2,1/2]
TableAttack['Poison'] = [1,1,1,1,2,1,1,1/2,1/2,1,1,1,1/2,1/2,1,1,0,2]
TableAttack['Ground'] = [1,2,1,2,1/2,1,1,2,1,0,1,1/2,2,1,1,1,2,1]
TableAttack['Flying'] = [1,1,1,1/2,2,1,2,1,1,1,1,2,1/2,1,1,1,1/2,1]
TableAttack['Psychic'] = [1,1,1,1,1,1,2,2,1,1,1/2,1,1,1,1,0,1/2,1]
TableAttack['Bug'] = [1,1/2,1,1,2,1,1/2,1/2,1,1/2,2,1,1,1/2,1,2,1/2,1/2]
TableAttack['Rock'] = [1,2,1,1,1,2,1/2,1,1/2,2,1,2,1,1,1,1,1/2,1]
TableAttack['Ghost'] = [0,1,1,1,1,1,1,1,1,1,2,1,1,2,1,1/2,1,1]
TableAttack['Dragon'] = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1/2,0]
TableAttack['Dark'] = [1,1,1,1,1,1,1/2,1,1,1,2,1,1,2,1,1/2,1,1/2]
TableAttack['Steel'] = [1,1/2,1/2,1/2,1,2,1,1,1,1,1,1,2,1,1,1,1/2,2]
TableAttack['Fairy'] = [1,1/2,1,1,1,1,2,1/2,1,1,1,1,1,1,2,2,1/2,1]

TableDefense = dict()
TableDefense['Normal'] = [1,1,1,1,1,1,2,1,1,1,1,1,1,0,1,1,1,1]
TableDefense['Fire'] = [1,1/2,2,1,1/2,1/2,1,1,2,1,1,1/2,2,1,1,1,1/2,1/2]
TableDefense['Water'] = [1,1/2,1/2,2,2,1/2,1,1,1,1,1,1,1,1,1,1,1/2,1]
TableDefense['Electric'] = [1,1,1,1/2,1,1,1,1,2,1/2,1,1,1,1,1,1,1/2,1]
TableDefense['Grass'] = [1,2,1/2,1/2,1/2,2,1,2,1/2,2,1,2,1,1,1,1,1,1]
TableDefense['Ice'] = [1,2,1,1,1,1/2,2,1,1,1,1,1,2,1,1,1,2,1]
TableDefense['Fighting'] = [1,1,1,1,1,1,1,1,1,2,2,1/2,1/2,1,1,1/2,1,2]
TableDefense['Poison'] = [1,1,1,1,1/2,1,1/2,1/2,2,1,2,1/2,1,1,1,1,1,1/2]
TableDefense['Ground'] = [1,1,2,0,2,2,1,1/2,1,1,1,1,1/2,1,1,1,1,1]
TableDefense['Flying'] = [1,1,1,2,1/2,2,1/2,1,0,1,1,1/2,2,1,1,1,1,1]
TableDefense['Psychic'] = [1,1,1,1,1,1,1/2,1,1,1,1/2,2,1,2,1,2,1,1]
TableDefense['Bug'] = [1,2,1,1,1/2,1,1/2,1,1/2,2,1,1,2,1,1,1,1,1]
TableDefense['Rock'] = [1/2,1/2,2,1,2,1,2,1/2,2,1/2,1,1,1,1,1,1,2,1]
TableDefense['Ghost'] = [0,1,1,1,1,1,0,1/2,1,1,1,1/2,1,2,1,2,1,1]
TableDefense['Dragon'] = [1,1/2,1/2,1/2,1/2,2,1,1,1,1,1,1,1,1,2,1,1,2]
TableDefense['Dark'] = [1,1,1,1,1,1,2,1,1,1,0,2,1,1/2,1,1/2,1,2]
TableDefense['Steel'] = [1/2,2,1,1,1/2,1/2,2,0,2,1/2,1/2,1/2,1/2,1,1/2,1,1/2,1/2]
TableDefense['Fairy'] = [1,1,1,1,1,1,1/2,2,1,1,1,1/2,1,1,0,1/2,2,1]

Types = ['Normal','Fire','Water','Electric','Grass','Ice','Fighting','Poison','Ground','Flying','Psychic','Bug','Rock','Ghost','Dragon','Dark','Steel','Fairy']
Noms = []

for i in range (801) :
    cur.execute("SELECT Name FROM POKEDEX WHERE ID_Interne = ?", (i,))
    result = cur.fetchone()
    Noms.append(result)

def DétecteType(n) :
    Ty=[]
    if len(n) == 2 :
        n = n[0]
    cur.execute("SELECT Type1 FROM POKEDEX WHERE Name = ?", (n,))
    result1 = cur.fetchone()
    if result1:
        Ty.append(result1[0])
    cur.execute("SELECT Type2 FROM POKEDEX WHERE Name = ?", (n,))
    result2 = cur.fetchone()
    if result2:
        Ty.append(result2[0])
    else:
        print(f"Error, please check spelling!")

    return Ty

def TypeChartAttack (a):
    résistance = []
    neutre = []
    faiblesse = []
    immunité = []
    if a in TableAttack :
        t1=TableAttack.get(a)
        for i in range (18) :
            if t1[i] == 1/2 :
                résistance.append(Types[i])
            if t1[i] == 1 :
                neutre.append(Types[i])
            if t1[i] == 2 :
                faiblesse.append(Types[i])
            if t1[i] == 0 :
                immunité.append(Types[i])
        print('A type attack ',a,'will be ineffective against types',str(résistance)[1:-1],' but will be super effective on types ',str(faiblesse)[1:-1],'.')
        if (len(immunité)) != 0 :
            print("The attack will be fully effective on a type pokémon", str(immunité)[1:-1],".")
    else :
        print('The type is unrecognized.')

def TypeChartDefense (*args):
    résistance = []
    doublerés = []
    neutre = []
    faiblesse = []
    doublefai = []
    immunité = []

    pk = 'A pokémon'

    if len(args) == 1 and args in Noms :
        pk = args[0]
        args = DétecteType(args[0])
        if args[1] == '' :
            a = args[0]
            b = None
        else :
            a = args[0]
            b = args[1]

    elif len(args) == 2 :
        a = args[0]
        b = args[1]
    elif len(args) == 1 and len(args[0]) != 2 :
        a = args[0]
        b = None
    elif len(args) > 2 :
        print('You can only enter two types maximum.')

    if b in Types :
        if a in TableDefense and b in TableDefense:
            t1=TableDefense.get(a)
            t2=TableDefense.get(b)
            for i in range (18) :
                if t1[i] == 1/2 and t2[i] == 1 or t1[i] == 1 and t2[i] == 1/2 :
                    résistance.append(Types[i])
                if t1[i] == 1/2 and t2[i] == 1/2 :
                    doublerés.append(Types[i])
                if t1[i] == 1 and t2[i] == 1 :
                    neutre.append(Types[i])
                if t1[i] == 1/2 and t2[i] == 2 or t1[i] == 2 and t2[i] == 1/2:
                    neutre.append(Types[i])
                if t1[i] == 2 and t2[i] == 1 or t1[i] == 1 and t2[i] == 2 :
                    faiblesse.append(Types[i])
                if t1[i] == 2 and t2[i] == 2 :
                    doublefai.append(Types[i])
                if t1[i] == 0 or t2[i] == 0 :
                    immunité.append(Types[i])

            if (len(résistance)) == 1 :
                print(pk,'having the double type',a,b,'will have a resistance to the type ',résistance[0],'.')
            if (len(résistance)) < 1 :
                print(pk,'having the double type',a,b,"will have no resistance.")
            if (len(résistance)) > 1 :
                print(pk,'having the double type',a,b,'will have several resistances against the types ', str(résistance)[1:-1],'.')
            if (len(doublerés)) == 1 :
                print('It also has a double resistance to type ',doublerés[0],'.')
            if (len(doublerés)) > 1 :
                print('It also has several double resistors against types ',str(doublerés)[1:-1],'.')

            if (len(faiblesse)) == 1 :
                print(pk,'having the double type',a,b,'will have a weakness to the type ',faiblesse[0],'.')
            if (len(faiblesse)) < 1 :
                print(pk,'having the double type',a,b,"will have no weakness.")
            if (len(faiblesse)) > 1 :
                print(pk,'having the double type',a,b,'will have several weaknesses against the types ',str(faiblesse)[1:-1],'.')
            if (len(doublefai)) == 1 :
                print('It also has a double weakness type ',doublefai[0],'.')
            if (len(doublefai)) > 1 :
                print('It also has several double weaknesses against the types ',str(doublefai)[1:-1],'.')

            if (len(neutre)) == 1 :
                print(pk,'having the double type',a,b, 'will have a neutrality ', neutre[0],'.')
            if (len(neutre)) > 1 :
                print(pk,'having the double type',a,b, 'will be neutral to the types', str(neutre)[1:-1],'.')

            if (len(immunité)) == 1 :
                print('The pokémon will have immunity to the type ',immunité[0],'.')
            if (len(immunité)) > 1 :
                print('Pokémon will have immunities to types ', str(immunité)[1:-1],'.')

    if b == None :
        if a in TableDefense :
            t1=TableDefense.get(a)
            for i in range (18) :
                if t1[i] == 1/2 :
                    résistance.append(Types[i])
                if t1[i] == 1 :
                    neutre.append(Types[i])
                if t1[i] == 2 :
                    faiblesse.append(Types[i])
                if t1[i] == 0 :
                    immunité.append(Types[i])

            if (len(résistance)) == 1 :
                print(pk,'of type',a,'will have a resistance to the type ',résistance[0],'.')
            if (len(résistance)) < 1 :
                print(pk,'of type',a,"will have no resistance.")
            if (len(résistance)) > 1 :
                print(pk,'of type',a,'will have several resistances against the types ', str(résistance)[1:-1],'.')

            if (len(faiblesse)) == 1 :
                print(pk,'of type',a,'will have a weakness to the type ',faiblesse[0],'.')
            if (len(faiblesse)) < 1 :
                print(pk,'of type',a,"will have no weakness.")
            if (len(faiblesse)) > 1 :
                print(pk,'of type',a,'will have several weaknesses against the types ',str(faiblesse)[1:-1],'.')

            if (len(neutre)) == 1 :
                print(pk,'of type',a, 'will be neutral ', neutre[0],'.')
            if (len(neutre)) > 1 :
                print(pk,'of type',a, 'will be neutral to the types', str(neutre)[1:-1],'.')

            if (len(immunité)) == 1 :
                print('The pokémon will have immunity to the type ',immunité[0],'.')
            if (len(immunité)) > 1 :
                print('Pokémon will have immunities to types ', str(immunité)[1:-1],'.')

    if a not in Types and a not in Noms :
        print('Type or pokémon not recognized.')

print("Content-type: text/html; charset=utf-8\n")

html =
<!DOCTYPE html>
<head>
    <meta charset="utf-8">
    <title>Version serveur</title>
    <link rel="stylesheet" href="styleonglet.css">
</head>
<body>
    <h1>The Pokemon XY-dex</h1>
	<center><p class="flotte"><img src="Oddish.gif"></p></center>
    <center><p1>Welcome to the XY-dex ! The data base pokemon until the gen 6 !</p1></center> <br>
    <p1>Check the different page of the <strong>pokedex</strong> and create <strong>your own team</strong> to receive your unofficial trainer degree !</p1>

    <br><br>

    <div>
	<button onclick="openTab(0)">Pokedex</button>
	<button onclick="openTab(1)">Regions</button>
	<button onclick="openTab(2)">Types</button>
    </div>

    <div class="mTOP10">
	    <div class="container">
		    <br>
<form action="#" method="post">
    <center>
        <input
            type="text"
            placeholder="Gotta Catch 'Em All"
            id="lookfor"
            name="lookfor"
            onchange="scrolltopokemon()">
        <center>Catch it !</center>
    </center>
</form>
		    <div class="scroll-bg">
                <div class="scroll-div">
                    <section class="pokemon-list">


cur.execute("SELECT ID_Interne, Number, Name, Type1, Type2, Total, HP, Attack, Defense, Sp_Atk, Sp_Def, Speed, Generation, Legendary, Artwork, Icone FROM POKEDEX")
pokemon_data = cur.fetchall()

for ID_Interne, Number, Name, Type1, Type2, Total, HP, Attack, Defense, Sp_Atk, Sp_Def, Speed, Generation, Legendary, Artwork, Icone in pokemon_data:
    if Legendary == True :
        legend = "Yes"
    else :
        legend = "No"
    icon_path = os.path.join('Icons', f"{Icone}")
    art_path = os.path.join('Artworks', f"{Artwork}")
    html += f
    <div id="{ID_Interne}" class="pokemon">
        <h1>{Name}</h1>
        <div class="pokemon">
            <p class="flotte"><img src="{art_path}" style="width:100%; height:auto" alt="{Name}"></p>
            <p><img src="{icon_path}" alt="{Name}"></p>
            <p><strong>Nationaldex number :</strong> {Number}<br> <strong>Type :</strong> {Type1} {Type2}<br><strong>Generation :</strong> {Generation}<br><strong>Legendary :</strong> {legend}<br><br><strong>Total stat :</strong> {Total}<br><strong>HP :</strong> {HP}<br><strong>Attack :</strong> {Attack}<br><strong>Defense :</strong>{Defense}<br><strong>Special Attack :</strong>{Sp_Atk}<br><strong>Special Defense :</strong>{Sp_Def}<br><strong>Speed :</strong>{Speed}<br></p>
        </div>
    </div>


html +=

                    </section>
                </div>
		    </div>
	    </div>

        <div class="container">
		    <div class="scroll-bg">
			    <div class="scroll-div">
			        <h2>- Kanto : 1G</h2>
	                <p>>Kanto is the first region of pokemon univers . Released on the 27 febuary  1996 in Japan with the Red and Green pokemon opus, there are 151 different pokemon. The most represented type of this region is the poison type with 33 pokemon followed by the water type with 32 pokemon.There are however less dragon and ice type.</p>
                    <center><img src="green.png"><img src="Kanto_LGPE.png"><img src="red.png"></center>
				    <h2>- Johto : 2G</h2>
	                <p>Johto is the region where takes place the Gold, Silver and Cristal opus and his remake Heartgold and Soulsilver. Players have the opportunity to discover it for the first time the 21 november 1999, it is the neighboring region of Kanto, situated on the ouest of her separated by the mount silvern, and they share the same league. This region introduced 100 new pokemon but share many pokemon with Kanto. The dominant type among the new types introduced is the flying type with 19 new entries and 18 water type but introduce just one ghost type despite the apparition of the dark and steel types.</p>
                    <center><img src="kris.png"><img src="1200px-Johto_HGSS.jpg"><img src="gold.jpg"></center>
				    <h2>- Hoenn : 3G</h2>
	                <p>Hoenn  is the third region and the first separate from the previous regions. Situated on the south-west of Johto and Kanto, on these marine sea roads we discover sapphire and ruby opus the 21 november 2002, as well as the complementary version emerald and his remake. This is the second region who introduce the most water type with 28 new apparition for just 4 electric type on this 134 new creatures.</p>
                    <center><img src="sapphir.png"><img src ="Carte_de_Hoenn_ROSA.png"><img src="rubis.png"></center>
				    <h2>- Sinnoh : 4G</h2>
	                <p>Sinnoh is the emblematic region of the fourth generation and Diamond, Pearl and Platinium opus and their remake. On the north of Kanto, Johto and Hoenn, as well as nearby of Fiore and Almia regions, Sinnoh has many commun point with the two first regions including the mysterious ruins Sinjoh or the composition of his mounds. We discover 106 pokemon including 14 legendary and fabulous. its always the region who introduiced the most  pokemon's mythical's of the licence. The least represented type is the fairy type with 2 pokemon and the most amazing is that the normal type is most represented with 16 pokemon.</p>
                    <center><img src="diam.png"><img src="Sinnoh-DEPS.png"><img src="perle.png"></center>
				    <h2>- Unys : 5G</h2>
	                <p>Unys is the first region not based on the Japan afetr 14 years ! Appeared with their Black and White opus the 18 september 2010, she undergoes many modification depending depending the chose version with the black city and the white forest. She introduced 155 new pokemon and don't representing on her earth none ancients pokemon, wanting to be like a total revival ! With a majority of flying, grass and bug type, she just representing 2 fairy type type and 7 ice type.</p>
                    <center><img src="ludvina.png"><img src="Unys_-_NB.png"><img src="hilbert.png"></center>
				    <h2>- Kalos : 6G</h2>
	                <p>Kalos was inspirated by the French metropole ! And the first region to have the 3D with the X and Y games realesed the 12 october 2013. Although openly incomplete with the great mystery of southern Kalos, the sixth generation introduced the fairy type and 17 new dragon type. She introduce just 72 new minster but compensates with compensates with his 43 mega-evolution, a new form for ancient pokemon.</p>
                    <center><img src="Serena2.png"><img src="Kalos_-_XY.png"><img src="Calem2.png"></center><br>
			    </div>
		    </div>
	    </div>

        <div class="container">
		    <div class="scroll-bg">
                <div class="scroll-div">
		            <h2>- The types of pokemon :</h2>
		                <p>In the univers of pokemon, these creatures are classified by many means : group of eggs, morphology, generation... A means of classification takes precedence, however : <br>the classification by type.<br>
                        Pokemon, as different as they are, can be classified into 18 different types: <br><br>
		                <img src="NormalIC_Big.png" loading="lazy" style="width:10%; height:auto;"><img src="FireIC_Big.png" loading="lazy" style="width:10%; height:auto;"><img src="WaterIC_Big.png" loading="lazy" style="width:10%; height:auto;"><img src="ElectricIC_Big.png" loading="lazy" style="width:10%; height:auto;"><img src="GrassIC_Big.png" loading="lazy" style="width:10%; height:auto;"><img src="IceIC_Big.png" loading="lazy" style="width:10%; height:auto;"><img src="FightingIC_Big.png" loading="lazy" style="width:10%; height:auto;"><img src="PoisonIC_Big.png" loading="lazy" style="width:10%; height:auto;"><img src="GroundIC_Big.png" loading="lazy" style="width:10%; height:auto;"><br>
		                <img src="FlyingIC_Big.png" loading="lazy" style="width:10%; height:auto;"><img src="PsychicIC_Big.png" loading="lazy" style="width:10%; height:auto;"><img src="BugIC_Big.png" loading="lazy" style="width:10%; height:auto;"><img src="RockIC_Big.png" loading="lazy" style="width:10%; height:auto;"><img src="GhostIC_Big.png" loading="lazy" style="width:10%; height:auto;"><img src="DragonIC_Big.png" loading="lazy" style="width:10%; height:auto;"><img src="DarkIC_Big.png" loading="lazy" style="width:10%; height:auto;"><img src="SteelIC_Big.png" loading="lazy" style="width:10%; height:auto;"><img src="FairyIC_Big.png" loading="lazy" style="width:10%; height:auto;">
		            <br><br>
		                These 18 types have specific relationships listed in the types table. On a balance like rock-leaf-scissor  where types beat and are beaten by others, some types have immunities and non-reciprocal relationships between them.<br>
		                To add diversity and complexity, some pokemon can have a double type, who is like his name indicate a affiliation of two different type providing more diverse among the resistance's and weakness's.<br><br>
		                <img src="typechart.png" loading="lazy" style="width:100%; height:auto;"> <img src="chart.jpg" loading="lazy" style="width:90%; height:auto;"><br><br>
		                There are other types beyond this classification such as the Shadow Type, which is unique to the Shadow Pokemon in Pokemon Colosseum and Pokemon XD: Gale of Darkness, where they are at the heart of the plot. There is also the type "bird", type bug of the first generation and attributed to the famous Missimino.<br>
		                <br><img src="UnknownIC_Big.png" loading="lazy" style="max-width:100%; height:auto;"><img src="Sprite_MissingNo._RV.png" loading="lazy" style="max-width:100%; height:auto;"><br>
		                <p>You should know that not all types of appeared in the first generation: in the Pokemon Red, Green and Blue opus, there were only 15 types (and the bird type). The second generation brings two new types: the dark type and the steel type, counterbalancing the dominant types of the first generation either the psy type and the poison type. Finally, years later, with the passage of 3D, XY reveals the fairy type, destroying the powerful dragons until then master. Nymphaly is the first fairy-type pokemon to be revealed.</p>
                    <br><br>
                    <h2>- Type selector :</h2>
                        <p>Select one or two type to see their traits :</p>

                </div>
		    </div>
	    </div>
    </div>

    <script src="function openTab(x){
    let contents = document.querySelectorAll(".container");
    let btns = document.querySelectorAll("button");
    for (let i =0; i < contents.length; i++){
        contents[i].style.display = "none";
        btns[i].classList.remove("active");
    }
    contents[x].style.display ="block";
    btns[x].classList.add("active");
}

function scrolltopokemon() {
    var input, filter, div, pokemon, i;
    input = document.getElementById('lookfor');
    filter = input.value.toUpperCase();
    div = document.getElementsByClassName('pokemon-list')[0];
    pokemon = div.getElementsByClassName('pokemon');

    console.log('Filter:', filter);

    for (i = 0; i < pokemon.length; i++) {
        console.log('Pokemon ID:', pokemon[i].id.toUpperCase());

        if (pokemon[i].id.toUpperCase().indexOf(filter) > -1) {
            pokemon[i].scrollIntoView({ behavior: 'smooth', block: 'start' });
            return;
        }
    }
}

        function submitData() {
            var type1 = $('#type1').val();
            var type2 = $('#type2').val();

            $.ajax({
                url: 'http://localhost:8000/submit',
                type: 'POST',
                data: {type1: type1, type2: type2},
                success: function(response) {
                    console.log(response);
                },
                error: function(error) {
                    console.log(error);
                }
            });
        }

openTab(0)"></script>

</body>
</html>


print(html)