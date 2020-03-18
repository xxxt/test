a = 'http://imgoss.cnu.cc/2002/25/40a62fc542a93900b3aa6a580c5aa667.jpg?width=1400&height=788&x-oss-process=style/flow280'
b = 'http://imgoss.cnu.cc/2002/25/40a62fc542a93900b3aa6a580c5aa667.jpg?width=1400&amp;height=788&amp;x-oss-process=style/flow280'

import re

pattern = re.compile(r'.*(?=\?width)')
r = re.match(pattern, a)

print(r.group())
print(r)