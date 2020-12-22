"""I have a box with 10 red balls and 10 green balls. I draw 2 balls from the 
box without replacing them. What is the probability that I get 2 red balls?"""

red_balls = 10
green_balls = 10

total = red_balls + green_balls

#taking one ball

first_red_ball_prob = red_balls/total

# taking second ball

second_red_ball_prob = (red_balls-1)/(total-1)

product_rule = first_red_ball_prob*second_red_ball_prob

print(product_rule) 

"""If I draw 3 balls without replacement, what is the probability that they 
are all red?"""


#taking third ball

three_balls = product_rule * (red_balls-2)/(total-2)

print(three_balls)