import phonenumbers
phone_number = phonenumbers.parse("+919305959635")
valid = phonenumbers.is_valid_number(phone_number)
possible = phonenumbers.is_possible_number(phone_number)
print(valid)
print(possible)