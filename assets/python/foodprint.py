
import random

def main():
	stillEntering = True
	user_dict = {}
	while stillEntering:
		key = input("What did you eat today? ")
		if not key.lower() in [x.lower() for x in food_dict.keys()]:
			valid = False
			while not valid:
				key = input("Food not valid. What did you eat today? ")
				if key.lower() in [x.lower() for x in food_dict.keys()]:
					valid = True
		value = float(input("How much of it did you eat (in grams)? ")) * 0.001
		user_dict[key] = value

		if input("Would you like to keep adding entries? (Y/N) ") == "Y":
			stillEntering = True
		else:
			stillEntering = False
	ratio_dict = filter_foods(user_dict.keys())
	ghg_sum = sum_food(ratio_dict, user_dict)
	if input("Is this your first day using Foodprint? (Y/N) ") == "Y":
		print("For your first day of tracking your dietary carbon footprint, your carbon footpring was approximately " + ghg_sum + "! Try to lower this number tomorrow by making less emission-heavy dietary choices!")
	else:
		last_day = float(input("Today your dietary carbon footprint was approximately " + ghg_sum + " kilograms of CO2eq emissions. What was your dietary carbon footprint (in kilograms) when you previously used Foodprint? "))
		print(evaluate_progress(pctg_check(ghg_sum, last_day)))
	return True


def filter_foods(input_list):
	# takes in list of food that user inputs		
	# returns the list of food that the user inputted and makes a dictionary with those foods and their respective "kg-of-GHG to kg-of-food-product" ratio
	new_dict = {}					
	for i in input_list:
		new_dict[i] = food_dict[i]
	return new_dict

'''def make_quant_dict(food_quant_dict):
	# takes in a dictionary (keys: food that user ate; values)
	new_dict = {}
	for i in input_list:
		new_dict[]
	return new_dict '''

def sum_food(eaten_dict, quant_dict): 
	# takes in: 1) a dictionary (keys: foods that user ate; values: their respective ratios) and 
			# 	2) another dictionary (keys: foods that user ate; values: their respective quantities consumed)
	# returns the total GHG emissions (estimate) of the foods consumed by user this day
	sum = 0
	for i in eaten_dict.keys(): 
		sum += food_dict.get(i, 0) * quant_dict.get(i, 0) 
	return sum


def pctg_check(this_day, last_day):
	# takes in total emissions from this day and last day
	# returns the percent change between the two days
	return (this_day - last_day) / last_day * 100

def evaluate_progress(pctg):
	# takes in: percentage change between this day and last day
	# returns: a feedback message
	s = ''
	pct = round(abs(pctg), 3)
	if pctg > 15.0:
		s = "Oh no! The carbon footprint of your diet today was " + str(pct) + "% higher than it was last today!" 
	elif pctg > 7.0:
		s = "Uh oh, the carbon footprint of your diet today was " + str(pct) + "% higher than it was last today."
	elif pctg > 0.0: 
		s = "Today you lowered your dietary carbon footprint by " + str(pct) + "% compared to last today!"
	elif pctg > -7.0:
		s = "Good job! Today the carbon footprint was " + str(pct) + "% lower than it was last today. Keep it up!"
	elif pctg > -15.0:
		s = "Your diet's carbon footprint from today was " + str(pct) + "% lower than it was last time! Amazing work!"
	else:
		s = "Wow! Today's dietary carbon footprint was a whole " + str(pct) + "% lower than it was last time! The planet is proud of you, and so are we."
	return s


test_list = {	'Cheese', 'Pig Meat', 'Groundnuts'}

food_dict = {	'Beef (beef herd)': 60, 
				'Lamb and Mutton': 24,
				'Cheese': 21,
				'Beefy (dairy herd)': 21,
				'Chocolate': 19,
				'Coffee': 17,
				'Prawns (farmed)': 12,
				'Palm Oil':	8,
				'Pig Meat': 7,
				'Poultry Meat': 6,
				'Olive Oil': 6,
				'Fish (farmed)': 5,
				'Eggs': 4.5,
				'Rice': 4,
				'Fish (wild catch)': 3,
				'Milk': 3,
				'Cane Sugar': 3,
				'Groundnuts': 2.5,
				'Wheat and Rye': 1.4,
				'Tomatoes': 1.4,
				'Maze (corn)': 1,
				'Cassava': 1,
				'Soymilk': 0.9,
				'Peas': 0.9,
				'Bananas': 0.7,
				'Root Vegetables': 0.4,
				'Apples': 0.4,
				'Citrus Fruits': 0.3,
				'Nuts': 0.3			}

main()



