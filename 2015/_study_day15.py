def mixtures(n, total):
    start = total if n == 1 else 0

    for i in range(start, total+1):
        left = total - i
        if n-1:
            for y in mixtures(n-1, left):
                yield [i] + y
        else:
            yield [i]
#Calories should always be the last element for each ingredient.
ingredients = [
    [1, 0, -5, 1],
    [0, 3, 0, 3],
]

def score(recipe, max_calories=0):
    proportions = [map(lambda x:x*mul, props) for props, mul in zip(ingredients, recipe)]
    dough = reduce(lambda a, b: map(sum, zip(a, b)), proportions)
    calories = dough.pop()
    result = reduce(lambda a, b: a*b, map(lambda x: max(x, 0), dough))
    return 0 if max_calories and calories > max_calories else result
#Then just map score over all possible recipes:
 recipes = mixtures(len(ingredients), 100)
 print max(map(score, recipes))
#Part2:
 print max(map(lambda r: score(r, 500), recipes))