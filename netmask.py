#!/usr/bin/env python
# -*- coding: utf-8 -*-

def principal():
    print("%s Introduce la IP (opcionalmente acepto notación CIDR: 'IP[/[0-32]]' )" % simbolo_pregunta)
    entrada_teclado = pedir_ip()
    contenido = entrada_teclado.rpartition('/')
    notacion_es_CIDR = True if contenido[1] == '/' else False
    # Si hay número CIDR:
    if notacion_es_CIDR:
        ip_es_valida = True if comprobar_ip(contenido[0]) else False
        # Si el número CIDR es válido y la IP también
        if ip_es_valida:
            # guardo IP y CIDR
            ip_principal = contenido[0]
            # si CIDR es válido guardarlo, si no pedir máscara.
            CIDR = contenido[2] if comprobar_mascara(contenido[2]) else False
            if not CIDR:
                pedir_mascara()
        # si la IP no es válida, la pido de nuevo junto con la máscara.
        elif not ip_es_valida:
            principal()
    # si no se ha metido notación CIDR, comprobar si lo introducido es una IP y es válida.
    elif not notacion_es_CIDR:
        ip_principal = entrada_teclado if comprobar_ip(entrada_teclado) else False
        if not ip_principal:
            principal()
        pedir_mascara()

def pedir_mascara():
    mascara = False
    while not mascara:
        print("%s Introduce la máscara en notación decimal puntuada o número CIDR /[0-32]." % simbolo_pregunta)
        entrada_teclado = pedir_ip()
        mascara = entrada_teclado if comprobar_mascara(entrada_teclado) else False
        if not mascara:
            error("máscara", entrada_teclado)

def comprobar_mascara(numero):
    valores = numero.rpartition('/')
    valores2 = numero.split('.')
    if valores[1] == '/' or len(valores2) == 1:
        if 0 <= int(valores[2]) <= 32:
            return True
        else:
            return False
    else:
        if len(valores2) == 4:
            permitidos = (255, 254, 252, 248, 240, 224, 192, 128, 0)
            for x in valores2:
                if not int(x) in permitidos:
                    return False
            return True
        else:
            return False

def error(tipo_error, IP):
    print("%s %s '%s' errónea!! Pon más atención la próxima vez." % (simbolo_error, tipo_error, IP))

def comprobar_ip(IP):
    valores_IP = IP.split('.')
    valido = True if (len(valores_IP) == 4) else False
    # Si hay numero IP
    if valido:
        for x in valores_IP:
            # Si hay un número entero IP fuera de rango devuelve 0
            if not 0 <= int(x) <= 255:
                error('IP', IP)
                return False
    # Si los 4 número son correctos devuelve 1
    return True

def pedir_ip():
    IP = raw_input("IP: ")
    return IP

simbolo_error = "\033[93;1m[\033[91;1m - \033[93;1m]\033[0m"
simbolo_info = "\033[93;1m[\033[92;1m + \033[93;1m]\033[0m"
simbolo_pregunta = "\033[93;1m[\033[34;1m ? \033[93;1m]\033[0m"

principal() 
