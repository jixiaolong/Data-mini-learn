#!/usr/bin/python
#-*-encoding:utf8 -*-

users={
	"Angelica": {
			"Blues Traveler": 3.5, 
			"Broken Bells": 2.0, 
			"Norah Jones": 4.5, 
			"Phoenix": 5.0, 
			"Slightly Stoopid": 1.5, 
			"The Strokes": 2.5, 
			"Vampire Weekend": 2.0
			},
	"Bill": {
			"Blues Traveler": 2.0,
			"Broken Bells": 3.5,
			"Deadmau5": 4.0,
			"Phoenix": 2.0,
			"Slightly Stoopid": 3.5,
			"Vampire Weekend": 3.0},
	"Chan": {
			"Blues Traveler": 5.0,
			"Broken Bells": 1.0,
			"Deadmau5": 1.0,
			"Norah Jones": 3.0,
			"Phoenix": 5,
			"Slightly Stoopid": 1.0
			},
	"Dan": {
			"Blues Traveler": 3.0, 
			"Broken Bells": 4.0,
			"Deadmau5": 4.5,
			"Phoenix": 3.0,
			"Slightly Stoopid": 4.5, 
			"The Strokes": 4.0, 
			"Vampire Weekend": 2.0
			},
	"Hailey": {
			"Broken Bells": 4.0, 
			"Deadmau5": 1.0,
			"Norah Jones": 4.0,
			"The Strokes": 4.0,
			"Vampire Weekend": 1.0
			},
	"Jordyn":  {
			"Broken Bells": 4.5,
			"Deadmau5": 4.0,
			"Norah Jones": 5.0, 
			"Phoenix": 5.0,
			"Slightly Stoopid": 4.5,
			"The Strokes": 4.0, 
			"Vampire Weekend": 4.0
			},
	"Sam": {
			"Blues Traveler": 5.0,
			"Broken Bells": 2.0,
			"Norah Jones": 3.0, 
			"Phoenix": 5.0,
			"Slightly Stoopid": 4.0,
			"The Strokes": 5.0
			},
	"Veronica": {
				"Blues Traveler": 3.0, 
				"Norah Jones": 5.0,
				"Phoenix": 4.0,
				"Slightly Stoopid": 2.5,
				"The Strokes": 3.0
				}
}

def Euclidean(rating1,rating2):
	"""
	distance between rating1 and rating2
	"""		
	distance=0
	for key in rating1:
		if key in rating2:
			distance += abs(rating1[key]-rating2[key])*2
	
	return distance**(0.5)

def computeNearestNeighbor(username,users):
	"""
	create a sorted list of users based on their distance to username
	"""
	distance_list=[]
	for user in users:
		if user != username:
			distance=Euclidean(users[username],users[user])
			distance_list.append((user,distance))
	new_list=sorted(distance_list,key=lambda item: item[1])
	print "distance list",new_list
	return new_list

def recommend(username,users): 
	"""
	Give list of recommendation	
	"""
	nearest=computeNearestNeighbor(username,users)[0][0]
	recommendation_list=[]
	
	rating_nearest=users[nearest]
	rating_current=users[username]

	for key in rating_nearest:
		if not key in rating_current:
			recommendation_list.append(key)	

	return recommendation_list


if __name__ =="__main__":
	print "Euclidean test"
	for key in users:
		print 'user is ',key
	name1=raw_input("输入用户名1")	
	#name2=raw_input("输入用户名2")	
	#print "Euclidean result is %f"%Euclidean(users[name1],users[name2])
	#print "distance_list"
	#print '',computeNearestNeighbor(name1,users)
	print "recommendation list"
	print '',recommend(name1,users)
