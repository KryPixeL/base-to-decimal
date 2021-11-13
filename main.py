"""
Base to Decimal Convertor
"""

while True:
    try:
        char_base = []

        base_increase = int(input("Base: "))

        if base_increase > 10:
            raise Exception("Base value may not exceed 10\n")

        base = input("Insert base string: ")

        # non-numerical numbers present if conversion returns false
        if not base.isnumeric():
            raise Exception("Base string may not contain non-numeric values\n")

        # base string converted to list of chars
        for char in base:
            if int(char) in range(0, base_increase):
                char_base.append(int(char))

            else:
                # raise exception if any char defies base domain
                raise Exception("String values not within base domain\n")

        # handled in reverse for ease
        char_base.reverse()

        value = 1
        value_list = []

        # get value of each char in base string
        for char in char_base:
            value_list.append(value)
            value *= base_increase

        decimal = 0

        # add values for each char in string to sum
        for i, j in enumerate(char_base):
            decimal += value_list[i] * j

        # return base string and decimal conversion
        print("\n" + base, "->", decimal, "\n")

    except Exception as e:
        print(e)
