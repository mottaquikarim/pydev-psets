"""
Weather III - Describe Conditions
"""

# Repeat the same process as p1, using this new set of variables.


is_it_warm = True
is_it_humid = True
is_it_cold = False
is_it_icy = False
is_it_foggy = False
is_it_windy = False
is_it_overcast = True


is_it_summer_weather = is_it_warm and is_it_humid and not is_it_windy # True 
print(is_it_summer_weather) # True and True and not False == True


is_rain_coming = is_it_overcast or is_it_foggy or is_it_humid
print(is_rain_coming) # True or False or True == True


is_it_muggy = is_it_humid or is_it_foggy and is_it_warm
print(is_it_muggy) # True or False and True == True


do_i_need_coat = is_it_cold and is_it_overcast or is_it_windy
print(do_i_need_coat) # True or False and False == False
