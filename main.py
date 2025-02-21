import random
import china, austria
import sys
from austria import cook as austria_cook
from china import cook as china_cook
from latam.argentina import cook as argentina_cook
from latam.brazil import cook as brazil_cook
from latam.mexico.yucatan import cook as yucatan_cook

def cook():
    print('we are making paella')

print('a random number is', random.randint(1,10))

china.greet()
china.cook()

austria.greet()
austria.cook()

for p in sys.path:
    print(p)

cook()

austria_cook()

china_cook()

argentina_cook()
brazil_cook()
yucatan_cook()