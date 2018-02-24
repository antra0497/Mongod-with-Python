
from pymongo import MongoClient

client = MongoClient()
db = client.primer
db.dataset

choice=1
while(choice == 1):
	def menu():
		print "Menu for Quries:"
	    print "Your options are as follows:"
	    print " "
	    print "1) Display all the documents in the collection restaurants."
	    print "2) Display the fields restaurant_id, name, borough and cuisine for all the documents in the collection restaurant."
	    print "3) Display the fields restaurant_id, name, borough and cuisine, but exclude the field _id for all the documents in the collection restaurant."
	    print "4) Display the fields restaurant_id, name, borough and zip code, but exclude the field _id for all the documents in the collection restaurant."
	    print "5) Display all the restaurant which is in the borough Bronx."
	    print "6) Display the first 5 restaurant which is in the borough Bronx."
	    print "7) Display the next 5 restaurants after skipping first 5 which are in the borough Bronx."
	    print "8) Find the restaurants who achieved a score more than 90."
	    print "9) Find the restaurants that achieved a score, more than 80 but less than 100."
	    print "10) Find the restaurants which locate in latitude value less than -95.754168."
	    print "11) Find the restaurants that do not prepare any cuisine of 'American' and their grade score more than 70 and latitude less than -65.754168."
	    print "12) Find the restaurants which do not prepare any cuisine of 'American' and achieved a score more than 70 and located in the longitude less than -65.754168"
	    print "13) Find the restaurants which do not prepare any cuisine of 'American ' and achieved a grade point 'A' not belongs to the borough Brooklyn"
	    print "14) Find the restaurant Id, name, borough and cuisine for those restaurants which contain 'Wil' as first three letters for its name"
	    print "15) Find the restaurant Id, name, borough and cuisine for those restaurants which contain 'ces'as last three letters for its name"
	    print "16) Find the restaurant Id, name, borough and cuisine for those restaurants which contain 'Reg' as three letters somewhere in its name."
	    print " "
     
    inp=int(input("Enter the query number you want answer of:"))

    if inp == 1:
    	solution()
    elif inp == 2:
    	solution(str({},{"restaurant_id" : 1,"name":1,"borough":1,"cuisine" :1}))
    elif inp == 3:
    	solution(str({},{"restaurant_id" : 1,"name":1,"borough":1,"cuisine" :1,"_id":0}))
    elif inp == 4:
    	solution(str({},{"restaurant_id" : 1,"name":1,"borough":1,"address.zipcode" :1,"_id":0}))
    elif inp == 5:
    	solution(str({"borough": "Bronx"}))			
    elif inp == 6:
    	solution(str({"borough": "Bronx"}, limit=5))
    elif inp == 7:
    	solution(str({"borough": "Bronx"}, skip=5, limit=5))
 	elif inp == 8:
    	solution(str({"grades.score": {"$gt":90} }))
 	elif inp == 9:
    	solution(str({"grades.score": { "$gt":80 ,"$lt":100 } } ))
 	elif inp == 10:
    	solution(str({"address.coord.0": { "$lt":-95.754168 } } ))
    elif inp == 11:
    	solution(str({"cuisine":{"$ne":"American"}},{"grades.score":{"$gt":70}} ,{"address.coord.0": { "$lt":-65.754168 } } ))
 	elif inp == 12:
    	solution(str({"cuisine":{"$ne":"American"}},{"grades.score":{"$gt":70}} ,{"address.coord.1": { "$lt":-65.754168 } }))
 	elif inp == 13:
    	solution(str("cuisine":{"$ne":"American"},"grades.grade":"A" ,"borough":{"$ne":"Brooklyn"}, sort=[("cuisines",-1)] ))
 	elif inp == 14:
    	solution(str({ "name": {"$regex": "^Wil"} }, {"restaurant_id" : 1,"name":1,"borough":1,"cuisine" :1} ))	
    elif inp == 15:
    	solution(str({ "name": {"$regex": "ces$"} }, {"restaurant_id" : 1,"name":1,"borough":1,"cuisine" :1} ))
 	elif inp == 16:
    	solution(str("name": {"$regex": "Reg"},{"restaurant_id" : 1,"borough":1,"cuisine" :1,"_id":0}))	

    choice=int(input("Do you want to continue? Enter 0: To quit, 1: To continue"))	


def solution(opt):
	selected= db.restaurants.find(opt)
	if selected.count()==0:
		print("No record found")
	for doc in selected:
		print(doc)



	






