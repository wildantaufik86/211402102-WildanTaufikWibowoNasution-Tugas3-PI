# Write a class that calculates and stores the height and weight of a person in metric. The file should be named lab.py.  BMI is calculated using this formula:
# Weight/Height^2 - weight is in kilograms and height is in meters.
# The class should have two properties named:
# Weight
# Height
# The class should have two methods:
# BMI_Value – This takes no arguments and returns a decimal value of the BMI
# Equals – This should override the equals method from the object class to compare the weight and height of two BMI objects.  To override the equal method you should implement this method: __eq__(self, other) and return a boolean


class BMI:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def BMI_Value(self):
        return self.weight / (self.height ** 2)

    def __eq__(self, other):
        return (self.weight, self.height) == (other.weight, other.height)

def main():
    person1 = BMI(70, 1.75)  # Weight in kg, Height in meters
    person2 = BMI(65, 1.70)  # Weight in kg, Height in meters

    print("Person 1 BMI:", person1.BMI_Value())
    print("Person 2 BMI:", person2.BMI_Value())

    if person1 == person2:
        print("Both persons have the same weight and height.")
    else:
        print("Persons have different weight or height.")

if __name__ == "__main__":
    main()
