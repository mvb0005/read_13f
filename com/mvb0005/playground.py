import re
s = "\'test\'"
print(re.search("\'(.*?)\'", s)[0])
