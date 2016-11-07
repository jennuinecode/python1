import re
# # \s signifies the space character
# # the "*" means ANY , so if we find ANY space characters.
# # So all together, if there are any instances of space characters, we are going to run .split method, which will create a list by splitting on the space.
# print(re.split(r'\s', 'here are some words'))
#
# #by putting () around the \s* we are saying group and include what we're breaking this up by.
# #that means that the spaces will be included in the list
# print(re.split(r('\s*'), 'here are some words'))
#
# #by removing the backslash, we are saying wherever there is an s, we are going to great the split.
# print(re.split(r('s*'), 'here are some words'))

# we are checking for characters a through f and splitting there. i am looking for a range of chracters to break up
# print(re.split(r'[a-f][a-f]','zdaffkjhklsjfGJDIWAKafJSF', re.I|re.M))
#re.I says to ignore case fluctuations
#re.M is saying if the input string is multi line, we can evaluate continously instead of stpping at each line.

print(re.findall(r'\d{1,5}\s\w+\s\w+\.', 'asdlf2949 parkwood st.kj;asdf'))
#"\d" means we are looking for digits. same thing as going [0-9]
# if we did capital d, it would look for the reverse. So everything EXCEPT digits 0-9
#findall() finds all instances of \d or whatever else we pass
# {1,5} means that we are going to be looking for a range of 1-5 digits
#\w means that the street number could be followed by the street name that has either letters or numbers. aka 5th street or continental ave. it means letters OR digits
# the + is because we want at least one (we dont know how many characters we will have)
#\. means anything at all with exception of new line of character
