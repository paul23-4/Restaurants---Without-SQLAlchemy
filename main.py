import os
from restaurant import Restaurant
from review import Review
from customer import Customer

# Clear the terminal screen
os.system('cls' if os.name == 'nt' else 'clear')

# Create sample instances
restaurant1 = Restaurant("Restaurant 1", 10)
restaurant2 = Restaurant("Restaurant 2", 20)
customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Doe")

# Add reviews
review1 = Review(restaurant1, customer1, 5)
review2 = Review(restaurant2, customer2, 2)

# Test object relationship methods
print("Customer 1's reviews:", customer1.reviews())
print("Customer 2's reviews:", customer2.reviews())
print("Restaurant 1's reviews:", restaurant1.reviews())
print("Restaurant 2's reviews:", restaurant2.reviews())

# Test aggregate and relationship methods
print("Customer 1's full name:", customer1.full_name())
print("Customer 2's full name:", customer2.full_name())

# Check if reviews are good or poor
print("Review 1 is good:", review1.is_good_review())
print("Review 1 is poor:", review1.is_poor_review())
print("Review 2 is good:", review2.is_good_review())
print("Review 2 is poor:", review2.is_poor_review())
