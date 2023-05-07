
class Car:
    def __init__(self, model_year, purchase_price, current_value = 0):
        # FIXME: Define the constructor
        self.model_year = model_year
        self.purchase_price = purchase_price
        selt.current_value = current_value

    def calc_current_value(self, current_year):
        depreciation_rate = 0.15
        # Car depreciation formula
        car_age = current_year - self.model_year
        self.current_value = round(self.purchase_price * (1 - depreciation_rate) ** car_age)
    
    def print_info(self):
        # FIXME: define print_info() method to output model_year,
        # purchase_price, and current_value
        print("Model year", self.model_year, "Purchase Price", self.purcase_price, "Current Vlaue", self.current_value)
    
year = int(input('Input the year of purchase: ')) 
price = int(input('Input the purchase price: '))
current_year = int(input('Input current year: '))
    
my_car = Car(year, price)
my_car.calc_current_value(current_year)
my_car.print_info()






