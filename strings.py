# datetime example
from datetime import datetime
now = datetime.now()
print('%02d/%02d/%04d %02d:%02d:%02d' % (now.month, now.day, now.year, now.hour, now.minute, now.second))



# given a string, reverse will return the letters in reverse order
def reverse(text):
    word = ""
    l = len(text) - 1
    while l >= 0:
        word = word + text[l]
        l -= 1
    return word

print(reverse("Hello World"))



# anti_vowel removes all the vowels from a string
def anti_vowel(text):
    word = ""
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    l = 0
    while l <= len(text) - 1:
        if not text[l] in vowels:
          word = word + text[l]

        l += 1
    return word

print(anti_vowel("Hello World"))



# scrabble score adds the point values for each letter in string
def scrabble_score(word):
    score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
             "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
             "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
             "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
             "x": 8, "z": 10}
    totalscore = 0

    l = 0
    while l <= len(word) - 1:
      totalscore += score[word[l].lower()]
      l += 1
    return totalscore

print(scrabble_score("HelloWorld"))


# censor replaces word found in text with ****
def censor(text, word):
    words = text.split()
    result = ''
    stars = '*' * len(word)
    count = 0
    for i in words:
        if i == word:
            words[count] = stars
        count += 1
    result =' '.join(words)

    return result

print(censor("this hack is wack hack", "hack"))



# count finds and reports how many time item appears on sequence
def count(sequence, item):
    count = 0
    for i in sequence:
        if i == item:
            count += 1
    return count

print(count([1, 2, 1, 1], 1))



# purify removes the odd numbers from a list
def purify(numbers):
    result = []
    for item in numbers:
        if item % 2 == 0:
            result.append(item)
    return result

print(purify([1, 2, 3, 4]))



# product multiplies all the items in the list
def product(numbers):
  result = 1
  for item in numbers:
    result *= item
  return result

print(product([4, 5, 5]))



# duplicates in the list are removed
def remove_duplicates(numbers):
  result = []
  for item in numbers:
    if item in result:
      print("already exists")
    else:
      result.append(item)
  return result

print(remove_duplicates([1, 1, 2, 2]))


# the next block illustrates various list operations
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
  for grade in grades_input:
    print(grade)

def grades_sum(scores):
  total = 0
  for score in scores:
    total += score
  return total

def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / float(len(grades_input))
  return average

def grades_variance(scores):
  average = grades_average(scores)
  variance = 0
  for score in scores:
    variance += (average - score) ** 2
  result = variance / len(scores)
  return result

variance = grades_variance(grades)

def grades_std_deviation(variance):
  return variance ** 0.5

print_grades(grades)
print(grades_sum(grades))
print(grades_average(grades))
print(variance)
print(grades_std_deviation(variance))


# python calls them dictionaries instead of hashes
my_dict = {
  "Description": "Widget",
  "Quantity": 10,
  "Price": 1.25
}

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

for key in my_dict:
  print(key, my_dict[key])


# popluating lists - list comprehension
doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]
even_squares = [x ** 2 for x in range(2, 12) if (x ** 2) % 2 == 0]
cubes_by_four = [x ** 3 for x in range(1, 11) if ((x ** 3) % 4) == 0]
threes_and_fives = [x for x in range(1, 16) if x % 3 == 0 or x % 5 == 0]

print(doubles_by_3)
print(even_squares)
print(cubes_by_four)

l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# prints the second thru 9th items stepping 2
# [start:end:stride]
print(l[2:9:2])

my_list = range(1, 11)
# prints every other entry
print(my_list[::2])

#reverses the list
print(my_list[::-1])




# simple file operations
my_list = [i ** 2 for i in range(1, 11)]

my_file = open("output.txt", "w")
for item in my_list:
  my_file.write(str(item) + "\n")
my_file.close()


my_file = open("output.txt","r")
print(my_file.read())
my_file.close()


# we can automatically close the file with this syntax
with open("text.txt", "w") as my_file:
  my_file.write("Success!")



# class definition example
class Fruit(object):
  """A class that makes various tasty fruits."""
  healthy = True

  def __init__(self, name, color, flavor, poisonous):
    self.name = name
    self.color = color
    self.flavor = flavor
    self.poisonous = poisonous

  def description(self):
    print("I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor))

  def is_edible(self):
    if not self.poisonous:
      print("Yep! I'm edible.")
    else:
      print("Don't eat me! I am super poisonous.")

lemon = Fruit("lemon", "yellow", "sour", False)

lemon.description()
lemon.is_edible()

print(lemon.healthy)


class ShoppingCart(object):
  """Creates shopping cart objects
  for users of our fine website."""

  def __init__(self, customer_name):
    self.customer_name = customer_name
    self.items_in_cart = {}
  def add_item(self, product, price):
    """Add product to the cart."""
    if not product in self.items_in_cart:
      self.items_in_cart[product] = price
      print(product + " added.")
    else:
      print(product + " is already in the cart.")

  def remove_item(self, product):
    """Remove product from the cart."""
    if product in self.items_in_cart:
      del self.items_in_cart[product]
      print(product + " removed.")
    else:
      print(product + " is not in the cart.")


my_cart = ShoppingCart("brian")
my_cart.add_item("dog food", 4.25)


# A class can inheirit methods from other objects
# notice Customer is built from an object but ReturningCustomer is built from Customer
class Customer(object):
  """Produces objects that represent customers."""
  def __init__(self, customer_id):
    self.customer_id = customer_id

  def display_cart(self):
    print("I'm a string that stands in for the contents of your shopping cart!")

class ReturningCustomer(Customer):
  """For customers of the repeat variety."""
  def display_order_history(self):
    print("I'm a string that stands in for your order history!")

monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()


# We can use the super function to access parent methods
class Employee(object):
  """Models real-life employees!"""
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00

class PartTimeEmployee(Employee):
  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 12.00

  def full_time_wage(self, hours):
    return super(PartTimeEmployee, self).calculate_wage(hours)

milton = PartTimeEmployee('Milton')
print(milton.full_time_wage(10))
