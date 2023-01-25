input = input('enter the statment: ')
acr = ''
raw_acr = input.split()

for i in raw_acr:
    acr = acr + str(i[0]).upper()
print(acr)