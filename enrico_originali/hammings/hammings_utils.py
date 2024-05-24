


def bindigits_list_from_num(num):
    # restituisce la codifica in binario come lista di interi, 0 e 1
    
    bin_temp = bin(num)[2:]
    bin_digits_list = [0 if c == "0" else 1 for c in bin_temp]

    return bin_digits_list



if __name__ == "__main__":

    # quick & dirty tests
    print(bindigits_list_from_num(1024))