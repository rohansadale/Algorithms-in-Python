def change_coins(coins, amount):
	mincoins = amount
	if amount in coins:
		return 1
	else:
		for i in [coin for coin in coins if coin < amount]:
			numcoins = 1 + change_coins(coins, amount-i)
			if numcoins < mincoins:
				mincoins = numcoins
		return mincoins

def change_coins_mem(coins, amount, memory):
	mincoins = amount
	if amount in coins:
		return 1
	elif memory[amount] > 0:
		return memory[amount]
	else:
		for i in [coin for coin in coins if coin < amount]:
			numcoins = 1 + change_coins_mem(coins, amount-i, memory)
			if numcoins < mincoins:
				mincoins = numcoins
				memory[amount] = mincoins
		return mincoins

def change_coins_dp(coins, amount):
	mincoins = [0]*(amount+1)
	for cents in range(amount+1):
		coins_change = cents
		for i in [coin for coin in coins if coin <= cents]:
			if mincoins[cents-i] + 1 < coins_change:
				coins_change = mincoins[cents-i] + 1
		mincoins[cents] = coins_change
	return mincoins[amount]

if __name__ == '__main__':
	#print change_coins([1,2,5], 63)
	print change_coins_mem([1,5, 10, 25], 63, [0]*64)
	print change_coins_dp([1,5, 10, 25], 63)