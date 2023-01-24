import re

str = 'apurva.sinha.25@gmail-25-of-India.com'
match = re.search(r'([\w\d.-]+)@([\w.-]+)', str)
match = re.search(r'([\w\d.-]+)@([\w.-]+)', str)
if match:
    print(match.group())  ## 'b@google'
    print(match.group(1))
    print(match.group(2))

# ---------------------------------------------------------------------------------------------------------

str = 'purple alic--.e@goo89_--.gle.com, blah monkey bob@abc67_.com blah dishwasher'

## Here re.findall() returns a list of all the found email strings
emails = re.findall(r'([\w.-]+)@([\w.-]+)_([\w.-]+)', str) ## ['alice@google.com', 'bob@abc.com']

for email in emails:
# do something with each found email string
    print(email,email[0],email[1],email[2],'\n')

# ---------------------------------------------------------------------------------------------------------

print(re.search(r'([<\w>]+)', '<i>soon<i> <i>soon enough<i>').group())

# ---------------------------------------------------------------------------------------------------------

#Squaring numbers
def square(match):
    number = int(match.group(0))
    return str(number**2)
print(re.sub(r"\d+", square, "1 2 3 4 5 6 7 8 9"))

# ---------------------------------------------------------------------------------------------------------
html = """
<head>
<title>HTML</title>
</head>
<object type="application/x-flash" 
  data="your-file.swf" 
  width="0" height="0">
  <!-- <param name="movie"  value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>
"""
print(re.sub("(<!--.*-->)", "", html))#remove comment
# ---------------------------------------------------------------------------------------------------------