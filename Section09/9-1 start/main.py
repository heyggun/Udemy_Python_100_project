programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again."}

print(programming_dictionary)


print(programming_dictionary['Bug'])


programming_dictionary['Loop'] = 'The action of doing something over and over again.'


print(programming_dictionary)

#Create an empth dictionary
empty_dictionary = {}
print(empty_dictionary)

#Edit an item in a dictionary

programming_dictionary['Bug'] = 'a moth in your computer'
print(programming_dictionary)

#Loop through a dictionary
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])