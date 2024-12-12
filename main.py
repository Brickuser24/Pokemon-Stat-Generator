import requests as r
import random
import streamlit as st

pokemon=st.text_input(value="Bulbasaur",label="Pokemon Name")
level=st.text_input(value="1",label="Pokemon Level")

try:
	url = "https://pokeapi.co/api/v2/pokemon/" + pokemon.lower().rstrip().lstrip()
	data = r.get(url).json()
	name = data['name'].title()
	base_stats = {}
	for stat in data["stats"]:
		if stat["base_stat"]>=1 and stat["base_stat"]<=24:
			dice=2
		elif stat["base_stat"]>=25 and stat["base_stat"]<=44:
			dice=3
		elif stat["base_stat"]>=45 and stat["base_stat"]<=64:
			dice=4
		elif stat["base_stat"]>=65 and stat["base_stat"]<=94:
			dice=5
		elif stat["base_stat"]>=95 and stat["base_stat"]<=124:
			dice=6
		elif stat["base_stat"]>=125 and stat["base_stat"]<=154:
			dice=7
		elif stat["base_stat"]>=155 and stat["base_stat"]<=199:
			dice=8
		else:
			dice=12
		base_stats[stat["stat"]["name"]] = dice

	stats={}
	for stat in base_stats:
		stat_val=0
		for j in range(int(level)):
			stat_val+=random.randint(1,base_stats[stat])
		if stat == "hp":
			for j in range(int(level)):
				stat_val+=random.randint(1,base_stats[stat])
		stats[stat]=stat_val

	st.write(f"Level {level} {name}")
	st.write("Stats:")
	for i in ["hp","attack","special-attack","defense","special-defense","speed"]:
		st.write(f"D{base_stats[i]} | {i.title()}: {stats[i]}")

except:
	st.write("An Error occured")
	st.write("Please check the inputs")
