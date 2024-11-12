import math

def area_of_sector(angle, radius): # angle (Celcius)
    area = (angle/360) * math.pi * (radius**2)
    return area
    
def area_of_triangle(angle, radius):
    area = (1/2) * (radius**2) * math.sin(math.radians(angle))
    return area

def area_of_shaded_region(a1, r1, a2, r2):
    area = (area_of_sector(a1, r1) - area_of_triangle(a1, r1)) + (area_of_sector(a2, r2) - area_of_triangle(a2, r2))
    return area
    
print(area_of_shaded_region(30, 4, 45, 4))
