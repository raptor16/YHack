#places = ["New York", "Grenada", "New Orleans", "Barados", "Bahamas", "Fort Lauderdale", "Liberia", "AZS", "San Diego", "Montego", "Saint Maarten", "Puero Plata", "St. Lucia", "Aruba", "Bermuda", "Curacao", "Tampa", "Grand Cayman", "San Juan", "Charleston", "Cancun", "West Palm Beach", "Orlando", "Turks and Caicos Islands", "Santo Domingo", "Punta Cana", "La Romana", "San Francisco", "Los Angeles", "Fort Myers", "Las Vegas")


if age>36: 
# give smaller distances for points
#give points to more relazing vacation
#most points is 15
	places[1] += 4
	places[2] += 9
	places[3] += 3
	places[4] += 5
	places[5] += 9
	places[6] += 10
	places[7] += 12
	places[8] += 0
	places[9] += 7
	places[10] += 3
	places[11] += 13
	places[12] += 15
	places[13] += 14
	places[14] += 15
	places[15] += 12
	places[16] += 15
	places[17] += 8
	places[18] += 7
	places[19] += 6
	places[20] += 10
	places[21] += 1
	places[22] += 9
	places[23] += 4
	places[24] += 10
	places[25] += 12
	places[26] += 14
	places[27] += 14
	places[28] += 8
	places[29] += 9
	places[30] += 9
	places[31] += 3
else if age>20 and age<36	
	places[1] += 12
	places[2] += 9
	places[3] += 2
	places[4] += 7
	places[5] += 8
	places[6] += 10
	places[7] += 5
	places[8] += 0
	places[9] += 9
	places[10] += 9
	places[11] += 4
	places[12] += 15
	places[13] += 6
	places[14] += 10
	places[15] += 10
	places[16] += 13
	places[17] += 2
	places[18] += 5
	places[19] += 5
	places[20] += 3
	places[21] += 7
	places[22] += 13
	places[23] += 14
	places[24] += 8
	places[25] += 6
	places[26] += 13
	places[27] += 10
	places[28] += 9
	places[29] += 14
	places[30] += 3
	places[31] += 15

else 
# give greater distances more points 
# give points to more adventure and small points to relaxing
	places[1] += 3
	places[2] += 9
	places[3] += 2
	places[4] += 9
	places[5] += 10
	places[6] += 5
	places[7] += 7
	places[8] += 0
	places[9] += 9
	places[10] +=10
	places[11] += 11
	places[12] += 12
	places[13] += 7
	places[14] += 10
	places[15] += 10
	places[16] += 13
	places[17] += 13
	places[18] += 7
	places[19] += 8
	places[20] += 1
	places[21] += 12
	places[22] += 15
	places[23] += 12
	places[24] += 15
	places[25] += 12
	places[26] += 15
	places[27] += 10
	places[28] += 9
	places[29] += 8
	places[30] += 7
	places[31] += 4

if gender == "female":
	#give warm destinations points
	#most points is 15
	places[1] += 5
	places[2] += 7
	places[3] += 5
	places[4] += 10
	places[5] += 9
	places[6] += 5
	places[7] += 10
	places[8] += 0
	places[9] += 5
	places[10] += 8
	places[11] += 9
	places[12] += 12
	places[13] += 12
	places[14] += 12
	places[15] += 10
	places[16] += 10
	places[17] += 13
	places[18] += 10
	places[19] +=15
	places[20] +=6
	places[21] += 15
	places[22] += 15
	places[23] += 10
	places[24] += 14
	places[25] += 15
	places[26] += 15
	places[27] += 15
	places[28] += 4
	places[29] += 5
	places[30] += 6
	places[31] += 5

else:
	#give sportier coler destinations more points
	places[1] += 6
	places[2] += 9
	places[3] += 5
	places[4] += 9
	places[5] += 10
	places[6] += 7
	places[7] += 5
	places[8] += 0
	places[9] += 2
	places[10] +=10
	places[11] += 11
	places[12] += 11
	places[13] += 6
	places[14] += 3
	places[15] += 5
	places[16] += 12
	places[17] += 6
	places[18] += 9
	places[19] += 11
	places[20] += 10
	places[21] += 5
	places[22] += 8
	places[23] += 8
	places[24] += 7
	places[25] += 5
	places[26] += 11
	places[27] += 12
	places[28] += 4
	places[29] += 9
	places[30] += 4
	places[31] += 15

if timezone = "":
	# identify western then give points to camping and skiing trips
	# most points is 10
	places[1] += 1
	places[2] += 5
	places[3] += 3
	places[4] += 7
	places[5] += 6
	places[6] += 7
	places[7] += 2
	places[8] += 0
	places[9] += 3
	places[10] += 9
	places[11] += 7
	places[12] += 6
	places[13] += 7
	places[14] += 9
	places[15] += 2
	places[16] += 10
	places[17] += 10
	places[18] += 7
	places[19] += 8
	places[20] += 3
	places[21] += 4
	places[22] += 5
	places[23] += 5
	places[24] += 8
	places[25] += 8
	places[26] += 9
	places[27] += 10
	places[28] += 4
	places[29] += 3
	places[30] += 7
	places[31] += 3

else if timezone = "":
	# identify eastern and give points to warm and sunny
	places[1] += 3
	places[2] += 9
	places[3] += 2
	places[4] += 9
	places[5] += 10
	places[6] += 5
	places[7] += 8
	places[8] += 0
	places[9] += 10
	places[10] +=10
	places[11] += 4
	places[12] += 10
	places[13] += 5
	places[14] += 8
	places[15] += 10
	places[16] += 3
	places[17] += 7
	places[18] += 7
	places[19] += 3
	places[20] += 8
	places[21] += 4
	places[22] += 10
	places[23] += 5
	places[24] += 10
	places[25] += 10
	places[26] += 10
	places[27] += 9
	places[28] += 10
	places[29] += 10
	places[30] += 7
	places[31] += 4
else if timezone = "":
	# idnentify midwest, give points to warm and sunny
	places[1] += 3
	places[2] += 9
	places[3] += 2
	places[4] += 9
	places[5] += 10
	places[6] += 5
	places[7] += 8
	places[8] += 0
	places[9] += 10
	places[10] +=10
	places[11] += 4
	places[12] += 10
	places[13] += 5
	places[14] += 8
	places[15] += 10
	places[16] += 3
	places[17] += 7
	places[18] += 7
	places[19] += 3
	places[20] += 8
	places[21] += 4
	places[22] += 10
	places[23] += 5
	places[24] += 10
	places[25] += 10
	places[26] += 10
	places[27] += 9
	places[28] += 10
	places[29] += 10
	places[30] += 7
	places[31] += 4
else:
	# go to a cruise
	places[1] += 0
	places[2] += 10
	places[3] += 0
	places[4] +=6
	places[5] += 10
	places[6] += 5
	places[7] += 5
	places[8] += 0
	places[9] += 6
	places[10] +=9
	places[11] += 3
	places[12] += 10
	places[13] += 7
	places[14] += 8
	places[15] += 10
	places[16] += 7
	places[17] += 7
	places[18] += 7
	places[19] += 4
	places[20] += 4
	places[21] += 8
	places[22] += 9
	places[23] += 3
	places[24] += 6
	places[25] += 7
	places[26] += 8
	places[27] += 9
	places[28] += 8
	places[29] += 6
	places[30] += 2
	places[31] += 1
#if locale != lastnamecountry: # repeat this until you finish all 15 of the destinations
	#match lastnamecountry with the country list
	# give points to last name country
	# most points is 10

#if locales in places:
	#places[] = 0


#compare countries for which country has the greatest points
