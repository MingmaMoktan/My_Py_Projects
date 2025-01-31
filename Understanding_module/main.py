import first_module

import my_package.my_math as mm

from other.other_stuff import stuff

import other.other_module as om

x = mm.add(2,3)
print(x)

y = stuff(2,2)
print(y)

z = om.function_from_other_module()
print(z)