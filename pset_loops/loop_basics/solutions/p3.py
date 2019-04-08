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
  sample_temps.update({f: c})

print(sample_temps)
"""
{91.4: 33.00000000000001, 
82.4: 28.000000000000004,
71.6: 21.999999999999996,
107.6: 42.0,
115.6: 46.44444444444444}
"""