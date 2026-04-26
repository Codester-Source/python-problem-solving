"""Moudle for calculating grains on a chessboard."""
def square(number):
    """Function to calculate number of grains in one square"""
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    grains=1
    for _ in range(1, number):
        grains=grains*2
    return grains
    
        
    


def total():
    """Function to calculate total grains in all square"""
    total_grains=0
    grains=1
    for _ in range(1, 65):
        total_grains+=grains
        grains=grains*2
    return total_grains
