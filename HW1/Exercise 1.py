# def temp_compare(normal, num):
#     if(abs(num-normal) <= 1):
#         print("true")
#         return True
#     print("false")
#     return False

def temp_tester(normal):
    def temp_compare(observed):
        if(abs(observed-normal) <= 1):
            print("true")
            return True
        print("false")
        return False
    return temp_compare


# Tests
human_tester = temp_tester(37)
chicken_tester = temp_tester(41.1)

chicken_tester(42) # True -- i.e. not a fever for a chicken
human_tester(42)   # False -- this would be a severe fever for a human
chicken_tester(43) # False
human_tester(35)   # False -- too low
human_tester(98.6) # False -- normal in degrees F but our reference temp was in degrees C

# Additional tests
human_tester(40) # False
chicken_tester(40) # False
human_tester (40) # False
human_tester(36.5) # True
chicken_tester(36.5) # False 