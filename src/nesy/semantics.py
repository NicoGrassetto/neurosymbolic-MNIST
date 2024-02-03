from abc import ABC, abstractmethod
import torch

class Semantics(ABC):

    @abstractmethod
    def conjunction(self, a, b):
        pass

    @abstractmethod
    def disjunction(self, a, b):
        pass

    @abstractmethod
    def negation(self, a):
        pass


class SumProductSemiring(Semantics):
    def conjunction(self, a, b):
        return a * b

    def disjunction(self, a, b):
        return a + b

    def negation(self, a):
        """
        Implements the "negation" operation of the semiring (usually subtraction from the identity).
        """
        return self.identity - a

class LukasiewiczTNorm(Semantics):
    def conjunction(self, a, b):
        """Implements the Lukasiewicz conjunction (and) operation."""
        return max(0, a + b - 1)

    def disjunction(self, a, b):
        """Implements the Lukasiewicz disjunction (or) operation."""
        return min(1, a + b)

    def negation(self, a):
        """Implements the Lukasiewicz negation (not) operation."""
        return 1 - a

class GodelTNorm(Semantics):
    def conjunction(self, a, b):
        """Computes the Gödel T-norm conjunction of two fuzzy values."""
        return torch.max(a + b - 1, 0)

    def disjunction(self, a, b):
        """Computes the Gödel T-norm disjunction of two fuzzy values."""
        return torch.min(a + b, 1)

    def negation(self, a):
        """Computes the Gödel T-norm negation of a fuzzy value."""
        return 1 - a

class ProductTNorm(Semantics):
    def conjunction(self, a, b):
        return a * b

    def disjunction(self, a, b):
        return max(a, b)

    def negation(self, a):
        return 1 - a