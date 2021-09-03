EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


# TODO: define the 'bake_time_remaining()' function
def bake_time_remaining(elapsed_bake_time):
    '''
    :param elapsed_bake_time: int baking time already elapsed
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    '''
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(num_layers):
    '''
    :param num_layers: int number of layers in lasagna
    :return: int total prep time based on 'PREPARATION_TIME'

    Function that takes the number of layers in a lasagna as argument
    and returns how many minutes will be needed to assembly the entire
    lasagna
    '''
    return num_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    '''
    :param number_of_layers: int number of layers in lasagna
    :param elapsed_bake_time: int number of minutes passed baking already
    :return: int total time currently elapsed in prep+baking time

    Function that takes the number of layers in the lasagna and how long
    lasagna has been baking for and calculates the total amount of time
    that has passed so far
    '''
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
