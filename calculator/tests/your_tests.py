#!/usr/bin/env python3
from calculator_adapter import run


### ADD AT LEAST TWO TESTS HERE!

# Checks that the program outputs "7" for an input of "3 + 4"
assert run("3 + 4").output == "7"
# Checks that the program outputs "8" for an input of "3 * 7"
assert run("3 * 7").output == "21"
# Checks that the program outputs "2" for an input of "10 - 8"
assert run("10 - 8").output == "2"
# Checks that the program outputs "4" for an input of "20 / 5"
assert run("20 / 5").output == "4"
# Checks that the program exists successfully (no error) for input "3 * 7"
assert run("3 * 7").exit_status == 0
# Checks that the program fails (correctly errors) for input "1 ! 9"
assert run("1 ! 9").exit_status != 0

###

print("All tests passed!")