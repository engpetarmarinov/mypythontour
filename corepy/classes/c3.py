"""
C3 Method Resolution Order ensures that:

* Subclasses come before base classes
* Base class order from class definition is preserved
* The first two qualities are preserved for all MROs in a program

"""


class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, A, C):
    pass


"""
TypeError: Cannot create a consistent method resolution
order (MRO) for bases A, C
"""
