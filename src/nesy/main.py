import nesy
from nesy.parser import parse_term, parse_program
# Create a program and a query
program = parse_program("""
fact(digit(tensor(images, 0), 1)).
fact(digit(tensor(images, 1), 2)).
rule(addition(tensor(images, A), tensor(images, B), C) :- digit(tensor(images, A), a), digit(tensor(images, B), b), C = a+b).
""")
query = parse_term("addition(tensor(images, 0), tensor(images, 1), 0)")

# Create a logic engine
logic_engine = nesy.ForwardChaining()

# Reason about the program and query
and_or_tree = logic_engine.reason(program, [query])

# Print the AND-OR tree
print(and_or_tree)