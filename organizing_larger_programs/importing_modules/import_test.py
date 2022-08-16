#!/usr/bin/env python3
# python3 import_test.py - will print dummy module
import dummypackage
from dummypackage import dummymodule

print(dummypackage.__path__)
# _NamespacePath(['/Users/mpetar/devwork/github.com/engpetarmarinov/mypythontour
# /organizing_larger_programs/importing_modules/dummypackage'])

print(dummymodule.__name__)  # dummypackage.dummymodule
print(dummypackage.dummymodule.__name__)  # dummypackage.dummymodule

