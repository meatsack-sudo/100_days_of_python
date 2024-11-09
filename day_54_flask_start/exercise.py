import time
#current_time = time.time()
#print(current_time) # seconds since Jan 1st, 1970 

# Write your code below 👇

def speed_calc_decorator(function):
  
  def time_the_function():
    current_time = time.time()
    function()
    end_time = time.time()
    time_to_run = end_time - current_time
    print(f"{function.__name__} ran for: {time_to_run} seconds.")

  return time_the_function

@speed_calc_decorator
def fast_function():
  for i in range(1000000):
    i * i
        
@speed_calc_decorator
def slow_function():
  for i in range(10000000):
    i * i
    
fast_function()
slow_function()