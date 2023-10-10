from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola amigos!")

def salud_con_input(request):
    nombre = input("dime tu nombre: ")
    
    return HttpResponse(f"Hola {nombre}")
    
def aleatorio(request):
    import random
    numero = random.randint(1, 6)
    
    if numero == 6:
        return HttpResponse(f"has tenido suerte, salio {numero}")
    
    else:
        return HttpResponse(f"no has tenido suerte, salio {numero}")
    
    