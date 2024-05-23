import pizza
# imports the entire module and all of its functions
from pizza import make_pizza
# a way to import just the function into your program
from pizza import make_pizza as mp
# gives the function a nickname that can be called
import pizza as p
# gives the module a nickname that can be called
from pizza import *
# tells python to import all functions from module, NOT RECOMMENDED
# these can then be called without the (dot) notation

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# (dot) notation is necessary when the entire module is imported

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# using the (dot) notation is not necessary when the function itself is imported

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
# the nickname for the function can be called

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# the nickname for the module can be called
