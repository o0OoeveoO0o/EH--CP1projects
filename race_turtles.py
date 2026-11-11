# EH Teenage mutant nija turtles race project p1 m4x YIPEEEE

import turtle
import random

def setup_screen():
    """Set up the race screen with title and finish line"""
    screen = turtle.Screen()
    screen.title("Turtle Race")
    screen.bgcolor("white")
    screen.setup(width=800, height=600)
    
    # Draw the finish line so the ninja turtles have a place to go
    finish = turtle.Turtle()
    finish.hideturtle()
    finish.speed(0)
    finish.penup()
    finish.goto(300, 250)
    finish.pendown()
    finish.pensize(3)
    finish.goto(300, -250)
    
    return screen

def create_turtles():
    """Create our 5 ninja turtles of different colors, lined up at the start."""
    colors = ["red", "blue", "green", "yellow", "purple"]
    y_positions = [150, 75, 0, -75, -150]
    turtles = []
    
    for i in range(5):
        t = turtle.Turtle()
        t.shape("turtle")
        t.color(colors[i])
        t.penup()
        t.goto(-300, y_positions[i])
        t.pendown()
        turtles.append(t)
    
    return turtles

def race(turtles):
    """Moves our ninja turtles forward a random number of steps each round until the strongest one wins."""
    winner = None
    while winner is None:
        for t in turtles:
            # Random steps between 1 and 10
            steps = random.randint(1, 10)
            t.forward(steps)
            
            # Check if turtle crossed the finish line (x >= 300)
            if t.xcor() >= 300:
                winner = t
                break
    return winner

def announce_winner(winner):
    """Announce the winner so the ninja turtle can laugh at it's opponents and to make it better we'll print it in both on screen and in the terminal"""
    color = winner.color()[0]
    print(f"The Strongest one is the {color} turtle! NOW BULLY YOUR OPPONENTS")
    
    # Write the winner message on the screen
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.goto(0, 220)
    pen.color(color)
    pen.write(f"Winner: {color.upper()} ninja turtle! GG's", align="center",
              font=("Arial", 20, "bold"))

def main():
    """Main function to run the turtle race game."""
    screen = setup_screen()
    turtles = create_turtles()
    
    # Small delay so the user can see the starting lineup
    screen.delay(20)
    
    winner = race(turtles)
    announce_winner(winner)
    
    # Keep the window open until the user clicks
    screen.exitonclick()

if __name__ == "__main__":
    main()
