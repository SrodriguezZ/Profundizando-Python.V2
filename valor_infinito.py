from decimal import Decimal
import math
valor_infinito = float('inf')
valor_negativo = float('inf')
#print(f'es valor infinito: {math.isinf(valor_infinito)}')
#print(f'es valor negativo ?: {math.isinf(valor_negativo)}')

#Modulo MATH
valor_infinito = math.inf
valor_negativo = -math.inf

#Modulo Decimal
valor_infinito = Decimal('Infinity')
valor_negativo = Decimal('-Infinity')
print(f'Valor infinito: {valor_negativo}')
print(f'Es valor infinito: {math.isinf(valor_negativo)}')