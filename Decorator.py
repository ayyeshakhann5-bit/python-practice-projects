def add_sprinkles(func):
  def wrapper(*args, **kwargs):
    print("Adding sprinkles to your ice cream! 🎊")
    func(*args, **kwargs)
  return wrapper  

def add_fudge(func):
  def wrapper(*args, **kwargs):
    print("Adding fudge to your ice cream! 🍫")
    func(*args, **kwargs)
  return wrapper

@add_sprinkles     
@add_fudge                                        #decorator
def get_ice_cream(flavor):                        #base function
  print(f"Here is your {flavor} ice cream! 🍦")
  
get_ice_cream("chocolate")  

