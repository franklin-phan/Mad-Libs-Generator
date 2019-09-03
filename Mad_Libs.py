print('Welcome to Franklin \'s Mad Lib Generator')

class colors: 
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'
#pronouns list

pronouns_list = ['pronoun', 'pronoun', 'pronoun', 'pronoun']

pronouns_list[0] = input(colors.red +'Type your first and last name: ')
pronouns_list[1] = input(colors.red +'Type your city and state: ')
pronouns_list[2] = input(colors.red +'Type a friends name: ')
pronouns_list[3] = input(colors.red +'Type another friend\'s name: ')

#nouns list
nouns_list = ['noun','noun','noun','noun','noun','noun','noun','noun']

nouns_list[0] = input(colors.pink+ 'Type a noun: ')
nouns_list[1] = input(colors.pink+'Type a group of people: ')
nouns_list[2] = input(colors.pink+'Type a relationship i.e. brother: ')
nouns_list[3] = input(colors.pink+'Type a noun: ')
nouns_list[4] = input(colors.pink+'Type a body part: ')
nouns_list[5] = input(colors.pink+'Type a food item: ')
nouns_list[6]= input(colors.pink+'Type a popular chain restaurant: ')
nouns_list[7] = input(colors.pink+'Type an noun: ')

#verb list
verb_list = ['verb','verb','verb','verb','verb']

verb_list[0] = input(colors.blue+'Type a verb, past tense: ')
verb_list[1]= input(colors.blue+ 'Type a verb (ing): ')
verb_list[2] = input(colors.blue+ 'Type a verb, present tense: ')
verb_list[3] = input(colors.blue+ 'Type a verb, past tense: ')
verb_list[4] = input(colors.blue+ 'Type a verb (ing): ')

#adjectives list
adj_list = ['adjective','adjective','adjective','adjective','adjective','adjective']

adj_list[0] = input(colors.cyan+'Type an physical adjective: ')
adj_list[1] = input(colors.cyan+'Type an emotional adjective: ')
adj_list[2] = input(colors.cyan+'Type an physical adjective: ')
adj_list[3] = input(colors.cyan+'Type an physical adjective: ')
adj_list[4] = input(colors.cyan+'Type an emotional adjective: ')
adj_list[5] = input(colors.cyan+'Type an crazy adjective: ')

#adverbs list
adverbs_list = ['adverb','adverb','adverb','adverb','adverb']

adverbs_list[0] = input(colors.purple+'Type an adverb i.e wildly: ')
adverbs_list[1] = input (colors.purple+'Type an adverb: ')
adverbs_list[2] = input (colors.purple+'Type an adverb: ')
adverbs_list[3] = input (colors.purple+'Type an adverb: ')
adverbs_list[4]= input (colors.purple+'Type an adverb: ')

#Story inspired by Mad Libs book story "Weird News"
print(colors.red +pronouns_list[0],colors.lightgrey+'of',colors.red +pronouns_list[1],colors.lightgrey+'was arrested this morning after they',colors.purple+adverbs_list[0],colors.blue+verb_list[0],colors.lightgrey+'a',colors.cyan+adj_list[0],colors.pink+nouns_list[0],colors.lightgrey+'in front of some',colors.cyan+adj_list[1],colors.pink+nouns_list[1],colors.lightgrey+'.',colors.red +pronouns_list[0],\
colors.lightgrey+'had a history of', colors.purple+adverbs_list[1],colors.blue+verb_list[1],colors.lightgrey+'but no-one, not even \ntheir', colors.pink+nouns_list[2],colors.red +pronouns_list[2],colors.lightgrey+'ever imagined they would', colors.purple+adverbs_list[2],colors.blue+verb_list[2], colors.lightgrey+'with a',colors.cyan+adj_list[2],colors.pink+nouns_list[3], \
colors.lightgrey+ 'stuck in their', colors.pink+nouns_list[4],colors.lightgrey+'.',colors.lightgrey+'After eating some',colors.pink+nouns_list[5],colors.lightgrey+', cops followed them to a',colors.pink+nouns_list[6],colors.lightgrey+'\nwhere they reportedly',colors.purple+adverbs_list[3],colors.blue+verb_list[3],colors.lightgrey+'in the fry machine .',colors.lightgrey+'Police commissioner',\
colors.red +pronouns_list[3], colors.lightgrey+'says that after witnessing them',colors.purple+adverbs_list[4],colors.blue+verb_list[4],colors.lightgrey+'with a',colors.cyan+adj_list[3],colors.pink+nouns_list[7],colors.lightgrey+', \nthere are probably going to be a lot of',colors.cyan+adj_list[4],colors.pink+nouns_list[1],colors.lightgrey+'that are going to need some',\
colors.cyan+adj_list[5],colors.lightgrey+'therapy .')