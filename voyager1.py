days_after = input("Number of days after 9/25/09: ")
day_number = float(days_after)

mile_speed = 38241
km_speed = mile_speed*1.609344
au_speed = mile_speed/92955887.6

miles_from_sun = 16637e6
miles_movement = day_number*(mile_speed*24)

km_from_sun = round(miles_from_sun*1.609344)
km_movement = round(day_number*(km_speed*24))

au_from_sun = round(miles_from_sun/92955887.6)
au_movement = round(day_number*(au_speed*24))
                    
print("Miles from the sun:",int(miles_movement+miles_from_sun))
print("Kilometers from the sun:",km_movement+km_from_sun)
print("AU from the sun:",au_movement+au_from_sun)
