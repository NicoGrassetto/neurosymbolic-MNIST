from nesy.term import Term, Clause
from nesy.parser import parse_term, parse_program
from abc import ABC, abstractmethod
from collections import namedtuple

class LogicEngine(ABC):

    @abstractmethod
    def reason(self, program: list[Clause], queries: list[Term]):
        pass

class ForwardChaining(LogicEngine):
    def reason(self, program: list[Clause], queries: list[Term]):
        known_facts = set(queries)
        while True:
            new_facts = set()
            for clause in program:
                if clause[0].head in known_facts:
                    for body_term in clause[0].body:
                        substituted_term = body_term.substitute(clause.variable_mapping)
                        if substituted_term not in known_facts:
                            new_facts.add(substituted_term)
            if not new_facts:
                break
            known_facts.update(new_facts)
        return known_facts