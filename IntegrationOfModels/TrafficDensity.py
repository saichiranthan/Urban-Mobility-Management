import random

def get_traffic_density(from_ward, to_ward):
    """
    Simulates traffic density between two wards.
    YOLO model is Used for real time number of vehicle-detection at every junction
    formula for traffic density  = (number of vehicles in a given road per minute / width of the road)
    """
    length_of_road=random.randint(5, 20)#in meters

    # Define a range for traffic density values (0 - 10)
    Total_vehicles_perminute = random.randint(0,50)
    
    # Generate random traffic density values 
    traffic_density=(Total_vehicles_perminute/length_of_road)
    
    return traffic_density

    
    
    