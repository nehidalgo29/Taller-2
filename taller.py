Spyder Editor
This is a temporary script file.
"""
numeros=[1,2,3,4,16,7,12,9,6,111]

arreglo=[20,"hello",3,"nestor",1,2,3,4]

letras=['A','B','C','D','E','z','y']

arregloslice=arreglo[1:-1]

letras.sort()

arregloextendido=numeros

arregloextendido.extend(letras)

print(letras)

letras.sort(key=str.lower)

letras