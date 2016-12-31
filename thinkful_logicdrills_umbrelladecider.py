def take_umbrella(weather, rain_chance):
    
    if (weather ==  "rainy") or (weather == "cloudy" and rain_chance > 0.20):
        return True
    elif (weather == "sunny" and rain_chance > 0.50):
        return True
    else:
        return False