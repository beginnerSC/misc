from math import pi

def circle_area(radius):
    """Compute area of a circle.
    
    The area of a circle with radius :math:`r` is :math:`\pi r^2`. 
    
    Parameters
    ----------
    radius : float or int, must be nonnegative
        Radius of the circle.
        
    Returns
    -------
    area : float
        Area of the circle.
    """
    
    if type(radius) not in [int, float]:
        raise TypeError("The radius must be int or float.")
    
    if radius < 0:
        raise ValueError("The radius cannot be negative")
    
    return pi*(radius**2)