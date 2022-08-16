#!/usr/bin/env python3
# python3 import_test.py - will print dummy module
import dummypackage
import dummypackage.subpackage
from dummypackage import dummymodule

print(dummypackage.__path__)
# _NamespacePath(['/Users/mpetar/devwork/github.com/engpetarmarinov/mypythontour
# /organizing_larger_programs/importing_modules/dummypackage'])
print(dummypackage.__file__)
# /Users/mpetar/devwork/github.com/engpetarmarinov/mypythontour/organizing_larger_programs/importing_modules/dummypackage/__init__.py
print(dummymodule.__file__)
# /Users/mpetar/devwork/github.com/engpetarmarinov/mypythontour/organizing_larger_programs/importing_modules/dummypackage/dummymodule.py
print(dummypackage.subpackage.__file__)
# /Users/mpetar/devwork/github.com/engpetarmarinov/mypythontour/organizing_larger_programs/importing_modules/dummypackage/subpackage/__init__.py
print(type(dummypackage))  # <class 'module'>
print(type(dummypackage.dummymodule))   # <class 'module'>

print(dummymodule.__name__)  # dummypackage.dummymodule
print(dummypackage.dummymodule.__name__)  # dummypackage.dummymodule
