choise = input('Which template do you want? a,b or c')

Num = input('Number: ')
Num_2 = input('Number2: ')
Measure_time = input('Measure of time: ')
Mode_Transport = input('Mode of transportation: ')
Adj = input('Adjective: ')
Adj_2 = input('Adjective2: ')
Adj_3 = input('Adjective3: ')
Adj_4 = input('Adjective4: ')
Adj_5 = input('Adjective5: ')
Noun = input('Noun: ')
Noun_2 = input('Noun2: ')
Noun_3= input('Noun3: ')
Noun_4 = input('Noun4: ')
Noun_5 = input('Noun5: ')
Color = input('Color: ')
Color_2= input('Color: ')
Part_Body = input('Part of the body: ')
Part_Body_2 = input('Party of the body 2: ')
Silly_Word = input('Silly Word: ')
Name= input("Noun(Person's name): ")
Feel= input('Adjective (Feeling): ')
Feel_2= input('Adjective (Feeling): ')
Animal= input('Animal: ')
Animal_2= input('Animal: ')
Verb = input('Verb: ')
Verb_2= input('Verb: ')
Verb_3= input('Verb (ending in ing)')
Adverb= input('Adverb (ending in ly)')
Place = input('Place: ')
Magic_Creature = input('Magical Creature (Plural)')
Magic_Creature_2 = input('Magical Creature (Plural)2')
Room_house = input('Room in a House')

def template_1():
    
    print(f'It was about {Num} {Measure_time} ago when I arrived at the hospital in a {Mode_Transport}. The hospital is a/an {Adj} place, there are a lot of {Adj_2} {Noun} here. There are nurses here who have {Color} {Part_Body}. If someone wants to come into my room I told them that they have to {Verb} first. I’ve decorated my room with {Num_2} {Noun_2}. Today I talked to a doctor and they were wearing a {Noun_3} on their {Part_Body_2}. I heard that all doctors {Verb} {Noun_4} every day for breakfast. The most {Adj_3} thing about being in the hospital is the {Silly_Word} {Noun_5} !')

def template_2():
    
    print(f"This weekend I am going camping with {Name}. I packed my lantern, sleeping bag, and {Noun}. I am so {Feel} to {Verb} in a tent. I am {Feel_2} we might see a(n) {Animal}, I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and {Verb_2}. I have heard that the {Color} lake is great for {Verb_3}. Then we will {Adverb} hike through the forest for {Num} {Measure_time}. If I see a {Color_2} {Animal_2} while hiking, I am going to bring it home as a pet! At night we will tell {Num_2} {Silly_Word} stories and roast {Noun_2} around the campfire!!")

def template_3():
    print(f'Dear {Name}, I am writing to you from a {Adj} castle in an enchanted forest. I found myself here one day after going for a ride on a {Color} {Animal} in {Place}. There are {Adj_2} {Magic_Creature} and {Adj_3} {Magic_Creature_2} here! In the {Room_house} there is a pool full of {Noun}. I fall asleep each night on a {Noun_2} of {Noun_3} and dream of {Adj_4} {Noun_4}. It feels as though I have lived here for {Num} {Measure_time}. I hope one day you can visit, although the only way to get here now is {Verb_3} on a {Adj_5} !!')

if choise == 'a':
    template_1()
elif choise == 'b':
    template_2()
elif choise == 'c':
    template_3()