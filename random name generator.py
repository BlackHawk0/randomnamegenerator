'''Build vesion 1.o created by Malibu for the group skill ratz
#The entire code is open source and free to use and alter
#For further help or inquiries hoola @malibu_inc twitter

'''


import random
girl_names={
	'a':[
	'aubrie',
	'alani',
	'aisha',
	'azalea',
	'alanna',
	'Aurora',
	'Savannah',
	'Audrey',
	'Brooklyn',
	'Bella',
	'Claire',
	'brianna',
	'brielle',
	'bridget',
	'christine',
	'chrissy',
	'christine',
	'Nova',
	'Genesis',
	'Emilia',
	'Kennedy',
	'Samantha',
	'Maya',
	'Willow',
	'Kinsley',
	'Skylar',
	'Lucy',
	'Paisley',
	'Everly',
	'Anna',
	'Caroline'],
	'b':[
	'aubrie',
	'alani',
	'aisha',
	'azalea',
	'alanna',
	'Aurora',
	'Savannah',
	'Audrey',
	'Brooklyn',
	'Bella',
	'brianna',
	'brielle',
	'bridget',
	'christine',
	'chrissy',
	'christine',
	'Nova',
	'Genesis',
	'Emilia',
	'Kennedy',
	'Samantha',
	'Maya',
	'Willow',
	'Kinsley',
	'Claire',
	'Skylar',
	'Lucy',
	'Paisley',
	'Everly',
	'Anna',
	'Caroline'],
	
}
boy_names={
	'a':[
	'allan',
	'aston',
	'arifith',
	 'Jacob',
 	'Michael',
	'n',
	'Shawn',
	'Danie',
	'Alex',
	'Ryan',
	'David',
	'Christopher',
	'Matthew',
	'Joseph',
	'Jack',
	'Alexandr',
	'Jordan',
	'yler',
	'evin',
	'lan',
	'Adam'],
	'b':[
	'cruiz',
	'party'
		'n',
	'Shawn',
	'Danie',
	'Alex',
	'Ryan',
	'David',
	'Christopher',
	'Matthew',
	'Joseph',
	'Jack',
	'Alexandr',
	'Jordan',
	'yler',
	'evin',
	'lan'],
}

choice = raw_input("Type ...*1*..... for boy names or ........*2*...... for girl names\n")
if choice == '1':
	print(random.choice(boy_names['a']))
	question = raw_input("Did you like it type 1 else type 2 to generate another name\n")
	if question == 1:
		print("Thank you for choosing a baby")
	else:
		while question == '2':
			print(random.choice(boy_names['b']))
			view = raw_input("Did you like it type 1 else type 2 to generate another name\n")
			if view == '1':
				print("***THANK YOU FOR CHOOSING A BABY NAME AT MALIBU INCREDIBLE")
				break
else:
	if choice == '2':
		print(random.choice(girl_names['a']))
		question = raw_input("Did you like it type 1 else type 2 to generate another name\n")
		if question == 1:
			print("Thank you for choosing a baby")
		else:
			while question == '2':
				print(random.choice(girl_names['b']))
				view = raw_input("Did you like it type 1 else type 2 to generate another name\n")
				if view == '1':
					print("***THANK YOU FOR CHOOSING A BABY NAME AT MALIBU INCREDIBLE")
					break