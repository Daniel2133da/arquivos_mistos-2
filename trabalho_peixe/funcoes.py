
# students = [
#     ['NOME',   'Kg' ],
#     ['Jõao',    17],
#     ['Daniel',  17],
#     ['Marla',   15],
#     ['Tonia',   16],
# ]

# for i, km in enumerate(students):
#     if i == 0:
#         continue
#     print(km)

def isNumero(numero: float):
    valido = False
    try:
        float(numero)
        valido = True
    except:
        valido = False
    return valido

def isLetra(string: str):
    valido = False
    for str in string:
        try:
            float(str)
            valido = False
            return valido
        except:
            valido = True
    return valido

print('lal lalal')
