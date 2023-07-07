from decimal import Decimal
import math
#NaN - nOT A NUMBER ( NO ES UN NUMERO)
#NAN NO ES SENSIBLE A MAYÚSCULA/MINÚSCULA
#NAN ES UN TIPO DE DATA NUMÉRICO INDEFINIDO
a = float('NaN')
print(f'Es NaN(not a number: ){math.isnan(a)}')
a = Decimal('Nan')
print(f'Es NaN(not a number: ){math.isnan(a)}')