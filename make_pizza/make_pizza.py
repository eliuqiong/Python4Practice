import pizza

print("\nimport the whole file, and the result will be:\n--------------")
pizza.make_pizza(12,"pinnaple")
pizza.make_pizza(12,"pinnaple","apple","banana","pepperoni")


print("\nimport one function from the py file, and the result will be:\n--------------")
from pizza import make_pizza
make_pizza(12,"pinnaple")
make_pizza(12,"pinnaple","apple","banana","pepperoni")