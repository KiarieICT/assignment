from gettext import npgettext
import turtle
import math
import numpy as np

# Function to calculate the angle between two points
def calculate_angle(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    angle = math.degrees(math.atan2(dy, dx))
    return angle

# Function to update the polygon's orientation based on the camera position
def update_orientation(poly, camera_x, camera_y):
    # Calculate the angle between the polygon and the camera
    angle = calculate_angle(poly.xcor(), poly.ycor(), camera_x, camera_y)
    
    # Set the polygon's heading to face the camera
    poly.setheading(angle)

# Function to move the camera and update the polygon's orientation
    
def move_camera(x, y):
    turtle.tracer(0)  # Turn off animation for smoother movement
    camera.goto(x, y)
    update_orientation(poly, x, y)
    turtle.update()

# Set up the Turtle screen
turtle.speed(0)
turtle.bgcolor("white")

# Create a polygon to act as the billboardimport numpy as np

class VirtualFramebuffer:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.framebuffer = np.zeros((height, width), dtype=int)

    def write_pixel(self, x, y, color):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.framebuffer[y, x] = color

    def read_pixel(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.framebuffer[y, x]
        return None

    def display(self):
        for row in self.framebuffer:
            row_str = ''.join(['#' if pixel else ' ' for pixel in row])
            print(row_str)

# Example usage
if __name__ == "__main__":
    width = 20
    height = 10

    framebuffer = VirtualFramebuffer(width, height)

    # Draw a line from (2, 2) to (18, 8) with color 1
    x0, y0 = 2, 2
    x1, y1 = 18, 8
    color = 1

    dx = x1 - x0
    dy = y1 - y0
    steps = max(abs(dx), abs(dy))

    x_increment = dx / steps
    y_increment = dy / steps

    for i in range(steps + 1):
        x = round(x0 + i * x_increment)
        y = round(y0 + i * y_increment)
        framebuffer.write_pixel(x, y, color)

    # Display the virtual framebuffer
    framebuffer.display()

    poly = turtle.Turtle()
    poly.shape("triangle")
    poly.color("blue")
    poly.penup()
    poly.goto(0, 100)

# Create a Turtle for the camera
camera = turtle.Turtle()
camera.shape("circle")
camera.color("red")
camera.penup()
camera.goto(0, 0)

# Bind the movement of the camera to the mouse
turtle.getcanvas().bind("<Motion>", lambda event: move_camera(event.x - turtle.window_width() // 2, turtle.window_height() // 2 - event.y))

# Initialize the orientation of the polygon
update_orientation(poly, camera.xcor(), camera.ycor())

# Start the Turtle graphics loop
turtle.mainloop()
