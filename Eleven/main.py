# # item1 = 'Phone'
# # item1_price = 100
# # item1_quantity = 5
# # item1_price_total = item1_price * item1_quantity



# class Item:
#     def __init__(self, name: str, price: float, quantity=0):
        
#         # Run validations to the received arguments
#         assert price >= 0, f"Price {price} is not greater than zero!"
#         assert quantity >= 0, f"Quantity {quantity} is not greater than zero!"
        
        
#         # Assign to self object
#         self.name = name
#         self.price = price
#         self.quantity = quantity
        
        
        
        
#     def calculate_total_price(self, x, y):
#         return x * y
    
    
# item1 = Item('Phone', 100, -5)

# total = item1.calculate_total_price(item1.price, item1.quantity)
# print(total)

# item2 = Item('Laptop', 1000, 3)



class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house 



def main():
    student = get_student()
    print(f"{student.name} from {student.house}")
    
    
    
def get_student():
    student = Student()
    student.name = input('Name: ')
    student.house = input('House: ')
    return student


main()
















