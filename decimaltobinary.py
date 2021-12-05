
ARR = [128, 64, 32, 16, 8, 4, 2, 1]
arr_inc = []


def start():
    DEC = int(input("Vendosni numrin tuaj(Decimal): "))
    global ARR
    while DEC != 0:
        for arr_index in ARR:
            if DEC - arr_index < 0:
                arr_index = 0
                arr_inc.append(arr_index)

            elif DEC - arr_index >= 0:
                DEC = DEC - arr_index
                arr_index = 1
                arr_inc.append(arr_index)
        print("Numri ne binare: ")
        print(*arr_inc)
        break


if __name__ == "__main__":
    start()
