from collections import namedtuple

"""
For now, until we don't find a better solution (e.g. a class?) use namedtuple.
Variable namedtuple fields have this meaning:
    1. name: Name of the variable (e.g. 'butler'). String
    2. index: position/order in which we consider the variable (e.g. 0). Int
    3. domain: possible states of the variable. Tuple of strings

Example usage:

butler = Variable('butler', 2, ('murderer', 'notmurderer')

More information: https://stackoverflow.com/a/2970722/6435921
Could also consider using dataclass for Python 3.7
"""
# Notice that because domain is going to be a tuple, the elements are ordered,
# So we don't need to explicitly say the index of each state.
Variable = namedtuple('Variable', ['name', 'index', 'domain'])


def order_variables(variable_list):
    """
    This function can be used to order Variable instances stored in some
    iterable, by index. When Variables will be implemented as a stand-alone
    class, this could just become a method.

    :param variable_list: Iterable containing Variable instances
    :type variable_list: list
    :return: Ordered list, based on Variable index
    :rtype: list
    """
    return sorted(variable_list, key=lambda x: x[0])


def index(variable: Variable, state: str) -> int:
    """
    This function takes a Variable instance and the name of a state in the
    domain of that variable and returns the index of that state.
    This should be implemented as a getter method in Variable class in the
    future.

    :param variable: Variable with a name, index and domain
    :type variable: Variable
    :param state: Name of the state for which we want the index
    :type state: str
    :return: Index of the state wrt the domain
    :rtype: int
    """
    return variable.domain.index(state)
