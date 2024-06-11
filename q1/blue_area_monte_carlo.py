import random
import math
import numpy as np

# constants definitions:

# the circles
CENTERS = [(0, 0), (np.cos(np.pi / 3), np.sin(np.pi / 3)), (-np.cos(np.pi / 3), np.sin(np.pi / 3))]
CIRCLES_RADIUS = 1

# Number of random points to generate
POINTS_NUM = 100000000

# Min and max values of the points
MIN_VAL = -2
MAX_VAL = 2

def main():
    estimate_area(POINTS_NUM)

def estimate_area(num_of_points: int):
    '''
    estimate the area according to number of points.
    it generates random points and for each one it checks wheather or not the point 
    is inside the area of the circles. Then it calculates the probability of a point from 
    the given square to be in the area, and then according to the square's area it 
    calculates the area of the given figure.
    Args:
        num_of_points (int): number of random points to generate
    '''
    
    in_points_num = get_num_of_in_points(num_of_points)
    in_point_probability = in_points_num / num_of_points

    # callculate the estimated figure's area according to the area of the square and
    # the probability of a point to be in this area
    square_area = (MAX_VAL - MIN_VAL) ** 2
    estimated_area = in_point_probability * square_area

    print(f'The estimated area for n = {num_of_points} is: {estimated_area}')

def get_num_of_in_points(num_of_points: int) -> int:
    '''
    generate points and return the number of the points that are inside the area
    Args:
        num_of_points (int): number of points to generate
    Returns:
        number of points that generated inside the area
    '''
    in_points_counter = 0 # will count the in point
    for _ in range(num_of_points):
        point = (random.uniform(MIN_VAL, MAX_VAL), random.uniform(MIN_VAL, MAX_VAL))
        if is_point_in_area(point, CENTERS, CIRCLES_RADIUS): # check if the point is inside the area
            in_points_counter += 1
    return in_points_counter

def is_point_in_area(point: tuple[float, float], centers: list[tuple[float]], radius: int) -> bool:
    '''
    determine if a given point is inside the area of a given circle's union

    Args:
        point (tuple of floats): the given point
        centers (list  of tuples of floats): the centers of the given circles
        radius (int): the given radius

    Returns:
        bool: yes if the point inside the area, no otherwise
    '''
    return any([is_point_in_circle(point, center, radius) for center in centers])

def is_point_in_circle(point: tuple[float, float], circle_center: tuple[float, float], circle_radius: int) -> bool:
    '''
    determine if a given point is inside the area of a given circle

    Args:
        point (tuple of floats): the given point
        circle_center (tuple of floats): the given circle's center
        circle_radius (int): the given circle's radius

    Returns:
        bool: yes if the point inside the area, no otherwise
    '''
    x1, y1 = point
    x2, y2 = circle_center
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance <= circle_radius

if __name__ == "__main__":
    main()