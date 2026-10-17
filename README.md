
# Triangle Classifier

## Copilot Review Log

| Test | Copilot-suggested? | Kept / Edited / Rejected | Why |
|---|---|---|---|
| test_invalid_triangle | Yes | Kept | Copilot correctly tested negative sides, zero sides, and the degenerate case. |
| test_equilateral_triangle | Yes | Kept | Copilot correctly checked that three equal sides return Equilateral. |
| test_isosceles_triangle | Yes | Kept | Copilot correctly tested equal sides in three different positions. |
| test_scalene_triangle | Yes | Edited | Copilot expected Scalene for (3, 4, 5), but this is also a right triangle. I corrected the expected result to Right Scalene. |
| test_right_triangle | Yes | Edited | Copilot suggested only integer-sided right triangles. I added a test using 5, 5, and 5 * math.sqrt(2) to check non-integer sides and floating-point tolerance. |

## Acceptance Criteria

1. When a customer enters three side lengths that make a triangle, the program should show the correct triangle type: Equilateral, Isosceles, or Scalene.

2. If a customer enters a zero, a negative number, or sides that cannot make a triangle, the program should display "Invalid" instead of giving a triangle type.

3. If the measurements make a right triangle, the program should include "Right" in the answer. This helps the customer know that the glass needs stronger corners.


## Acceptance Test Explanation

For this test, I focused on what the customer needs when ordering a stained-glass piece. I checked different triangle measurements to make sure the program gives the right shape. I also tested measurements that cannot make a triangle because the customer should know if something is wrong before placing an order. Lastly, I checked a right triangle since those pieces need stronger corners. These tests help make sure the program gives customers the correct information.


## How to Run the Tests

To run the tests, open the terminal in VS Code and type:


python -m pytest -v

## The equivalence classes and boundaries

I tested different types of triangles to make sure the program works correctly. My tests include triangles with equal sides, two equal sides, and different sides.

I also checked invalid measurements, including zero, negative numbers, and sides that add up to exactly the third side. These cases are important because they cannot form a real triangle.



## AI Use Disclosure

I used GitHub Copilot to help suggest unit tests for the triangle classifier. I reviewed the suggestions and made changes when needed. For example, Copilot suggested that a triangle with sides (3, 4, 5) was Scalene, but I corrected it to Right Scalene.