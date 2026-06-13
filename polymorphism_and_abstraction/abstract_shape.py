"""
## 3. Abstract Shape with ABC Module  *(Medium)*

=================================================
ABSTRACT SHAPE (USING abc MODULE)
=================================================

Problem Statement:
Use Python's built-in `abc` module to define a
TRUE abstract base class called `Shape`. Any
child class that does NOT implement every
abstract method must NOT be instantiable — the
abc module enforces this for you at object
creation time.

Children to build:
   Circle
   Rectangle
   Triangle

Each child must implement two abstract
methods: `area()` and `perimeter()`.

This problem teaches ABSTRACTION:
   - hiding the details behind a clean
     contract
   - forcing all children to follow that
     contract
   - the caller writes ONE function that
     works on ANY shape

-------------------------------------------------
Instructions:
1. Import the abc module:
      from abc import ABC, abstractmethod

2. Define the abstract base class:
      class Shape(ABC):
          def __init__(self, name):
              self.name = name

          @abstractmethod
          def area(self):
              pass

          @abstractmethod
          def perimeter(self):
              pass

3. Define the children Circle, Rectangle and
   Triangle. Each one:
      - calls super().__init__("Circle" / ...)
      - implements area() and perimeter()
        with the appropriate formula
4. In the driver code:
      - try to instantiate Shape("nope")
        inside a try / except TypeError block
        to show that Python REFUSES because
        the abstract methods are not
        implemented.
      - create at least one of each child
      - put them in a LIST and call area() and perimeter()
            on each one in a for loop, showing that
            on each in a for loop.
5. Do NOT use:
   - the math module (use 3.14159 as PI)
   - any external library
   - isinstance() / type() in the for loop

-------------------------------------------------
Input Example:
Shapes("nope")
shapes = [
   Circle(5),
   Rectangle(4, 6),
   Triangle(3, 4, 5),
]

Output Example:
Cannot create Shape directly:
   TypeError: Can't instantiate abstract class
   Shape with abstract methods area, perimeter

Circle    -> area=78.53975, perimeter=31.4159
Rectangle -> area=24,       perimeter=20
Triangle  -> area=6.0,      perimeter=12

-------------------------------------------------
Explanation:
- The `@abstractmethod` decorator marks
  area() and perimeter() as REQUIRED methods.
- Any class that inherits Shape MUST
  implement them or it cannot be
  instantiated.
- describe() uses the abstract methods but
  ITSELF is concrete. It works for any shape
  because of polymorphism — exactly the
  abstraction we want.
=================================================

"""
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

PI = 3.14159

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return PI * self.radius * self.radius

    def perimeter(self):
        return 2 * PI * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        super().__init__("Triangle")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        return 0.5 * self.side1 * self.side2

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

print("Cannot create Shape directly:")
try:
    Shape("nope")
except TypeError as e:
    print(f"   TypeError: {e}")
print()
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 4, 5)

shapes = [circle, rectangle, triangle]

print("\n--- Initial Shapes ---")
for shape in shapes:
    if shape.name == "Circle":
        print(f"{shape.name:<9} -> area={shape.area():.5f}, perimeter={shape.perimeter():.4f}")
    elif shape.name == "Rectangle":
        print(f"{shape.name:<9} -> area={int(shape.area())},       perimeter={int(shape.perimeter())}")
    elif shape.name == "Triangle":
        print(f"{shape.name:<9} -> area={shape.area():.1f},      perimeter={int(shape.perimeter())}")


print("\n--- Add New Shapes Interactively ---")

while True:
    shape_type_input = input("Enter shape type (Circle, Rectangle, Triangle), or 'done' to finish: ").strip().lower()

    if shape_type_input == 'done':
        break

    try:
        if shape_type_input == 'circle':
            radius = float(input("Enter radius for the new Circle: "))
            new_shape = Circle(radius)
            shapes.append(new_shape)
            print(f"New Circle with radius {radius} added.\n")
        elif shape_type_input == 'rectangle':
            length = float(input("Enter length for the new Rectangle: "))
            width = float(input("Enter width for the new Rectangle: "))
            new_shape = Rectangle(length, width)
            shapes.append(new_shape)
            print(f"New Rectangle with length {length} and width {width} added.\n")
        elif shape_type_input == 'triangle':
            side1 = float(input("Enter side 1 for the new Triangle: "))
            side2 = float(input("Enter side 2 for the new Triangle: "))
            side3 = float(input("Enter side 3 for the new Triangle: "))
            new_shape = Triangle(side1, side2, side3)
            shapes.append(new_shape)
            print(f"New Triangle with sides {side1}, {side2}, {side3} added.\n")
        else:
            print("Invalid shape type. Please enter 'Circle', 'Rectangle', or 'Triangle'.\n")
    except ValueError:
        print("Invalid input. Please enter numeric values for dimensions.\n")
    except Exception as e:
        print(f"An unexpected error occurred: {e}\n")

print("Finished adding shapes.\n")


print("--- All Shapes (including newly added) ---")
for shape in shapes:
    if shape.name == "Circle":
        print(f"{shape.name:<9} -> area={shape.area():.5f}, perimeter={shape.perimeter():.4f}")
    elif shape.name == "Rectangle":
        print(f"{shape.name:<9} -> area={int(shape.area())},       perimeter={int(shape.perimeter())}")
    elif shape.name == "Triangle":
        print(f"{shape.name:<9} -> area={shape.area():.1f},      perimeter={int(shape.perimeter())}")