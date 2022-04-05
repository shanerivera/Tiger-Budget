import tkinter as tk

#GUI (Jack)
window = tk.Tk()

window.configure(bg='#88a2bf')

window.title("TigerBudget")

window.geometry("600x400")

# Label
d_d_label = tk.Label(window, text="Dining Dollars", bg='#88a2bf')
d_d_label.pack()

#Entry field 
default = tk.StringVar(window, value='1')
entry_field1 = tk.Entry(window, textvariable=default)
entry_field1.pack()

#Label 2
weeks_left_label = tk.Label(text="Weeks Left in Semester", bg='#88a2bf')
weeks_left_label.pack()

#Entry field 2
default2 = tk.StringVar(window, value='1')
entry_field2 = tk.Entry(window, textvariable=default2)
entry_field2.pack()

#Label 3
mpw_label = tk.Label(text="Meals Per Week Using DD", bg='#88a2bf')
mpw_label.pack()

#Entry field 3
default3 = tk.StringVar(window, value='1')
entry_field3 = tk.Entry(window, textvariable=default3)
entry_field3.pack()

#Label 4
choice_label = tk.Label(text="Restaurant", bg='#88a2bf')
choice_label.pack()

#Dropdown
clicked = tk.StringVar()
clicked.set("Chick Fil A")

dropdown = tk.OptionMenu(window, clicked, "Chick Fil A", 
"Einstein Bros. Bagels", "Panda Express", "Amsterdam Cafe", "Amsterdam Taco Truck", "Samabazon",
"Toro Sushi", "Salad Works", "NYC GYRO Food Truck", "Hibachi Food Truck", "Philly Connection", "Noodle Fun Food Truck", "Good Karma Food Truck", "Smoothie King", "Cafe 25", "Tiger Bread Company", "Tiger Zone", "Chicken Salad Chick", "The Edge", "Panera")

dropdown.pack()

#ListBox

list_box = tk.Listbox(window, width=50)
list_box.configure(background = '#ffbb54')
list_box.pack()


#Dictionaries

Chicken_Salad_Chick = {
    "Scoop": 8.99,
    "Sandwich": 8.99,
    "Chicken Salad BLT": 9.49,
    "Pimiento Cheese BLT": 9.49,
    "Broccoli Salad": 3.09,
    "Mac and Cheese": 3.09,
    "Soup of the Day": 3.59,
    "Loaded Potato Soup": 3.59
}

Chick_fil_a = {
    "Chicken Sandwich Meal": 7.55,
    "Chicken Sandwich Deluxe Meal": 8.25,
    "Grilled Chicken Sandwich Meal": 9.15,
    "Spicy Chicken Sandwich Meal": 7.79,
    "Spicy Chicken Sandwich Deluxe Meal": 8.49,
    "Chargrilled Chicken Club Sandwich Meal": 10.65,
    "8-Count Nuggets Meal": 7.65,
    "12-Count Nuggets Meal": 9.45,
    "8-Count Grilled Nuggets Meal": 8.45,
    "12-Count Grilled Nuggets Meal": 10.75
}

Einstein_bros = {
    "Spicy Chicken Sandwich": 6.49,
    "Applewood Bacon & Cheddar Egg Sandwich": 5.59,
    "Turkey-Sauasage & Cheddar Egg Sandwich": 4.99,
    "Egg & Cheddar Sandwich": 4.69,
    "Big Breakfast Burrito": 5.99,
    "Bagel": 1.29,
    "Bagel with Shmear": 2.79,
    "Half Dozen Bagels": 6.99,
    "Baker's Dozen Bagels": 10.99
}

Panda_Express = {"Bowl": 6.40, "Plate": 7.90, "Bigger Plate": 9.40}

Amsterdam_Cafe_Food_Truck = {
    "Amsterdam turkey Wrap": 11.99,
    "Griddle Burger": 10.99,
    "Buffalo Chicken Sandwich": 10.99,
    "Chicken Finger plate": 11.99
}

Amsterdam_Taco_Truck = {
    "Beef/Chicken/Carnitas Tacos": 10.99,
    "Steak Tacos": 11.99,
    "Vegetarian Tacos": 9.99,
    "Beef/Chicken/Carnitas Burrito Bowls": 11.99,
    "Steak Burrito Bowls": 12.99,
    "Vegetarian Burrito Bowls": 10.99,
    "Beef/Chicken/Carnitas Nachos": 11.99,
    "Steak Nachos": 12.99
}

Samabazon = {
    "Berry Bowl": 7.99,
    "Coconut Mango Bowl": 7.99,
    "Chocolate, Peanut Butter & Banana": 7.99,
    "Amazon Protein Bowl": 7.99,
    "Create Your Own Bowl": 7.99
}

Toro_Sushi = {
    "Create your Own Poke Bowl": 1.99,
    "Create your Own Sushi": 8.49,
    "Create your Own Crunchy Special Roll": 9.49,
    "Spicy Mango Roll": 9.49,
    "Tiger Tail": 7.99,
    "Special Tiger Tail": 8.99
}

NYC_GYRO_Truck = {
    "Gyro Wrap Combo": 12.99,
    "Lamb Loaded Fries": 12.9,
    "Salad": 12.99,
    "Cheeseburger Combo": 11.99,
    "Chicken Wings": 11.99,
    "Chicken Tenders": 11.99
}

Noodle_Fun_Food_Truck = {
    "Mapo Tofu": 10.95,
    "Kungpo Chicken": 10.95,
    "Pork Belly with Vegetables": 10.95,
    "Spare Rib with Potato": 10.95,
    "General Tso’s Chicken": 10.95,
    "Shredded Pork with Garlic Sauce": 10.95,
    "Egg with Tomato": 10.95,
    "Shredded Pork with Spiced Tofu": 10.95,
    "Roasted Duck Over Rice": 10.95,
    "Roasted Pork Over Rice": 10.95,
    "Roasted Duck Noodle Soup": 10.95,
    "Roasted Pork Noodle Soup": 10.95,
    "Stewed Beef Noodle Soup": 10.95,
    "Steamed Chives Dumpling": 9.95
}

Salad_Works = {
    "Create your Own Salad/Wrap": 9.29,
    "Buffalo Bleu Salad/Wrap": 9.29,
    "Mandarin Chicken Salad/Wrap": 9.29,
    "Sophie's Salad/Wrap": 9.29,
    "Thai Chicken Salad/Wrap": 9.29,
    "Turkey Club Salad/Wrap": 9.29,
    "Tivoli Salad/Wrap": 9.29,
    "Farmhouse Salad/Wrap": 9.29,
    "Bently Salad/Wrap": 9.29,
    "Chicken Caesar Salad/Wrap": 8.69,
    "Fire Roasted Cabo Salad/Wrap": 9.29,
    "Mediterranean Salad/Wrap": 9.29,
    "Cobb Salad/Wrap": 9.29
}

Tiger_Zone_Dining = {"Cheese Pizza": 9.99, "Pepperoni Pizza": 9.99}

Tiger_Bread_Company = {
    "Create your Own Sandwich": 7.59,
    "08 oz Soup Combo": 3.09,
    "Soup": 3.19
}

Cafe_25 = {
    "Create Your Own Sandwich": 7.59,
    "08oz Soup Combo": 3.09,
    "Soup": 3.19
}

Smoothie_King_Food = {
    "Chocolate Peanut Power Plus": 8.00,
    "Strawberry Peanut Power Plus": 8.00,
    "Angel Food": 8.00,
    "Caribbean Way": 8.00,
    "Lemon Twist Strawberry": 8.00,
    "Pineapple Surf": 8.00,
    "Strawberry kiwi Breeze": 8.00
}

Philly_Connection_Food_Truck = {
    "The Original": 9.99,
    "The Plain Jane": 9.99,
    "The Chicken Original": 9.99,
    "The Chicken Plain Jane": 9.99,
    "The Veggie": 9.99,
    "The Turkey": 9.99,
    "The Italian Sub": 9.99
}

Good_Karma_Food_Truck = {
    "Create Your Own Rice Bowl": 10.99,
    "Chicken Tikka Masala": 10.99,
    "Paneer Curry": 10.99,
    "Aloo Mattar": 10.99
}

Hibachi_Food_Truck = {
    "Grilled Chicken Bowl": 10.99,
    "Pork Bowl": 10.99,
    "Shrimp Bowl": 12.99,
    "Steak Bowl": 11.99,
    "Surf & Turf Bowl": 13.99,
    "Shirmp Tempura Bowl": 12.99,
    "Tofu Bowl": 10.99,
    "Dumplings": 6.99
}

Edge_Dining_Hall = {"Entry": 12}

Panera_Bread = {
    "New Sausage & Pepperoni Flatbread Pizza": 10.99,
    "Pepper Flatbread  Pizza": 10.99,
    "Chiptole Chicken & Bacon Flatbread Pizza": 10.99,
    "Sanwich and Soup/Mac": 9.98,
    "Soup/Mac and Salad": 10.18,
    "Soup/Mac and Soup/Mac": 9.98,
    "New Grilled Mac & Cheese Sandwich": 8.29,
    "Chiptole Chicken Avocado Melt": 8.29,
    "Smokehouse Bbq Chicken Sandwich": 9.79,
    "Fuji Apple Salad with Chicken": 8.29,
    "Caesar Salad with Chicken": 8.29,
    "Asian Sesame Salad with Chicken": 8.29,
    "Mac & Cheese": 6.59,
    "Broccoli Cheddar Mac & Cheese": 6.59,
    "Vegetarian Autumn Squash soup": 6.19
}

#User Input Code -> $ Budget Per Meal
def button_clicked():
  list_box.delete(0, tk.END)

  try:
    float(entry_field1.get())
  except:
    list_box.insert(1, 'Enter a float value for entry field 1')
    return

  try:
    int(entry_field2.get())
    int(entry_field3.get())
  except:
    list_box.insert(1, 'Enter an integer value for entry fields 2 & 3')
    return

  if (entry_field1.get() == '0'):
    return
  if (entry_field2.get() == '0'):
    return
  if (entry_field3.get() == '0'):
    return

  dining_dollars_left = float(entry_field1.get())
  weeks_left_in_semester = int(entry_field2.get())
  meals_per_week = int(entry_field3.get())

  #Dictionary Match (Keanna/Mason)
  #match the user input to the dictionary

  choice = clicked.get()

  if choice == 'Chick Fil A':
      place = Chick_fil_a
  if choice == 'Einstein Bros. Bagels':
      place = Einstein_bros
  if choice == 'Panda Express':
      place = Panda_Express
  if choice == 'Amsterdam Cafe':
      place = Amsterdam_Cafe_Food_Truck
  if choice == 'Amsterdam Taco Truck':
      place = Amsterdam_Taco_Truck
  if choice == 'Samabazon':
      place = Samabazon
  if choice == 'Toro Sushi':
      place = Toro_Sushi
  if choice == 'Salad Works':
      place = Salad_Works
  if choice == 'NYC GYRO Food Truck':
      place = NYC_GYRO_Truck
  if choice == 'Hibachi Food Truck':
      place = Hibachi_Food_Truck
  if choice == 'Philly Connection':
      place = Philly_Connection_Food_Truck
  if choice == 'Noodle Fun Food Truck':
      place = Noodle_Fun_Food_Truck
  if choice == 'Good Karma Food Truck':
      place = Good_Karma_Food_Truck
  if choice == 'Smoothie King':
      place = Smoothie_King_Food
  if choice == 'Cafe 25':
      place = Cafe_25
  if choice == 'Tiger Bread Company':
      place = Tiger_Bread_Company
  if choice == 'Tiger Zone':
      place = Tiger_Zone_Dining
  if choice == 'Chicken Salad Chick':
      place = Chicken_Salad_Chick
  if choice == 'The Edge':
      place = Edge_Dining_Hall
  if choice == 'Panera':
      place = Panera_Bread

  budget = round(
      (dining_dollars_left) / (weeks_left_in_semester * meals_per_week), 2)
  list_box.insert(1, choice)
  list_box.insert(2, "Budget per meal: ${:.2f}".format(budget))

  #Budget Comparison (Shane/Josh)
  #traverse through each dictionary and compare the budget to the food price
  #display all items that fall below the budget
  index = 3
  for item, price in place.items():
      if price < budget:
          list_box.insert(index, "{} - ${:.2f}".format(item, price))
          index += 1
      else:
          pass

  index += 1
  list_box.insert(index, '*If no items are shown, then budget is too low*')
  index += 1
  list_box.insert(index, '*NOTE: All Prices Are Subject to Change Due to Taxes/Service Fees*')

#button
button = tk.Button(window, text='Generate Options', command = button_clicked)
button.pack()

window.mainloop()