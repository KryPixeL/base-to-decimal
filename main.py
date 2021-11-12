"""
Binary to Decimal Convertor
"""

INVALID = [2, 3, 4, 5, 6, 7, 8, 9]  # values impossible in binary

while True:
    try:
        char_base2 = []
        base2 = input("Insert binary string: ")

        # non-numerical numbers present if conversion returns false
        if not base2.isnumeric():
            raise Exception("String is not numeric")

        # binary string converted to list of chars
        for char in base2[0:len(base2)]:
            if int(char) in INVALID:
                # if any char is not 0 or 1, raise exception
                raise Exception("String contains non-binary values")

            else:
                char_base2.append(int(char))

        # handled in reverse for ease
        char_base2.reverse()
        on_bit_list = []

        for i, j in enumerate(char_base2):
            # keep list of every activated bit
            if j == 1:
                on_bit_list.append(i)

        value = 1
        value_list = []

        # get value of each char in binary string
        for char in char_base2:
            value_list.append(value)
            value *= 2

        base10 = 0

        # for every activated bit
        for on_index in on_bit_list:
            # add activated bit's value to sum
            base10 += value_list[on_index]

        # return binary and decimal conversion
        print("\n" + base2, "->", base10, "\n")

    except Exception as e:
        print(e)  # return a raised exception
