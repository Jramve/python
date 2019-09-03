pswd = "contraseña"
passUser = input("Introduzca la contraseña: ")
count = 0
for i in passUser.lower():
    if pswd[count] == i:
        if count == len(pswd):
            print ("las contraseñas coinciden")
        else:
            count = count + 1
    else: 
        print("no coincide la contraseña ")
        break



