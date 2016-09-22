first_string = "not empty"

# Print the first letter of the following string
print ("M")
school = "McHenry County College"




# print the length of the school string
print (len(school))



# Use a while loop to print each character (including spaces) in the school variable

i=0

while i < len(school):
    print school[i]
    i += 1

# Slice school into three variables, print the variables

print (school[0:7])
print (school[8:14])
print (school[15:22])

# use a while statement to search for the letter "e" in the contents of the school variable
# print the index of every location with the letter "e"
# remember, you should not use the same variable twice in the same program
# so if you used the variable index, use something else

index = 0
while index < len(school):
    e = school[index]
    print school
    index = index + 9


# Write the code to count the number of times the letter y appears in the school variable
# print the total

word = 'McHenry County College'
count = 0
for letter in word:
    if letter == 'y':
        count = count + 1
print count





# create a variable named college and store the upper case version of the variable school in it

value = "College"
x = value.upper()
print x


# check to see if Count is in the school variable

if "Count" in school:
    print "yes"

