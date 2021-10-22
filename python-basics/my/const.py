TOLSTOY_BIRTH_YEAR=1828

FLAG_SMART=2**0
FLAG_QUTE=2**1
FLAG_FUNNY=2**2
FLAG_QUIET=2**3

charact=FLAG_FUNNY|FLAG_SMART

print(bin(FLAG_FUNNY))
print(bin(FLAG_SMART))
print(bin(charact))

print(bin(charact&FLAG_SMART))




