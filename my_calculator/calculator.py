"""Калькулятор модулі — CI/CD демонстрациясы үшін."""


def add(a, b):
    """Екі санды қосып қайтарады."""
    return a + b


def subtract(a, b):
    """Бірінші саннан екіншісін азайтады."""
    return a - b


def multiply(a, b):
    """Екі санды көбейтеді."""
    return a * b


def divide(a, b):
    """Бөлу — нөлге бөлуден қорғайды."""
    if b == 0:
        raise ValueError("Нөлге бөлуге болмайды!")
    return a / b

