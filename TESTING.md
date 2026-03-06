# Testing Strategy

## Overview

This project uses a layered testing strategy consisting of unit tests and integration tests. The goal is to verify both the correctness of the core calculator logic and the interaction between the input layer and the calculation logic.

## What Was Tested

The following areas were tested:
- Addition, subtraction, multiplication, and division
- Edge cases such as division by zero, negative numbers, decimal numbers, and large numbers
- Integration between the application flow and the calculator logic
- Clear/reset behavior after a calculation

## What Was Not Tested

The following areas were not tested:
- Performance
- Security
- Usability with real users
- Cross-platform interface behavior

These were not included because the assignment focuses mainly on functional correctness, testing strategy, and version control.

## Relation to Lecture Concepts

### Testing Pyramid

This project reflects the testing pyramid by including more unit tests than integration tests. There are 8 unit tests and 2 integration tests. This follows the pyramid because unit tests are fast and verify small pieces of logic, while integration tests are broader and fewer in number.

### Black-box vs White-box Testing

The unit tests are closer to white-box testing because they directly test individual methods in the calculator logic. The integration tests are closer to black-box testing because they simulate user actions and verify the visible result without focusing on internal implementation details.

### Functional vs Non-Functional Testing

This project focuses on functional testing. It checks whether the calculator performs the required operations correctly and whether the clear function resets the state properly. Non-functional aspects such as speed and usability were intentionally left out because they are outside the assignment scope.

### Regression Testing

This test suite can also act as a regression testing suite. If the calculator is extended with new features in the future, the existing tests can confirm that the old functionality still works and that previously fixed issues have not returned.

## Test Results Summary

| Test Name                            | Type        | Status |
|-------------------------------------|-------------|--------|
| test_addition                       | Unit        | Pass   |
| test_subtraction                    | Unit        | Pass   |
| test_multiplication                 | Unit        | Pass   |
| test_division                       | Unit        | Pass   |
| test_division_by_zero               | Unit        | Pass   |
| test_add_negative_numbers           | Unit        | Pass   |
| test_decimal_multiplication         | Unit        | Pass   |
| test_large_number_addition          | Unit        | Pass   |
| test_full_user_interaction_addition | Integration | Pass   |
| test_clear_resets_display           | Integration | Pass   |