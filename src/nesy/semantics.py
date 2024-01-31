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
    # TODO: Implement this

    def conjunction(self, a, b):
        pass

    def disjunction(self, a, b):
        pass

    def negation(self, a):
        pass

class LukasieviczTNorm(Semantics):
    # TODO: Implement this

    def conjunction(self, a, b):
        pass

    def disjunction(self, a, b):
        pass

    def negation(self, a):
        pass

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
    # TODO: Implement this

    def conjunction(self, a, b):
        pass

    def disjunction(self, a, b):
        pass

    def negation(self, a):
        pass