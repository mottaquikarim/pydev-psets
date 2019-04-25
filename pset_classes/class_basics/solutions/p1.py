"""
RGB to HEX
"""

# Remember our function "rgb_hex" from the functions pset? That function took a color in rgb format and returned it in hex format as well as vice versa. Wouldn't it be so much easier to do that with a class called Color?

# Define a class called "Color" to store each color's rgb and hex values. Define a method called "convert_codes()" to retrieve one value given the other. Create at least one instance of Color and try the convert_codes() method.


class Color():
	def __init__(self, rgb, hex_code):
		self.rgb = rgb
		self.hex_code = hex_code

	def convert_codes(self, color_code):
		if color_code == self.rgb:
			return self.hex_code
		elif color_code == self.hex_code:
			return self.rgb
		else:
			return 'Error: Invalid color'



black = Color('rgb(0, 0, 0)', '#000000')
white = Color('rgb(255, 255, 255)', '#ffffff')


# Convert rgb to hex
print(black.convert_codes('rgb(0, 0, 0)')) # '#000000'
print(white.convert_codes('rgb(255, 255, 255)')) # '#ffffff'


# Convert hex to rgb
print(black.convert_codes('#000000')) # 'rgb(0, 0, 0)'
print(white.convert_codes('#ffffff')) # 'rgb(255, 255, 255)'



