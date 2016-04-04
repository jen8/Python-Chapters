import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)
    
def add_fruit(inventory, fruit, quantity = 0):
    previous_quantity = inventory.get(fruit, 0)    
    inventory[fruit] = quantity + previous_quantity


# Make these tests work...
new_inventory = {}
add_fruit(new_inventory, "strawberries", 10)

test("strawberries" in new_inventory)
test(new_inventory["strawberries"] == 10)


add_fruit(new_inventory, "strawberries", 25)
test(new_inventory["strawberries"] == 35)
