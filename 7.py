peso = float(input ("introduce peso en kg: "))
altura = float(input ("introduce altura en metros: "))
imc = round(float (peso) / float(altura) ** 2,2)
print ("imc: " + str(imc))