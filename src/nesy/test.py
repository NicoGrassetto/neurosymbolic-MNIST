from logic import ForwardChaining
from nesy.term import Term, Clause
from nesy.parser import parse_term, parse_program
from abc import ABC, abstractmethod
from collections import namedtuple

# Define the program
program = [parse_program("addition(X,Y,1) :- digit(X,0), digit(Y,1)."), 
           parse_program("addition(X,Y,1) :- digit(X,1), digit(Y,0).")]

# # Define the queries
# queries = [parse_term("addition(tensor(images,0), tensor(images,1), 0)")]

# # Create the logic engine and reason with the program and queries
# engine = ForwardChaining()
# results = engine.reason(program, queries)

# print("Results:")
# for result in results:
#     print(type(result))

# nicograssetto@Nicos-MacBook-Pro neurosymbolic-MNIST % export PYTHONPATH=$PYTHONPATH:/Users/nicograssetto/Documents/Github/neurosymbolic-MNIST/src
# (nesy) nicograssetto@Nicos-MacBook-Pro neurosymbolic-MNIST % export PYTHONPATH=$PYTHONPATH:/Users/nicograssetto/Documents/Github/neurosymbolic-MNIST/src/nesy





# # Define the program
# program = [parse_program("andAnimal(x) :- mammal(x)."), 
#            parse_program("waterAnimal(x) :- mammal(x), hasFins(x)."),
#            parse_program("flightAnimal(x) :- bird(x)."), 
#            parse_program("hasFur(x) :- mammal(x)."), 
#            parse_program("laysEggs(x) :- bird(x)."), 
#            parse_program("mammal(dog)."), 
#            parse_program("mammal(cat)."), 
#            parse_program("bird(eagle)."), 
#            parse_program("bird(chicken)."), 
#            parse_program("mammal(cat).")]
# print(f"Program has {len(program)} clauses.")

# # Define the queries
# queries = [parse_term("landAnimal(dog)")]
# # landAnimal(dog).  // Output: true
# # landAnimal(cat).  // Output: true
# # waterAnimal(dog).  // Output: false
# # waterAnimal(eagle).  // Output: false
# # flightAnimal(cat).  // Output: false
# # flightAnimal(eagle).  // Output: true
# print(f"Query: {queries}")

# # Create the logic engine and reason with the program and queries
# engine = ForwardChaining()
# results = engine.reason(program, queries)

