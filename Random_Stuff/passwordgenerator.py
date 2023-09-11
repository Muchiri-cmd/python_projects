import random

lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols="[]{}()*/,._-"
numbers="0123456789"

all=lower+upper+numbers+symbols
length=12
password="".join(random.sample(all,length))

print(password)