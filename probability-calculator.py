import copy
import random

class Hat:

    def __init__(self, **kwargs):
        # Initialize the contents of the hat as an empty list
        self.contents = []
        # Loop through the keyword arguments and add the specified number of balls of each color to the contents list
        for key, value in kwargs.items():
            for _ in range(value):
                self.contents.append(key)

    def draw(self, number):
        # If the number of balls to draw is greater than the total number of balls in the hat, return all the balls
        if number >= len(self.contents):
            return self.contents
        balls = []
        # Randomly draw balls from the hat 'number' times and add them to the 'balls' list
        for _ in range(number):
            choice = random.randrange(len(self.contents))
            balls.append(self.contents.pop(choice))
        return balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # Convert the expected_balls dictionary values to a list for comparison
    expected_no_of_balls = list(expected_balls.values())
    successes = 0

    # Run the experiment 'num_experiments' times
    for _ in range(num_experiments):
        # Create a deep copy of the hat to avoid modifying the original hat during the experiment
        new_hat = copy.deepcopy(hat)
        # Draw 'num_balls_drawn' balls from the hat
        balls = new_hat.draw(num_balls_drawn)

        # Count the occurrences of each color ball in the drawn balls
        no_of_balls = [balls.count(key) for key in expected_balls]

        # Check if the number of each color ball drawn matches the expected number of balls
        if no_of_balls >= expected_no_of_balls:
            successes += 1

    # Return the probability of success (successes divided by the total number of experiments)
    return successes / num_experiments
