# Python <3 FP: Breaking data down ➝ transforming it ➝ composing the result 
# List comprehension + map() are perfect for transforming filtered data concisely.
# zip() cleanly pairs data like names and stats or generations.
# NumPy shines for numeric ops — use np.sum and np.mean with axis=1 for row-wise/horizontal calcs.

poke_names = ['Abomasnow', 'Abra', 'Absol', 'Accelgor', 'Aerodactyl', 'Aggron', 'Aipom', 'Alakazam', 'Alomomola', 'Altaria', 'Amaura', 'Ambipom', 'Amoonguss', 'Ampharos', 'Anorith', 'Arbok', 'Arcanine', 'Arceus', 'Archen', 'Archeops', 'Ariados', 'Armaldo', 'Aromatisse', 'Aron', 'Articuno', 'Audino', 'Aurorus', 'Avalugg', 'Axew', 'Azelf', 'Azumarill', 'Azurill', 'Bagon', 'Baltoy', 'Banette', 'Barbaracle', 'Barboach', 'Basculin', 'Bastiodon', 'Bayleef', 'Beartic', 'Beautifly', 'Beedrill', 'Beheeyem', 'Beldum', 'Bellossom', 'Bellsprout', 'Bergmite', 'Bibarel', 'Bidoof', 'Binacle', 'Bisharp', 'Blastoise', 'Blaziken', 'Blissey', 'Blitzle', 'Boldore', 'Bonsly', 'Bouffalant', 'Braixen', 'Braviary', 'Breloom', 'Bronzong', 'Bronzor', 'Budew', 'Buizel', 'Bulbasaur', 'Buneary', 'Bunnelby', 'Burmy', 'Butterfree', 'Cacnea', 'Cacturne', 'Camerupt', 'Carbink', 'Carnivine', 'Carracosta', 'Carvanha', 'Cascoon', 'Castform', 'Caterpie', 'Celebi', 'Chandelure', 'Chansey', 'Charizard', 'Charmander', 'Charmeleon', 'Chatot', 'Cherrim', 'Cherubi', 'Chesnaught', 'Chespin', 'Chikorita', 'Chimchar', 'Chimecho', 'Chinchou', 'Chingling', 'Cinccino', 'Clamperl', 'Clauncher', 'Clawitzer', 'Claydol', 'Clefable', 'Clefairy', 'Cleffa', 'Cloyster', 'Cobalion', 'Cofagrigus', 'Combee', 'Combusken', 'Conkeldurr', 'Corphish', 'Corsola', 'Cottonee', 'Cradily', 'Cranidos', 'Crawdaunt', 'Cresselia', 'Croagunk', 'Crobat', 'Croconaw', 'Crustle', 'Cryogonal', 'Cubchoo', 'Cubone', 'Cyndaquil', 'Darkrai', 'DarmanitanStandard Mode', 'DarmanitanZen Mode', 'Darumaka', 'Dedenne', 'Deerling', 'Deino', 'Delcatty', 'Delibird', 'Delphox', 'Dewgong', 'Dewott', 'Dialga', 'Diancie', 'Diggersby', 'Diglett', 'Ditto', 'Dodrio', 'Doduo', 'Donphan', 'Doublade', 'Dragalge', 'Dragonair', 'Dragonite', 'Drapion', 'Dratini', 'Drifblim', 'Drifloon', 'Drilbur', 'Drowzee', 'Druddigon', 'Ducklett', 'Dugtrio', 'Dunsparce', 'Duosion', 'Durant', 'Dusclops', 'Dusknoir', 'Duskull', 'Dustox', 'Dwebble', 'Eelektrik', 'Eelektross', 'Eevee', 'Ekans', 'Electabuzz', 'Electivire', 'Electrike', 'Electrode', 'Elekid', 'Elgyem', 'Emboar', 'Emolga', 'Empoleon', 'Entei', 'Escavalier', 'Espeon', 'Espurr', 'Excadrill', 'Exeggcute', 'Exeggutor', 'Exploud', "Farfetch'd", 'Fearow', 'Feebas', 'Fennekin', 'Feraligatr', 'Ferroseed', 'Ferrothorn', 'Finneon', 'Flaaffy', 'Flabébé', 'Flareon', 'Fletchinder', 'Fletchling', 'Floatzel', 'Floette', 'Florges', 'Flygon', 'Foongus', 'Forretress', 'Fraxure', 'Frillish', 'Froakie', 'Frogadier', 'Froslass', 'Furfrou', 'Furret', 'Gabite', 'Gallade', 'Galvantula', 'Garbodor', 'Garchomp', 'Gardevoir', 'Gastly', 'Gastrodon', 'Genesect', 'Gengar', 'Geodude', 'Gible', 'Gigalith', 'Girafarig', 'Glaceon', 'Glalie', 'Glameow', 'Gligar', 'Gliscor', 'Gloom', 'Gogoat', 'Golbat', 'Goldeen', 'Golduck', 'Golem', 'Golett', 'Golurk', 'Goodra', 'Goomy', 'Gorebyss', 'Gothita', 'Gothitelle', 'Gothorita', 'Granbull', 'Graveler', 'Greninja', 'Grimer', 'Grotle', 'Groudon', 'GroudonPrimal Groudon', 'Grovyle', 'Growlithe', 'Grumpig', 'Gulpin', 'Gurdurr', 'Gyarados', 'Happiny', 'Hariyama', 'Haunter', 'Hawlucha', 'Haxorus', 'Heatmor', 'Heatran', 'Heliolisk', 'Helioptile', 'Heracross', 'Herdier', 'Hippopotas', 'Hippowdon', 'Hitmonchan', 'Hitmonlee', 'Hitmontop', 'Ho-oh', 'Honchkrow', 'Honedge', 'Hoothoot', 'Hoppip', 'Horsea', 'Houndoom', 'Houndour', 'Huntail', 'Hydreigon', 'Hypno', 'Igglybuff', 'Illumise', 'Infernape', 'Inkay', 'Ivysaur', 'Jellicent', 'Jigglypuff', 'Jirachi', 'Jolteon', 'Joltik', 'Jumpluff', 'Jynx', 'Kabuto', 'Kabutops', 'Kadabra', 'Kakuna', 'Kangaskhan', 'Karrablast', 'Kecleon', 'Kingdra', 'Kingler', 'Kirlia', 'Klang', 'Klefki', 'Klink', 'Klinklang', 'Koffing', 'Krabby', 'Kricketot', 'Kricketune', 'Krokorok', 'Krookodile', 'Kyogre', 'KyogrePrimal Kyogre', 'Kyurem', 'KyuremBlack Kyurem', 'KyuremWhite Kyurem', 'Lairon', 'Lampent', 'Lanturn', 'Lapras', 'Larvesta', 'Larvitar', 'Latias', 'Latios', 'Leafeon', 'Leavanny', 'Ledian', 'Ledyba', 'Lickilicky', 'Lickitung', 'Liepard', 'Lileep', 'Lilligant', 'Lillipup', 'Linoone', 'Litleo', 'Litwick', 'Lombre', 'Lopunny', 'Lotad', 'Loudred', 'Lucario', 'Ludicolo', 'Lugia', 'Lumineon', 'Lunatone', 'Luvdisc', 'Luxio', 'Luxray', 'Machamp', 'Machoke', 'Machop', 'Magby', 'Magcargo', 'Magikarp', 'Magmar', 'Magmortar', 'Magnemite', 'Magneton', 'Magnezone', 'Makuhita', 'Malamar', 'Mamoswine', 'Manaphy', 'Mandibuzz', 'Manectric', 'Mankey', 'Mantine', 'Mantyke', 'Maractus', 'Mareep', 'Marill', 'Marowak', 'Marshtomp', 'Masquerain', 'Mawile', 'Medicham', 'Meditite', 'MeowsticFemale', 'MeowsticMale', 'Meowth', 'Mesprit', 'Metagross', 'Metang', 'Metapod', 'Mew', 'Mewtwo', 'Mienfoo', 'Mienshao', 'Mightyena', 'Milotic', 'Miltank', 'Mime Jr.', 'Minccino', 'Minun', 'Misdreavus', 'Mismagius', 'Moltres', 'Monferno', 'Mothim', 'Mr. Mime', 'Mudkip', 'Muk', 'Munchlax', 'Munna', 'Murkrow', 'Musharna', 'Natu', 'Nidoking', 'Nidoqueen', 'Nidoran♀', 'Nidoran♂', 'Nidorina', 'Nidorino', 'Nincada', 'Ninetales', 'Ninjask', 'Noctowl', 'Noibat', 'Noivern', 'Nosepass', 'Numel', 'Nuzleaf', 'Octillery', 'Oddish', 'Omanyte', 'Omastar', 'Onix', 'Oshawott', 'Pachirisu', 'Palkia', 'Palpitoad', 'Pancham', 'Pangoro', 'Panpour', 'Pansage', 'Pansear', 'Paras', 'Parasect', 'Patrat', 'Pawniard', 'Pelipper', 'Persian', 'Petilil', 'Phanpy', 'Phantump', 'Phione', 'Pichu', 'Pidgeot', 'Pidgeotto', 'Pidgey', 'Pidove', 'Pignite', 'Pikachu', 'Piloswine', 'Pineco', 'Pinsir', 'Piplup', 'Plusle', 'Politoed', 'Poliwag', 'Poliwhirl', 'Poliwrath', 'Ponyta', 'Poochyena', 'Porygon', 'Porygon-Z', 'Porygon2', 'Primeape', 'Prinplup', 'Probopass', 'Psyduck', 'Pupitar', 'Purrloin', 'Purugly', 'Pyroar', 'Quagsire', 'Quilava', 'Quilladin', 'Qwilfish', 'Raichu', 'Raikou', 'Ralts', 'Rampardos', 'Rapidash', 'Raticate', 'Rattata', 'Rayquaza', 'Regice', 'Regigigas', 'Regirock', 'Registeel', 'Relicanth', 'Remoraid', 'Reshiram', 'Reuniclus', 'Rhydon', 'Rhyhorn', 'Rhyperior', 'Riolu', 'Roggenrola', 'Roselia', 'Roserade', 'Rotom', 'RotomFan Rotom', 'RotomFrost Rotom', 'RotomHeat Rotom', 'RotomMow Rotom', 'RotomWash Rotom', 'Rufflet', 'Sableye', 'Salamence', 'Samurott', 'Sandile', 'Sandshrew', 'Sandslash', 'Sawk', 'Sawsbuck', 'Scatterbug', 'Sceptile', 'Scizor', 'Scolipede', 'Scrafty', 'Scraggy', 'Scyther', 'Seadra', 'Seaking', 'Sealeo', 'Seedot', 'Seel', 'Seismitoad', 'Sentret', 'Serperior', 'Servine', 'Seviper', 'Sewaddle', 'Sharpedo', 'Shedinja', 'Shelgon', 'Shellder', 'Shellos', 'Shelmet', 'Shieldon', 'Shiftry', 'Shinx', 'Shroomish', 'Shuckle', 'Shuppet', 'Sigilyph', 'Silcoon', 'Simipour', 'Simisage', 'Simisear', 'Skarmory', 'Skiddo', 'Skiploom', 'Skitty', 'Skorupi', 'Skrelp', 'Skuntank', 'Slaking', 'Slakoth', 'Sliggoo', 'Slowbro', 'Slowking', 'Slowpoke', 'Slugma', 'Slurpuff', 'Smeargle', 'Smoochum', 'Sneasel', 'Snivy', 'Snorlax', 'Snorunt', 'Snover', 'Snubbull', 'Solosis', 'Solrock', 'Spearow', 'Spewpa', 'Spheal', 'Spinarak', 'Spinda', 'Spiritomb', 'Spoink', 'Spritzee', 'Squirtle', 'Stantler', 'Staraptor', 'Staravia', 'Starly', 'Starmie', 'Staryu', 'Steelix', 'Stoutland', 'Stunfisk', 'Stunky', 'Sudowoodo', 'Suicune', 'Sunflora', 'Sunkern', 'Surskit', 'Swablu', 'Swadloon', 'Swalot', 'Swampert', 'Swanna', 'Swellow', 'Swinub', 'Swirlix', 'Swoobat', 'Sylveon', 'Taillow', 'Talonflame', 'Tangela', 'Tangrowth', 'Tauros', 'Teddiursa', 'Tentacool', 'Tentacruel', 'Tepig', 'Terrakion', 'Throh', 'Timburr', 'Tirtouga', 'Togekiss', 'Togepi', 'Togetic', 'Torchic', 'Torkoal', 'Torterra', 'Totodile', 'Toxicroak', 'Tranquill', 'Trapinch', 'Treecko', 'Trevenant', 'Tropius', 'Trubbish', 'Turtwig', 'Tympole', 'Tynamo', 'Typhlosion', 'Tyranitar', 'Tyrantrum', 'Tyrogue', 'Tyrunt', 'Umbreon', 'Unfezant', 'Unown', 'Ursaring', 'Uxie', 'Vanillish', 'Vanillite', 'Vanilluxe', 'Vaporeon', 'Venipede', 'Venomoth', 'Venonat', 'Venusaur', 'Vespiquen', 'Vibrava', 'Victini', 'Victreebel', 'Vigoroth', 'Vileplume', 'Virizion', 'Vivillon', 'Volbeat', 'Volcanion', 'Volcarona', 'Voltorb', 'Vullaby', 'Vulpix', 'Wailmer', 'Wailord', 'Walrein', 'Wartortle', 'Watchog', 'Weavile', 'Weedle', 'Weepinbell', 'Weezing', 'Whimsicott', 'Whirlipede', 'Whiscash', 'Whismur', 'Wigglytuff', 'Wingull', 'Wobbuffet', 'Woobat', 'Wooper', 'WormadamPlant Cloak', 'WormadamSandy Cloak', 'WormadamTrash Cloak', 'Wurmple', 'Wynaut', 'Xatu', 'Xerneas', 'Yamask', 'Yanma', 'Yanmega', 'Yveltal', 'Zangoose', 'Zapdos', 'Zebstrika', 'Zekrom', 'Zigzagoon', 'Zoroark', 'Zorua', 'Zubat', 'Zweilous']
poke_gens = [4, 1, 3, 5, 1, 3, 2, 1, 5, 3, 6, 4, 5, 2, 3, 1, 1, 4, 5, 5, 2, 3, 6, 3, 1, 5, 6, 6, 5, 4, 2, 3, 3, 3, 3, 6, 3, 5, 4, 2, 5, 3, 1, 5, 3, 2, 1, 6, 4, 4, 6, 5, 1, 3, 2, 5, 5, 4, 5, 6, 5, 3, 4, 4, 4, 4, 1, 4, 6, 4, 1, 3, 3, 3, 6, 4, 5, 3, 3, 3, 1, 2, 5, 1, 1, 1, 1, 4, 4, 4, 6, 6, 2, 4, 3, 2, 4, 5, 3, 6, 6, 3, 1, 1, 2, 1, 5, 5, 4, 3, 5, 3, 2, 5, 3, 4, 3, 4, 4, 2, 2, 5, 5, 5, 1, 2, 4, 5, 5, 5, 6, 5, 5, 3, 2, 6, 1, 5, 4, 6, 6, 1, 1, 1, 1, 2, 6, 6, 1, 1, 4, 1, 4, 4, 5, 1, 5, 5, 1, 2, 5, 5, 3, 4, 3, 3, 5, 5, 5, 1, 1, 1, 4, 3, 1, 2, 5, 5, 5, 4, 2, 5, 2, 6, 5, 1, 1, 3, 1, 1, 3, 6, 2, 5, 5, 4, 2, 6, 1, 6, 6, 4, 6, 6, 3, 5, 2, 5, 5, 6, 6, 4, 6, 2, 4, 4, 5, 5, 4, 3, 1, 4, 5, 1, 1, 4, 5, 2, 4, 3, 4, 2, 4, 1, 6, 1, 1, 1, 1, 5, 5, 6, 6, 3, 5, 5, 5, 2, 1, 6, 1, 4, 3, 3, 3, 1, 3, 3, 5, 1, 4, 3, 1, 6, 5, 5, 4, 6, 6, 2, 5, 4, 4, 1, 1, 2, 2, 4, 6, 2, 2, 1, 2, 2, 3, 5, 1, 2, 3, 4, 6, 1, 5, 1, 3, 1, 5, 2, 1, 1, 1, 1, 1, 1, 5, 3, 2, 1, 3, 5, 6, 5, 5, 1, 1, 4, 4, 5, 5, 3, 3, 5, 5, 5, 3, 5, 2, 1, 5, 2, 3, 3, 4, 5, 2, 2, 4, 1, 5, 3, 5, 5, 3, 6, 5, 3, 4, 3, 3, 4, 3, 2, 4, 3, 3, 4, 4, 1, 1, 1, 2, 2, 1, 1, 4, 1, 1, 4, 3, 6, 4, 4, 5, 3, 1, 2, 4, 5, 2, 2, 1, 3, 3, 3, 3, 3, 6, 6, 1, 4, 3, 3, 1, 1, 1, 5, 5, 3, 3, 2, 4, 5, 3, 2, 4, 1, 4, 4, 1, 3, 1, 4, 5, 2, 5, 2, 1, 1, 1, 1, 1, 1, 3, 1, 3, 2, 6, 6, 3, 3, 3, 2, 1, 1, 1, 1, 5, 4, 4, 5, 6, 6, 5, 5, 5, 1, 1, 5, 5, 3, 1, 5, 2, 6, 4, 2, 1, 1, 1, 5, 5, 1, 2, 2, 1, 4, 3, 2, 1, 1, 1, 1, 3, 1, 4, 2, 1, 4, 4, 1, 2, 5, 4, 6, 2, 2, 6, 2, 1, 2, 3, 4, 1, 1, 1, 3, 3, 4, 3, 3, 3, 2, 5, 5, 1, 1, 4, 4, 5, 3, 4, 4, 4, 4, 4, 4, 4, 5, 3, 3, 5, 5, 1, 1, 5, 5, 6, 3, 2, 5, 5, 5, 1, 1, 1, 3, 3, 1, 5, 2, 5, 5, 3, 5, 3, 3, 3, 1, 4, 5, 4, 3, 4, 3, 2, 3, 5, 3, 5, 5, 5, 2, 6, 2, 3, 4, 6, 4, 3, 3, 6, 1, 2, 1, 2, 6, 2, 2, 2, 5, 1, 3, 4, 2, 5, 3, 1, 6, 3, 2, 3, 4, 3, 6, 1, 2, 4, 4, 4, 1, 1, 2, 5, 5, 4, 2, 2, 2, 2, 3, 3, 5, 3, 3, 5, 3, 2, 6, 5, 6, 3, 6, 1, 4, 1, 2, 1, 1, 5, 5, 5, 5, 5, 4, 2, 2, 3, 3, 4, 2, 4, 5, 3, 3, 6, 3, 5, 4, 5, 5, 2, 2, 6, 2, 6, 2, 5, 2, 2, 4, 5, 5, 5, 1, 5, 1, 1, 1, 4, 3, 5, 1, 3, 1, 5, 6, 3, 6, 5, 1, 5, 1, 3, 3, 3, 1, 5, 4, 1, 1, 1, 5, 5, 3, 3, 1, 3, 2, 5, 2, 4, 4, 4, 3, 3, 2, 6, 5, 2, 4, 6, 3, 1, 5, 5, 3, 5, 5, 1, 5]

gen1_gen2_name_lengths_loop = []
# print(list(zip(poke_names, poke_gens))[:5])
# print([*zip(poke_names, poke_gens)][:5])
# [
#     ('Abomasnow',   4),
#     ('Abra',        1),
#     ('Absol',       3),
#     ('Accelgor',    5),
#     ('Aerodactyl',  1)
# ]

# filter the Pokémon that belong to generation one or two, and collect the number of letters in each Pokémon's name
for name, gen in zip(poke_names, poke_gens):
  if gen < 3:
    name_length = len(name)
    poke_tuple = (name, name_length)
    gen1_gen2_name_lengths_loop.append(poke_tuple)

# Eliminate the above for loop using list comprehension and the map() function

# (1) Use list comprehension to collect each Pokémon that belongs to generation 1 or generation 2
# [output_if_true | for variable in iterable | if condition]
gen1_gen2_pokemon = [name for name, gen in zip(poke_names, poke_gens) if gen < 3]
# use the map() function to collect the number of letters in each Pokémon's name
name_lengths_map = map(len, gen1_gen2_pokemon) 
# Combine gen1_gen2_pokemon and name_lengths_map into a list
gen1_gen2_name_lengths = [*zip(gen1_gen2_pokemon, name_lengths_map)]

# print(gen1_gen2_name_lengths_loop[:5])
# print(gen1_gen2_name_lengths[:5])
# [
#     ('Abra',        4),
#     ('Aerodactyl', 10),
#     ('Aipom',       5),
#     ('Alakazam',    8),
#     ('Ampharos',    8)
# ]


#############

import numpy as np

num_pokemon = len(poke_names)
# Create random stats for each Pokémon: HP, Atk, Def, Sp.Atk, Sp.Def, Speed
# Values range roughly from 10 to 180 in real Pokémon stats
stats = np.random.randint(10, 181, size=(num_pokemon, 6))

poke_list = []

# print(list(zip(poke_names, stats))[:5])
# print([*zip(poke_names, stats)][:5])
# [
#     ('Abomasnow',   array([107, 102,  82, 145,  42,  54])),
#     ('Abra',        array([120, 126,  44, 138, 114, 178])),
#     ('Absol',       array([116, 134, 123,  25, 175, 146])),
#     ('Accelgor',    array([ 18, 119,  34, 163, 147, 133])),
#     ('Aerodactyl',  array([ 88, 171, 137, 130,  36,  74]))
# ]

# gather each Pokémon's total stat value (i.e., the sum of each row in stats) 
# and each Pokémon's average stat value (i.e., the mean of each row in stats) so that you find the strongest Pokémon.
for pokemon, row in zip(poke_names, stats):
	total_stats = np.sum(row)
	average_stats = np.mean(row)
	poke_list.append((pokemon, total_stats, average_stats))

# Eliminate the above for loop 

total_stats_np = np.sum(stats, axis=1)
avg_stats_np = np.mean(stats, axis=1)
poke_list_np = [*zip(poke_names, total_stats_np, avg_stats_np)]
# print(poke_list_np[:5])
# print(poke_list[:5])
# [
#     ('Abomasnow',  473,  78.83),
#     ('Abra',       528,  88.00),
#     ('Absol',      609, 101.50),
#     ('Accelgor',   526,  87.67),
#     ('Aerodactyl', 770, 128.33)
# ]
