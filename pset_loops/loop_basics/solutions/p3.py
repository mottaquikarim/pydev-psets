f"""
Temperature Conversions - SOLUTIONS
"""

# You're studying climate change, and over the last 3 years, you've recorded the temperature at noon every day in degrees Fahrenheit (F). The var sampleF holds a portion of those recordings. 

sampleF = [91.4, 82.4, 71.6, 107.6, 115.6]

# Convert each item in this list into degrees Celsius and add the results to a dict called sample_temps so that the conversion of each day's temperature is easily accessible (no need to round). For reference, the conversion equation between F and C is:
# Celsius = (Fahrenheit - 32) * 5.0/9.0

sample_temps = {}

for f in sampleF:
	c = (f - 32)*(5/9)
	sample_temps.update({f: format(c, '.2f')})

for k, v in sample_temps.items():
	print(f'{k} F -> {v} C')

"""
91.4 F -> 33.00 C
82.4 F -> 28.00 C
71.6 F -> 22.00 C
107.6 F -> 42.00 C
115.6 F -> 46.44 C
"""