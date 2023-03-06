choise = input('Which template do you want? a,b or c')

Number = input('Number: ')
Measure_of_time = input('Measure of time: ')
Mode_of_Transportation = input('Mode of transportation: ')
Adj = input('Adjective: ')
Adj_2 = input('Adjective2: ')
Adj_3 = input('Adjective3: ')
Adj_4 = input('Adjective4: ')
Adj_5 = input('Adjective5: ')
Noun = input('Noun: ')
Color = input('Color: ')
Part_of_the_Body = input('Part of the body: ')
Verb = input('Verb: ')
Number2 = input('Number2: ')
Noun2 = input('Noun2: ')
Noun3= input('Noun3: ')
Part_of_the_Body_2 = input('Party of the body 2: ')
Noun4 = input('Noun4: ')

Silly_Word = input('Silly Word: ')
Name= input("Noun(Person's name): ")
Noun5 = input('Noun5: ')
Feeling= input('Adjective (Feeling): ')
Feeling2= input('Adjective (Feeling): ')
Animal= input('Animal: ')
Verb2= input('Verb: ')
Verb3= input('Verb (ending in ing)')
Adverb= input('Adverb (ending in ly)')
Color2= input('Color: ')
Animal2= input('Animal: ')
Number3= input('Number: ')
Place = input('Place: ')
MagicalCreature = input('Magical Creature (Plural)')
MagicalCreature2 = input('Magical Creature (Plural)2')
Roominahouse = input('Room in a House')
def template_1():
    
    print(f'It was about {Number} {Measure_of_time} ago when I arrived at the hospital in a {Mode_of_Transportation}. The hospital is a/an {Adj} place, there are a lot of {Adj_2} {Noun} here. There are nurses here who have {Color} {Part_of_the_Body}. If someone wants to come into my room I told them that they have to {Verb} first. I’ve decorated my room with {Number2} {Noun2}. Today I talked to a doctor and they were wearing a {Noun3} on their {Part_of_the_Body_2}. I heard that all doctors {Verb} {Noun4} every day for breakfast. The most {Adj_3} thing about being in the hospital is the {Silly_Word} {Noun} !')

if choise == 'a':
    template_1()

def template_2():
    
    print(f"This weekend I am going camping with {Name}. I packed my lantern, sleeping bag, and {Noun}. I am so {Feeling} to {Verb} in a tent. I am {Feeling2} we might see a(n) {Animal}, I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and {Verb2}. I have heard that the {Color} lake is great for {Verb3}. Then we will {Adverb} hike through the forest for {Number2} {Measure_of_time}. If I see a {Color2} {Animal2} while hiking, I am going to bring it home as a pet! At night we will tell {Number3} {Silly_Word} stories and roast {Noun2} around the campfire!!")

def template_3():
    print(f'Dear {Name}, I am writing to you from a {Adj} castle in an enchanted forest. I found myself here one day after going for a ride on a {Color} {Animal} in {Place}. There are {Adj_2} {MagicalCreature} and {Adj_3} {MagicalCreature2} here! In the {Roominahouse} there is a pool full of {Noun}. I fall asleep each night on a {Noun2} of {Noun3} and dream of {Adj_4} {Noun4}. It feels as though I have lived here for {Number} {Measure_of_time}. I hope one day you can visit, although the only way to get here now is {Verb3} on a {Adj_5} !!')