#Funtions with Outputs

def format_name(f_name, l_name):
  """ Take a first and last name and foramt ist to return the title case version of the name."""
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f'{formated_f_name} {formated_l_name}'

formatted_string = format_name('gun', 'kim')
print(formatted_string)
print(format_name('gun', 'kim'))

output = len('gun')

format