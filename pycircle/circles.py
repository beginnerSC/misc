from math import pi

def circle_area(r):
    """Compute area of a circle.
    
    The area of a circle with radius $r$ is $\pi r^2$. 
    
    Parameters
    ----------
    r : float or int, must be nonnegative
        Radius of the circle.
        
    Returns
    -------
    area : float
        Area of the circle
    """
    
    if type(r) not in [int, float]:
        raise TypeError("The radius must be a non-negative real number.")
    
    if r < 0:
        raise ValueError("The radius cannot be negative")
    
    return pi*(r**2)