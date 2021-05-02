divList = []

[divList.append(int(input())) for x in range(2)]

print(divList[0] // divList[1], divList[0] % divList[1], divmod(divList[0], divList[1]), sep='\n')
