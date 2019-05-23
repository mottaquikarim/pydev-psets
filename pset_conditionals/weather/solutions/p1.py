"""
Weather I - Do you need boots?
"""

# Use the values of the vars defined below to ouput the correct contextual answer to the questions below. (Note: The variables themselves ARE the questions.)

# Example:
## am_i_hungry = False
## am_i_tired = True
## do_i_need_to_stay_awake = False

## should_i_drink_coffee_now = am_i_tired and do_i_need_to_stay_awake

## ^^ This ^^ evaluates to False. If you're tired and don't need to stay awake, you don't need to drink coffee!


is_it_raining = True
is_it_snowing = False


do_i_need_snow_boots = is_it_snowing # False
print(do_i_need_snow_boots)

can_i_skip_snow_boots = not is_it_snowing # True
print(can_i_skip_snow_boots)

do_i_need_rain_boots = is_it_raining # True
print(do_i_need_rain_boots)

can_i_skip_rain_boots = not is_it_raining # False
print(can_i_skip_rain_boots)