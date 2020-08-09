
import random

def filter_food(eaten_list):
	new_dict = {}
	for i in eaten_list:
		new_dict[i] = food_dict[i]
	return new_dict

def combine_food(eaten_dict, quant_dict):
	sum = 0
	for i in eaten_dict.keys():
		sum += food_dict.get(i, 0) * quant_dict.get(i, 0)
	return sum


def pctg_check(this_week, last_week):
	return (this_week - last_week) / last_week * 100

def evaluate_progress(pctg):
	s = ''
	if pctg > 50.0:
		s = "Oh no! The carbon footprint of your diet this week was " + str(abs(pctg)) + "% higher than it was last week!" 
	elif pctg > 20.0:
		s = "Uh oh, the carbon footprint of your diet this week was " + str(abs(pctg)) + "% higher than it was last week."
	elif pctg > 0.0: 
		s = "This week, you lowered your dietary carbon footprint by " + str(abs(pctg)) + "% compared to last week!"
	elif pctg > -20.0:
		s = "Good job! This week the carbon footprint was " + str(abs(pctg)) + "% lower than it was last week. Keep it up!"
	elif pctg > -50.0:
		s = "Your diet's carbon footprint was " + str(abs(pctg)) + "% lower than it was last week! Amazing work!"
	else:
		s = "Wow! Your dietary carbon footprint was a whole " + str(abs(pctg)) + "% lower than it was last week! The planet is proud of you, and so are we."
	return s

def not_fun_facts():
	str = ""
	x = random.randint(1, 11)
	if x == 1:
		str = "According to sciencemag.org, our current chain of food supply is responsible for 26\% of man-made greenhouse gas emissions, or 13.7 billion metric tons per year."
		# https://science.sciencemag.org/content/360/6392/987

	elif x == 2:
		str = "By switching to diets that exclude animal products, we could save 3.1 billion hectares of land that would otherwise go toward the raising of livestock, a 76\% decrease in food-related land use."

		# https://science.sciencemag.org/content/360/6392/987
	elif x == 3:
		str = "Livestock from farms are fed with harvested foods, processed, transported, refrigerated in retail, and even packaged. All of these steps, including the processes of clearing land to have these farms in the first place, have the potential to release emissions."

		# https://www.visualcapitalist.com/visualising-the-greenhouse-gas-impact-of-each-food/

	elif x == 4:
		str = "One of the most surefire ways to reduce your dietary carbon footprint is to shift away from animal-based foods and toward plant-based ones! The greenhouse gases emitted by animal-based products are multitudes higher than plant-based ones when it comes to areas like changes in biomass, animal byproducts, and crop production for livestock feed."

		# https://ourworldindata.org/food-choice-vs-eating-local

	elif x == 5:
		str = "According to Our World in Data, one rather obscure way to reduce your dietary carbon footprint is to avoid purchasing air-freighted food products. These products can be responsible for 50 times more CO2eq emissions than their boat-transported counterparts."

		# https://ourworldindata.org/food-choice-vs-eating-local
	elif x == 6:
		str = ""
	elif x == 7:
		str = ""
	elif x == 8:
		str = ""
	elif x == 9:
		str = ""
	elif x == 10:
		str = ""
	elif x == 11:
		str = ""
	return str


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



