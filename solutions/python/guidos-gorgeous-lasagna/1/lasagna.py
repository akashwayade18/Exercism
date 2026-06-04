"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

#TODO (student): Remove 'pass' and complete the 'bake_time_remaining()' function below
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    
    return EXPECTED_BAKE_TIME - elapsed_bake_time
    

   
def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes.

    Parameters:
        number_of_layers (int): Number of layers ou want to add to lasagna.

    Returns:
        int: preparato time (in minutes) derived from 'PREPARATION_TIME'.

    Function that takes the number of layers the lasagna has as
    an argument and returns how many minutes preparation needs to be done
    based on the `PREPARATION_TIME`.
    """
    
    return PREPARATION_TIME*number_of_layers
    

#TODO (student): define the 'elapsed_time_in_minutes()' function below.

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.
    
    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
        elapsed_bake_time (int): Time the lasagna has been baking in the oven.
    
    Returns:
        int: The total time elapsed (in minutes) preparing and baking.

    This function takes two integers representing the number of lasagna 
    layers and the time already spent baking the lasagna. It calculates 
    the total elapsed minutes spent cooking (preparing + baking).
    """
    
    return elapsed_bake_time + preparation_time_in_minutes(number_of_layers)
    
   
