print(

)
import time


def coparation():
    compar_value = 1
    while True:

        with open ('arquivo_vrpk.kv', 'r') as f:
            text_compare_one = f.read()

        with open ('vrpk_2.txt', 'r') as f:
            text_compare_two = f.read()

        time.sleep(1)
    
        if text_compare_one == text_compare_two:
            print('{} compar: os textos são iguais!'.format(compar_value))
        elif text_compare_one != text_compare_two:
            print('{} compar: os textos são diferentes!'.format(compar_value))
        compar_value +=1


print(

)
coparation()