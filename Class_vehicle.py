class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
modelx= Vehicle(240, 18)
print("Model X has a maximum speed of", modelx.max_speed)
print("Model X has a mileage of", modelx.mileage)