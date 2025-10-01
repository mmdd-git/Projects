def suma(a, b):
    """Suma dos números."""
    return a + b

def multiplica(a, b):
    """Multiplica dos números."""
    return a * b

def divide(a, b):
    """Divide dos números."""
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b