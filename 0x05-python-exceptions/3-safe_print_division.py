#!/usr/bin/python3
def safe_print_division(a, b):
    c = 0
    try:
        c = c + (a / b)
    except (ZeroDivisionError, ValueError, TypeError):
        c = None
    finally:
        return c
