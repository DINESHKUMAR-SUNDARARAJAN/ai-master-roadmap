def get_current_year():
    from datetime import datetime
    return {"year": datetime.now().year}

def multiply_numbers(x: float, y: float):
    return {"result": x * y}