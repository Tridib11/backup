import random
# random_integer=random.randint(1,10)
# print(random_integer)

# random_float=random.random() #for float we use random
# print(random_float*5)


# #a float has a random function and the range stays in 0 to 1
# import random
# randomFloat = random.random() * 100

# randomPercent = round(randomFloat, 2)

# print(str(randomPercent) + '%')

#Reference: http://www.easypythondocs.com/random.html


# colors = ['red', 'green', 'yellow', 'blue', 'purple']

# randomColor = random.choice(colors)

# print(randomColor)

#Reference: http://www.easypythondocs.com/random.html


cards=[1,2,3,4,5,6,7,8,9,'J','Q','K','A']
random.shuffle(cards)
print(cards)