import csv

# no gay here, gender eliminaatory


# the dictionnaire infos contient les champs qui vont nous permettre de faire nos match.
# en key le nom des champs, en value une liste qui comporte le score attribue, et l'index correspondant a la position du champs dans le  csv

infos =	 {
	'id': [0, 0], 'gender': [0, 0], 'age': [40, 0], 'field_cd': [40, 0], 'undergra': [30, 0 ], 'imprace': [70, 0],
    'imprelig': [70, 0], 'from': [40, 0], 'zipcode': [20, 0], 'income': [40, 0], 'goal': [80, 0], 'date': [30, 0], 'go_out': [30, 0],
    'career_c' : [40, 0] , 'sport': [60, 0], 'tvsports': [30, 0], 'excercise': [50, 0], 'dining': [50, 0], 'museums': [30, 0], 'art': [40, 0],
    'hiking': [20, 0], 'gaming': [30, 0], 'clubbing': [40, 0], 'reading': [20, 0], 'tv': [30, 0], 'theater': [20, 0], 'movies': [20, 0],
    'concerts': [30, 0], 'music': [40, 0], 'shopping': [30, 0], 'yoga': [20, 0], 'exphappy': [60, 0], 'expnum': [90, 0],
    'match_es': [30, 0], 'length' : [20, 0], 'matchs' : []
	}

# simplement pour acceder plus lisiblement a la 1 ere et 2 eme dimension de notre liste contenue dans infos.
score_info = 0
index = 1

matching_minimum_score = 300

candidate_dict = {}
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

def FindMatch(candidate_dict):
	i = 0
	y = 0
	count = 0
	total = 0
	cpt = 0
	print len(candidate_dict), "--"
	print '________________________________________________'

	for keys, value in candidate_dict.iteritems():
		for keys_, value_ in candidate_dict.iteritems():
			if (keys != keys_):
				y = 0
				for x in value:
					if (value[x] == value_[x]):
						count += infos[x][index]
					y += 1
					total += count
				if count > 350:
					print "count ==", count
				count = 0
				cpt +=1
	print "total = ", (total / cpt)


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

toto = 0
for keys , number in candidate_dict.iteritems():
	#print keys
	toto += 1
