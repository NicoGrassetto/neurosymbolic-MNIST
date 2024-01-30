from nesy.term import Term, Clause
from nesy.parser import parse_term, parse_program
from abc import ABC, abstractmethod
from collections import namedtuple

class LogicEngine(ABC):

    @abstractmethod
    def reason(self, program: list[Clause], queries: list[Term]):
        pass

class ForwardChaining(LogicEngine):

    def reason(self, program: tuple[Clause], queries: list[Term]):
        # TODO: Implement this

        # Dummy example:

        query = parse_term("addition(tensor(images,0), tensor(images,1), 0)")


        Or = lambda x:  None
        And = lambda x: None
        Leaf = lambda x: None
        and_or_tree = Or([
            And([
                Leaf(parse_term("digit(tensor(images,0), 0)")),
                Leaf(parse_term("digit(tensor(images,1), 0)")),
            ])
        ])

        return and_or_tree
    
# print("Hello World")
# from nesy.term import Term, Clause
# from nesy.parser import parse_term, parse_program
# from abc import ABC, abstractmethod
# from collections import namedtuple

# class LogicEngine(ABC):

#     @abstractmethod
#     def reason(self, program: list[Clause], queries: list[Term]):
#         pass

# class ForwardChaining(LogicEngine):

#     def reason(self, program: tuple[Clause], queries: list[Term]):
#         # Implement forward chaining algorithm here

#         # Create a set of known facts
#         known_facts = set()

#         # Add the initial facts to the known facts
#         for fact in program:
#             known_facts.add(fact.head)

#         # Iterate through the queries
#         for query in queries:
#             # Initialize a queue to store new facts to be discovered
#             to_check = [query]

#             # Loop until there are no more facts to check
#             while to_check:
#                 fact = to_check.pop()

#                 # Check if the fact is already known
#                 if fact not in known_facts:
#                     # Find applicable rules for the fact
#                     applicable_rules = []
#                     for rule in program:
#                         if fact in rule.body:
#                             applicable_rules.append(rule)

#                     # Apply applicable rules and add the new facts to the queue
#                     for rule in applicable_rules:
#                         for new_fact in rule.head:
#                             if new_fact not in known_facts:
#                                 to_check.append(new_fact)
#                                 known_facts.add(new_fact)

#         # Construct the AND-OR tree from the known facts
#         Or = lambda x:  None
#         And = lambda x: None
#         Leaf = lambda x: None
#         and_or_tree = Or([
#             And([
#                 Leaf(fact) for fact in known_facts
#             ])
#         ])

#         return and_or_tree