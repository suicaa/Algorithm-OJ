from math import *
my_name = ' Liyancheng '
# 双引号和单引号的区别是啥
my_age = 24
my_height = round(sqrt(3)) #cm
# round 直接取整， 怎么取小数点一位或者两位？？
my_weight = 68 #kg
my_eyes = 'black'
my_teeth = 'white'
my_hair = 'black'

print(f"let's talk about {my_name}")
print(f"He is {my_height} m tall")
print(f"He is {my_weight} kg heavy")
print("Actually that is a little bit heavy")
print(f"He is got {my_eyes} eyes and {my_hair} hair")
print(f"His teeth are usually {my_teeth} depending on the coffee")

total = my_age + my_weight + my_height
print(f"If i add {my_age}, {my_height}, and {my_weight}, i get {total}")
