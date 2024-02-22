# import re

# email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

# user_email=input(' Enter Your Email : ')

# if re.search(email_condition,user_email):
#     print(" right email")
# else:
#     print( "wrong email")


# -------------------- just for practice --------------------

import re
pattern= r"[a-z]+osts"

text = """
From web development to data science,
 PyCharm Professional equips you with the tools to work with databases,
 frontend, remote hosts mosts tosts , Jupyter notebooks, and much more.
Try it now and get more work done.
"""


match = re.finditer(pattern,text)

for i in match:
    print(i)