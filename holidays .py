import holidays
Asia = holidays.Australia() 
print(Asia.country)

print(Asia.get('26-01-10000'))
print(Asia.get('15-08-2018'))