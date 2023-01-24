regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))

# import re
# match = re.search(r'word:\w\w\w', 'an example word:cat!!')
# # print(match)
# if match:
#   print('found', match.group()) ## 'found word:cat'
# else:
#   print('did not find')

# str = 'purple alice-b@google.com monkey dishwasher'
# match = re.search(r'[\w.-]+@[\w.-]+', str)
# if match:
#   print(match.group())  ## 'alice-b@google.com'