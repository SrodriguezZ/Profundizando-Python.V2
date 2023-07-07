#Convertidor de F_c y C_F
class Convertidor_Temperatura:
    #cuando esta esta en mayúscula por las buenas practicas de python no se 
    #puede tocar la variable y se la toma como una constante
    MAX_CELSIUS = 100
    MAX_FAHRENHEIT = 213
    @classmethod
    def _C_F(cls, Celsius):
        if Celsius > cls.MAX_CELSIUS:
            raise ValueError (f'Temperatura C demasiada alta: {Celsius}')
        return Celsius*9/5+32
    @classmethod
    def _F_C(cls, Fahrenheit):
        if Fahrenheit > cls.MAX_FAHRENHEIT:
            raise ValueError(f'Temperatura F demasiada alta:{Fahrenheit}')
        return (Fahrenheit-32)*5/9

print('Hello')
if __name__ =='__main__':    
    Resultado = Convertidor_Temperatura._F_C(200)
    print(f'{Resultado:.2f}')
