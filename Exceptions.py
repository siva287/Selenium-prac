
items_in_cart = 0

if items_in_cart != 0:
    #raise Exception("Product cart count not match")
    pass

try:
    assert(items_in_cart == 1)

except Exception as e:
    print("Exception is", e)
    print("there is an exception in try block")

finally:
    print("finally block")
