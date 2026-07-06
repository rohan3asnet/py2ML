#looping through an entire list
movies=['minions', 'main hoon lucky the racer', 'superman', 'batman', 'spiderman']
for movie in movies:# it tells python to pull a name form list and associate with variable movie
    print(movie) # it prints the name that is assigned to movie
    #for every movie in the list of movies, print the movie's name
 # also keep in mind you can choose any name you want 
 # for the  temporary variable that will be associated with each value in the list
 # but try to choose meaningful one 

#doing more work within a for loop
movies=['minions', 'main hoon lucky the racer', 'superman', 'batman', 'spiderman']
for movie in movies:
    print(f"{movie.title()} is a great movie.")
    print(f"I can't wait to see the sequel of {movie}.\n")
#doing something after a for loop
print("Every movie was Paisaa Vasoooool.")

#using the range() function
for value in range(1,7): # range() causes python to start counting at the first value i.e. 1
    #  and it stops when it reaches the second value i.e. 7
    # because it stops at second value, the output never contains the end value 
    print(value)

#using range() to make a list of numbers
num=list(range(1,6)) 
print(num)
even_num=list(range(2,11,2))#python uses third argument as a step size
print(even_num)# in this example, python adds 2 repeadedly untl it reaches or pass the end valuse 11

cubes=[]
for value in range(1,5):
    cube= value **3 # double ** is called exponent
    cubes.append(cube)
print(cubes)