
KOCH_NUM=123.456
KOCH_STR="YOKLMN"
def koch_func(x):
    return x/KOCH_NUM
if __name__=="__main__":
    print('тестируем'+__name__)
    print(koch_func(KOCH_NUM))
else:
    print("импортируем "+__name__)
