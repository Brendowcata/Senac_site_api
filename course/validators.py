def duration_time_isValid(duration_time):
    """Check if the duration time is valid / Verifica se o tempo de duração é válido"""
    return duration_time > 0

def name_isValid(name):
    """Check if the name is valid / Verifica se o nome é válido"""
    if any(char.isdigit() for char in name):
        return False
    else:
        return True

def occupation_area_isValid(occupation_area):
    """Check if the occupation area is valid / Verifica se a area de ocupação é válido"""
    if any(char.isdigit() for char in occupation_area):
        return False
    else:
        return True