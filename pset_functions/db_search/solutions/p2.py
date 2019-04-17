"""
RGB to HEX
"""

# Write a and call a function called "rgb_hex" that takes a parameter called "color." The function should be able to intake a color in rgb format and return it in hex format as well as vice versa. A sample of color conversions are below. Write in logic so the function can interpret rgb and hex colors entered in different formats such as "rgb_hex((255,255,255))" or "rgb_hex('ffffff')". Also make sure to account for someone inputting a color not in the database.

def rgb_hex(color):
  """this function converts a color in rgb to hex format and vice versa"""

  color_conversions = {
  '#4286f4': 'rgb(66, 134, 244)',
  '#5905c6': 'rgb(89, 5, 198)',
  '#fce702': 'rgb(252, 231, 2)',
  '#ffffff': 'rgb(255, 255, 255)',
  '#000000': 'rgb(0, 0, 0)',
  '#0ac913': 'rgb(10, 201, 19)',
  '#65c672': 'rgb(101, 198, 114)',
  '#f8d6ff': 'rgb(248, 214, 255)',
  '#b70782': 'rgb(183, 7, 130)',
  '#001184': 'rgb(0, 17, 132)',
  '#495eed': 'rgb(73, 94, 237)',
  '#b7ffb8': 'rgb(183, 255, 184)',
  '#ffbf00': 'rgb(255, 191, 0)',
  '#7a020e': 'rgb(122, 2, 14)',
  '#ff5e6e': 'rgb(255, 94, 110)',
  '#22003d': 'rgb(34, 0, 61)'
  }

  clean = None

  if isinstance(color,tuple) == True:
    clean = str(color)
    clean = 'rgb' + clean
    color = clean
  elif '#' not in color and 'rgb' not in color and len(color) == 6:
    clean = '#' + color
    color = clean

  for k, v in color_conversions.items():
    if color == k:
      return v
    elif color == v:
      return k
    else:
      continue
  
  return 'Sorry we don\'t have that color on file. Please make sure you entered the color with its correct syntax.'

get_hex1 = rgb_hex('rgb(89, 5, 198)')
print(get_hex1) # #5905c6

get_rgb1 = rgb_hex('#b7ffb8')
print(get_rgb1) # rgb(183, 255, 184)

get_hex2 = rgb_hex((255, 191, 0)) 
print(get_hex2) # #ffbf00

get_rgb2 = rgb_hex('ff5e6e')
print(get_rgb2) # rgb(255, 94, 110)

get_hex2 = rgb_hex((5, 91, 0)) 
print(get_hex2) # ERROR

get_rgb2 = rgb_hex('2f2f3f')
print(get_rgb2) # ERROR


