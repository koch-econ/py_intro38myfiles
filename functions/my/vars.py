x=123

def ref_var_loc():
    x=0
    print(x)


def ref_var_glo():
    print(x)


def main():
    ref_var_glo()
    ref_var_loc()


main()