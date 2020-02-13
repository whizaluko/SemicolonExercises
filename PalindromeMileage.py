
for mile in range(1_000_000):
    mile_str =str(mile)

    last_four = mile_str[-4:]
    last_five = mile_str[-5:]

    if last_four == last_four[::-1] and last_five != last_five[::-1]:
        mile_str = str (mile+1)
        last_five = mile_str[-5:]

        if last_five == last_five[::-1]:
            mile_str = str(mile + 2)
            mid_four = mile_str[1:5]

            if mid_four == mid_four[::-1]:
                mile_str = str(mile+3)

                if mile_str == mile_str[::-1]:
                    print(f"The total mileage is {mile} miles")








