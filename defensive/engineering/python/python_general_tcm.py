
# STRINGS PRINT

print("----S T R I N G S----")
print('\n')
print('HELLO WORLD') #with single quote
print("HELLO WORLD") #with double quote
print("""MULTI
LINE""") # multiline
print("PARTE DEL TEXTO"+" AGREGADO") #concatenate
print("\n") #next line, can be used with single quote as well
print("SALTO DE LINEA")
print('\n')

# MATH OPERATIONS PRINT

print("----M A T H----")
print('\n')
print(10 + 10) # suma
print(10 - 10) # resta
print(10 * 10) # multi
print(10 / 10) # division
print(10 ** 2) # exponent
print(50 / 6) # float, will get decimal values
print(50 // 6) # no float results, only integer
print('\n')

# VARIABLES PRINT

print("----V A R I A B L E S & M E T H O D S----")
print('\n')
var1 = "Texto Almancenado en variable"
print(var1)
print(var1.lower()) # all text in lowercase
print(var1.upper()) # all text in uppercase
print(var1.title()) # capital letters
print(len(var1)) # counts how many letters

name = "Esteban Brenes" # string
age = 31 # integer

# no concatena strings con integers, para que corra correctamente se debe agregar la palabra "str()" 
# y dentro del parentesis se ingresa la variable integer. 
print("Mi nombre es " + name + " y mi edad es " + str(age) + " years")

# increase a int variable

age += 1
print("edad nueva: " + str(age))
print('\n')

# FUNCTIONS

print("----F U N C T I O N S ----")
print('\n')

# function to concatenate strings and integers
def who(): # functions without parameters
    name = "Esteban" # local variable
    age = 30
    print("Mi nombre es " + name + " y mi edad es " + str(age) + " anhos")

who()

print(age) # this is to show the difference between the local and global variables
# here is using the global variable with the last value assigned.

# function to add integer value
def add_numbers(value):
    print(value + 25)

add_numbers(4)

# function with two values
def add_values(x,y):
    print(x + y)

add_values(8,7)

# function using the return statement
def return_func(a,b):
    return a * b # se puede usar el return como para capturar los datos, sin embargo va a necesitar la
# opcion print para que salga en pantalla.

return_func(7,7)
print(return_func(7,7))

# function to create a new line
def new_line():
    print('\n')

new_line()

# BOOLEAN EXPRESSIONS (TRUE OR FALSE)

print("---- B O O L E A N | E X P R E S S I O N S ----")
new_line()

bol1 = True
bol2 = 3*3 == 9 # the == value means that is EQUAL
bol3 = False
bol4 = 3*3 != 9 # the != means does not (se necesita implementar ! = juntos, aca lo convierte al nuevo  

print(bol1,bol2,bol3,bol4)
print(type(bol1)) # using the type option you can check what is the variable type that is in place

# RELATIONAL AND BOOLEAN OPERATORS

greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7

test_AND_true = (7 > 5) and (5 < 7) # will be TRUE
test_AND_false = (7 > 5) and (5 > 7) # will be FALSE
test_OR = (7 > 5) or (5 < 7) # will be TRUE, it only requires one parameter true to be true. 
test_NOT = not True # will be FALSE
new_line()

# CONDITIONAL STATEMENTS if/else

print("---- C O N D I T I O N A L | S T A T E M E N T S----")
new_line()    

def get_sms(sms):
    if sms >= 8:
        return "SMS sent..."
    else:
        return "No SMS to send..."

print(get_sms(5))
print(get_sms(9))

new_line()

def buy_something(age,money):
    if (age >=21) and (money >= 6):
        return "Purchase completed"
    elif (age >= 21) and (money < 6):
        return "Not enough money to buy"
    elif (age < 21) and (money >=6):
        return "Go away..."
    else: 
        return "Please come back later..."

print(buy_something(21,7))
print(buy_something(21,3))
print(buy_something(18,7))

new_line()

# LISTS
print("---- L I S T S ----")
new_line()

cars = ["toyota","fiat","honda","cooper"]
print(cars) # printing the entire list
print(cars[2]) # printing the position number 2
print(cars[1:3]) # printing all content in the list starting at position 1 and ending at position 2, it will not 
# count the last value we specified.
print(cars[:1]) # it will print all content but not the position specified. 
print(cars[1:]) # it will print all content but not the position specified.
print(cars[-1]) # it will print the last value of the list
print(len(cars)) # print the count of the list objects

cars.append("nissan") # add values to the list
print(cars)

cars.insert(2, "subaru") # add value on a specific position
print(cars) 

cars.pop() # it will remove the last item added
print(cars)

cars.pop(1) # it will remove the position specified
print(cars)

parts_of_cars = ["tire", "windows", "brake"]
catalog = cars + parts_of_cars # it is allowed to combine lists
print(catalog)

users = [["fabi",8],["juan",9],["odin",6]] # you can create a list inside of a list and it will maintain the same position order
user_to_retrieve = users[1][0] # it is retrieving the position 1 with the value 0. "juan"
print(user_to_retrieve)

user_to_retrieve = [1][0] = 56
print(user_to_retrieve)

new_line()

# TUPLES
print("---- T U P L E S ----") # are not mutable as lists
new_line()

# tuples are not mutable, so, functions like "append() and pop()" will not work. 
usa_score_system = ("a","b","c","d","f")
print (usa_score_system[3])

new_line()

print("----L O O P I N G----")
new_line()

# for -- start to finish of an iterate
food = ["rice","chicken","eggs"]
for X in food:
    print(X)

# while -- execute as long as we got a TRUE value

i = 0
while i < 10:
    print(i)
    i += 1

new_line()
# ADVANCED STRINGS
print("---- A D V A N C E D | S T R I N G S----")
new_line()

last_name = "Brenes"
print(last_name[0]) # first letter
print(last_name[-1]) # last letter
# different letters can be extracted using the index position

sentence = "La vida es una!"
print(sentence[:2])
print(sentence.split()) # it works as delimiter, the default one is a space

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)

sentence1 = "enjoy everyday until you 'die'" # you can use the single quote to inquote some text
print(sentence1)

sentence2 = "enjoy everyday until you \"die\"" # also double quote can be used, however it needs the scape character
print(sentence2)

space_sentence = "            vida      "
print(space_sentence.strip()) # it will use the default delimeter to understand. 

# match a value against the word, for this example, but the goal is to match something or not,
# the result will be boolean
print("A" in "Apple")
print("a" in "Apple")

letter = "A"
word = "Apple"
print(letter.lower() in word.lower()) 

# ways to concatenate strings, some of them works only on python 3
car_model = "Land Cruiser"
print("my car model is " + car_model)
print("my car model is {}.".format(car_model))
print("my car model is %s." %car_model)
print(f"my car model is {car_model}.")

new_line()

# DICTIONARIES - are generated like key/value pairs
print("----D I C T I O N A R I E S----")
new_line()

fiat_models = {"Ducato":2005, "500":2021} # normal list
print(fiat_models)

car_cost = {"Toyota": ["1992","2001","2017"],"Fiat": ["2005","2021"]} # dictionry with different values
print(car_cost)

fiat_models['Palio'] = ["2022"] # add a new key:value pair to the fiat_models dictionarie
print(fiat_models)

fiat_models.update({"Honda": ["2021"]}) # again it will add a new key/value pair to the dictionary
print(fiat_models)

print(fiat_models.get("Ducato")) # get one specific value inserting the key associated

