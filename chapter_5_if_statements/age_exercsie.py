age = 19
if age < 2:
    stage = 'a baby.'
elif 2 <= age < 4:
    stage = 'a toddler.'

elif 4 <= age < 13:
    stage = 'a kid.'

elif 13 <= age < 20:
    stage = 'a teenager.'

elif 20 <= age < 65:
    stage = 'an adult.'

elif 65 <= age:
    stage = 'an elder.'

print(f"This person is {stage}")
