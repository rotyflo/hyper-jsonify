import sys

file = open(sys.argv[1], 'r')
file_contents = eval(file.read())
colorscheme = {}

colorscheme['name'] = file.name.replace('.txt', '').replace('.', '_')
color_names = [
    'black',
    'red',
    'green',
    'yellow',
    'blue',
    'magenta',
    'cyan',
    'white',
    'lightBlack',
    'lightRed',
    'lightGreen',
    'lightYellow',
    'lightBlue',
    'lightMagenta',
    'lightCyan',
    'lightWhite'
]
color_values = file_contents['color']
color_dictionary = {}

for i in range(16):
    color_dictionary[color_names[i]] = color_values[i]

output = 'let ' + colorscheme['name'] + ' = {'
output += "'colors': " + str(color_dictionary) + ', '
output += "'foreground': '" + file_contents['foreground'] + "', "
output += "'background': '" + file_contents['background'] + "'"

output += '};'

print()
print(output)
print()