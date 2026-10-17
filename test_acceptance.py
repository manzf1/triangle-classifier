
from triangle import classify_triangle


def test_customer_order():
    # Check a triangle with all equal sides
    assert classify_triangle(4, 4, 4) == "Equilateral"

    # Check a triangle with two equal sides
    assert classify_triangle(5, 5, 7) == "Isosceles"

    # Check a triangle with different sides
    assert classify_triangle(4, 5, 6) == "Scalene"

    # Check measurements that cannot make a triangle
    assert classify_triangle(2, 3, 5) == "Invalid"

    # Check a right triangle that needs stronger corners
    assert classify_triangle(3, 4, 5) == "Right Scalene"
