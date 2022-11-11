MENU = {
	"espresso": {
		"ingredients": {
			"water": 50,
			"coffee": 18,
		},
		"cost": 1.5,
	},
	"latte": {
		"ingredients": {
			"water": 200,
			"milk": 150,
			"coffee": 24,
		},
		"cost": 2.5,
	},
	"cappuccino": {
		"ingredients": {
			"water": 250,
			"milk": 100,
			"coffee": 24,
		},
		"cost": 3.0,
	}
}

resources = {
	"water": 300,
	"milk": 200,
	"coffee": 100,
	"money": 0.0,
}


def prompt():
	off = False
	while not off:
		choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
		if choice == "espresso" or choice == "latte" or choice == "cappuccino":
			if resource_check(choice):
				if payment(choice) > 0:
					update_resources(choice)
					print(f"Here is your {choice}. Enjoy!\n")
		elif choice == "report":
			report()
		elif choice == "off":
			print("Turning off...")
			off = True
		else:
			print("Please enter a valid input.")


def resource_check(choice):
	if choice == "espresso":
		if MENU["espresso"]["ingredients"]["water"] > resources["water"]:
			print("Not enough water.")
			return False
		elif MENU["espresso"]["ingredients"]["coffee"] > resources["coffee"]:
			print("Not enough coffee.")
			return False
		else:
			return True
	elif choice == "latte":
		if MENU["latte"]["ingredients"]["water"] > resources["water"]:
			print("Not enough water.")
			return False
		elif MENU["latte"]["ingredients"]["milk"] > resources["milk"]:
			print("Not enough milk.")
			return False
		elif MENU["latte"]["ingredients"]["coffee"] > resources["coffee"]:
			print("Not enough coffee.")
			return False
		else:
			return True
	elif choice == "cappuccino":
		if MENU["cappuccino"]["ingredients"]["water"] > resources["water"]:
			print("Not enough water.")
			return False
		elif MENU["cappuccino"]["ingredients"]["milk"] > resources["milk"]:
			print("Not enough milk.")
			return False
		elif MENU["cappuccino"]["ingredients"]["coffee"] > resources["coffee"]:
			print("Not enough coffee.")
			return False
		else:
			return True


def payment(choice):
	if choice == "espresso":
		cost = MENU["espresso"]["cost"]
	elif choice == "latte":
		cost = MENU["latte"]["cost"]
	elif choice == "cappuccino":
		cost = MENU["cappuccino"]["cost"]

	print(f"Cost: ${'{0:.2f}'.format(cost)}")
	print("Please insert coins.")
	quarters = int(input("How many quarters? "))
	dimes = int(input("How many dimes? "))
	nickels = int(input("How many nickels? "))
	pennies = int(input("How many pennies? "))
	total = ((quarters * .25) + (dimes * .1) + (nickels * .05) + (pennies * .01))

	if total > cost:
		change = total - cost
		print(f"Here is ${'{0:.2f}'.format(change)} in change.")
		return cost
	elif total < cost:
		print("Insufficient funds. Money refunded.")
		return 0
	else:
		return cost


def update_resources(choice):
	if choice == "espresso":
		resources["water"] -= MENU["espresso"]["ingredients"]["water"]
		resources["milk"] -= MENU["espresso"]["ingredients"]["milk"]
		resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
		resources["money"] += MENU["espresso"]["cost"]
	elif choice == "latte":
		resources["water"] -= MENU["latte"]["ingredients"]["water"]
		resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
		resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
		resources["money"] += MENU["latte"]["cost"]
	elif choice == "cappuccino":
		resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
		resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
		resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
		resources["money"] += MENU["cappuccino"]["cost"]


def report():
	water = resources["water"]
	milk = resources["milk"]
	coffee = resources["coffee"]
	money = resources["money"]
	print(f"Water: {water}mL")
	print(f"Milk: {milk}mL")
	print(f"Coffee: {coffee}g")
	print(f"Money: ${'{0:.2f}'.format(money)}\n")

prompt()
