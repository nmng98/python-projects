#GWC PROJECT
import random

career_list=["journalist", "chef", "filmmaker","graphic designer","architect","engineer"]
career_length=len(career_list)
random_index = random.randint(0, career_length)
def select(career_list):
	if career_list != []:
		pos = randrange( len(career_length) )
		elem = data[pos]
		data[pos] = data[-1]
		del data[-1]
		return elem
	else:
		return None

    
    
place_list=["San Francisco", "Los Angeles", "New York", "Tokyo", "Paris","London"]
place_length=len(place_list)
random_index = random.randint(0, place_length-1)
def select(place_list):
	if place_list != []:
		pos = randrange( len(place_length) )
		elem = data[pos]
		data[pos] = data[-1]
		del data[-1]
		return elem
	else:
		return None
    

residence_list=["shack","mansion","house","apartment","penthouse","hut"]
residence_length=len(residence_list)
random_index = random.randint(0, residence_length-1)
def select(residence_list):
	if residence_list != []:
		pos = randrange( len(residence_length))
		elem = data[pos]
		data[pos] = data[-1]
		del data[-1]
		return elem
	else:
		return None


print("I predict you will be a " + career_list[random_index] + " living in a " + residence_list[random_index] + " in " + place_list[random_index] + "." )

