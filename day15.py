'''
Frosting: capacity 4, durability -2, flavor 0, texture 0, calories 5
Candy: capacity 0, durability 5, flavor -1, texture 0, calories 8
Butterscotch: capacity -1, durability 0, flavor 5, texture 0, calories 6
Sugar: capacity 0, durability 0, flavor -2, texture 2, calories 1
'''
ingredients, scores = [], []
ingredients.append((4,-2,0,0,5))
ingredients.append((0,5,-1,0,8))
ingredients.append((-1,0,5,0,6))
ingredients.append((0,0,-2,2,1))
capacity, durability, flavor, texture, calories = 0,0,0,0,0
tTbsp = 100
for i1 in range(tTbsp):
	for i2 in range(tTbsp-i1):
		for i3 in range(tTbsp-i1-i2):
			i4 = tTbsp - i1 - i2 - i3
			capacity =		ingredients[0][0]*i1 + ingredients[1][0]*i2 + ingredients[2][0]*i3 + ingredients[3][0]*i4
			durability =	ingredients[0][1]*i1 + ingredients[1][1]*i2 + ingredients[2][1]*i3 + ingredients[3][1]*i4
			flavor =		ingredients[0][2]*i1 + ingredients[1][2]*i2 + ingredients[2][2]*i3 + ingredients[3][2]*i4
			texture = 		ingredients[0][3]*i1 + ingredients[1][3]*i2 + ingredients[2][3]*i3 + ingredients[3][3]*i4
			score = (capacity*durability*flavor*texture)
			print (score)
			scores.append(max(0,score))

print(max(scores))