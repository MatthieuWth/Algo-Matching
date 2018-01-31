import csv
from collections import defaultdict

# no gay here, gender eliminaatory


# the dictionnaire infos contient les champs qui vont nous permettre de faire nos match.
# en key le nom des champs, en value une liste qui comporte le score attribue, et l'index correspondant a la position du champs dans le  csv

infos =	 {
	'id': [0, 0], 'gender': [0, 0], 'age': [40, 0], 'field_cd': [40, 0], 'undergra': [30, 0 ], 'imprace': [70, 0],
    'imprelig': [70, 0], 'from': [40, 0], 'zipcode': [20, 0], 'income': [40, 0], 'goal': [80, 0], 'date': [30, 0], 'go_out': [30, 0],
    'career_c' : [40, 0] , 'sport': [60, 0], 'tvsports': [30, 0], 'excercise': [50, 0], 'dining': [50, 0], 'museums': [30, 0], 'art': [40, 0],
    'hiking': [20, 0], 'gaming': [30, 0], 'clubbing': [40, 0], 'reading': [20, 0], 'tv': [30, 0], 'theater': [20, 0], 'movies': [20, 0],
    'concerts': [30, 0], 'music': [40, 0], 'shopping': [30, 0], 'yoga': [20, 0], 'exphappy': [60, 0], 'expnum': [90, 0],
    'match_es': [30, 0], 'length' : [20, 0], 'matchs' : [[], 0]
	}

# simplement pour acceder plus lisiblement a la 1 ere et 2 eme dimension de notre liste contenue dans infos.
score_info = 0
index = 1

matching_minimum_score = 300

candidate_dict = defaultdict()
#

# check if the field already exists if not it create an ID related to the field.
# def isAlreadySet():

# creat an Id
# def setId():


def setField(line, Id):
	candidate_list = {}
	tab = [row for row in line]
	for key, value in infos.iteritems():
		candidate_list[key] = tab[value[index]]
	return candidate_list


#
#	Loop on all existing people and calcul the affinity of two people
#	depending on if they have enough things in common or not.
#
def FindMatch(candidate_dict):
	y = 0
	love_score = 0
	total = 0
	number_matchs = 0

	stop = 0

	for keys in candidate_dict.iteritems():
		candidate_dict[str(keys[0])]["matchs"] = []
		for keys_ in candidate_dict.iteritems():
			if (keys[0] != keys_[0]):
				y = 0
				for value in infos.iteritems():

					# Condition of the matchs
					# Special condition have been made for Age and Income.
					if (keys_[1][value[0]] != "" and keys[1][value[0]] != "" and value[0] == "age" and int(keys_[1][value[0]]) >= int(keys[1][value[0]]) - 5 and int(keys_[1][value[0]]) <= int(keys[1][value[0]]) + 5):
						love_score += infos[value[0]][index]
					elif (keys_[1][value[0]] != "" and keys[1][value[0]] != "" and value[0] == "income" and int(keys_[1][value[0]]) >= int(keys[1][value[0]]) - 2000 and int(keys_[1][value[0]]) <= int(keys[1][value[0]]) + 2000):
						love_score += infos[value[0]][index]
					elif (keys[1][value[0]] == keys_[1][value[0]]):
						love_score += infos[value[0]][index]
					y += 1
					total += love_score
				# Love score is the love panel to reach in order to match someone.
				if love_score > 845:
					number_matchs += 1
					new_node = [keys_, love_score]
					candidate_dict[str(keys[0])]["matchs"].append(new_node)
				love_score = 0
		print "Affinites trouvees pour le user", keys[0], " with ", number_matchs, " matchs"
		number_matchs = 0
		stop += 1
		# Stop when 400 profile are checked, you can change this condition in order to have more people to analyze.
		if stop == 400:
			break


#
#	Check that the match of the people is also in his match list.
#
def check_affinity(Id, curr):
	for x in candidate_dict[curr]["matchs"]:
		if (x[0][0] == Id):
			return 1

#
#	Get a list of best match of a profile.
#
def findBestMatch(Id):
	list_match = []
	for curr in candidate_dict[Id]["matchs"]:
		if (isinstance(curr, str)):
			continue
		else:
			list_match.append(curr[1])
	list_match.append(23)
	sorted(list_match, reverse=True)

#
#	Find best matchs of a profile.
#
def isThereLove(candidate_dict):
	for keys in candidate_dict.iteritems():
		for curr in candidate_dict[str(keys[0])]["matchs"]:
			if (curr[0][0] > str(0) and check_affinity(keys[0], curr[0][0])):
				findBestMatch(keys[0])
				continue


#
#	Get fields of the first line in data.csv
#
def getField(line):
	i = 0
	print 'line = ', line
	for field in line:
		for keys , number in infos.items():
				if field == keys:
					infos[field][index] = i
					print field, "---", infos[field][index]
		i += 1
	print infos

Id = 0


#
#	First part of the code executed. Open data.csv and launch the algorithme.
#
with open('data.csv', 'rb') as csvfile:
	data = csv.reader(csvfile, delimiter=',')
	for line in data:
		if Id == 0:
			getField(line)
		else:
			candidate_dict[str(Id)] = setField(line, Id)
			#print candidate_dict
		Id += 1
	FindMatch(candidate_dict)
	isThereLove(candidate_dict)
