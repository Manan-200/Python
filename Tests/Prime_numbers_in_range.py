start = int(input("Enter lower limit: "))
end = int(input("Enter upper limit: "))
counter = 0

for num in range(start, end+1):
	if num != 1 and num != 0:
		is_prime = True
		for div in range(2, num):
			if num % div == 0:
				is_prime = False
				
		if is_prime:
			counter += 1
			print(f"{num}; counter: {counter}")