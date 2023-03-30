# prime number calculator: find all primes up to n
max = int(input("Find primes up to what number? : "))
#esta función crea una lista en la que se van agregandos numeros
primeList = []
#for loop for checking each number
for x in range(2, max + 1):
    #se define la variable "IsPrime" como verdadera
	isPrime = True
	index = 0
	root = int(x ** 0.5) + 1
	while index < len(primeList) and primeList[index] <= root:
		if x % primeList[index] == 0:
			isPrime = False
			break
		index += 1
	if isPrime:
		primeList.append(x)
print(primeList)
#-------------------------------------------------------------
# prime number calculator: find the first n primes
count = int(input("Find how many primes?: "))
primeList = []
#variable inicial
x = 2
while len(primeList) < count:
	isPrime = True
	index = 0
	root = int(x ** 0.5) + 1
	while index < len(primeList) and primeList[index] <= root:
		if x % primeList[index] == 0:
			isPrime = False
			break
		index += 1
	if isPrime:
		primeList.append(x)
	x += 1
print(primeList)