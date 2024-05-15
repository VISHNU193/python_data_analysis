capitals ={"Karnataka":"Bangalore","Maharashtra":"Mumbai","Tamil Nadu":"Chennai"}

print(capitals.keys())
print(capitals.values())
print(capitals.items())
print(capitals.get("Karnataka"))
print(capitals)

other_capitals = {"Gujrat":"Ahmedabad",}
capitals.update(other_capitals)
print(other_capitals)

