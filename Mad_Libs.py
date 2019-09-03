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
pronouns_list = []

first_pronoun = input(colors.red +'Type your first and last name: ')
second_pronoun = input('Type your city and state: ')
third_pronoun = input('Type a friends name: ')
fourth_pronoun = input('Type another friend\'s name: ')

pronouns_list.append(first_pronoun)
pronouns_list.append(second_pronoun)
pronouns_list.append(third_pronoun)
pronouns_list.append(fourth_pronoun)
#nouns list
nouns_list = []

first_noun = input('Type a noun: ')
second_noun = input('Type a group of people: ')
third_noun = input('Type a relationship i.e. brother: ')
fourth_noun = input('Type a noun: ')
fifth_noun = input('Type a body part: ')
sixth_noun = input('Type a food item: ')
seventh_noun = input('Type a popular chain restaurant: ')
eighth_noun = input('Type an noun: ')



nouns_list.append(first_noun)
nouns_list.append(second_noun)

nouns_list.append(third_noun)
nouns_list.append(fourth_noun)
nouns_list.append(fifth_noun)
nouns_list.append(sixth_noun)
nouns_list.append(seventh_noun)
nouns_list.append(eighth_noun)


#verb list
verb_list = []

first_verb = input('Type a verb, past tense: ')
second_verb = input('Type a verb (ing): ')
third_verb = input('Type a verb, present tense: ')
fourth_verb = input('Type a verb, past tense: ')
fifth_verb = input('Type a verb (ing): ')

verb_list.append(first_verb)
verb_list.append(second_verb)
verb_list.append(third_verb)
verb_list.append(fourth_verb)
verb_list.append(fifth_verb)

#adjectives list
adj_list = []

first_adj = input('Type an physical adjective: ')
second_adj = input('Type an emotional adjective: ')
third_adj = input('Type an physical adjective: ')
fourth_adj = input('Type an physical adjective: ')
fifth_adj = input('Type an emotional adjective: ')
sixth_adj = input('Type an crazy adjective: ')

adj_list.append(first_adj)
adj_list.append(second_adj)
adj_list.append(third_adj)
adj_list.append(fourth_adj)
adj_list.append(fifth_adj)
adj_list.append(sixth_adj)


#adverbs list
adverbs_list = []

first_adverb = input('Type an adverb i.e wildly: ')
second_adverb = input ('Type an adverb: ')
third_adverb = input ('Type an adverb: ')
fourth_adverb = input ('Type an adverb: ')
fifth_adverb = input ('Type an adverb: ')

adverbs_list.append(first_adverb)
adverbs_list.append(second_adverb)
adverbs_list.append(third_adverb)
adverbs_list.append(fourth_adverb)
adverbs_list.append(fifth_adverb)


print(pronouns_list[0],'of',pronouns_list[1],'was arrested this morning after they',adverbs_list[0],verb_list[0],'a',adj_list[0],nouns_list[0],'in front of some',adj_list[1],nouns_list[1],'.',pronouns_list[0],\
'had a history of', adverbs_list[1],verb_list[1],'but no-one, not even their', nouns_list[2],pronouns_list[2],'ever imagined they would', adverbs_list[2],verb_list[2], 'with a',adj_list[2],nouns_list[3], \
'stuck in their', nouns_list[4],'.','After eating some',nouns_list[5],', cops followed them to a',nouns_list[6],'where they reportedly',adverbs_list[3],verb_list[3],'in the fry machine .','Police commissioner',\
pronouns_list[3], 'says that after witnessing them',adverbs_list[4],verb_list[4],'with a',adj_list[3],nouns_list[7],', there are probably going to be a lot of',adj_list[4],nouns_list[1],'that are going to need some',\
adj_list[5],'therapy .')





