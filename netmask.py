#!/usr/bin/env python
# -*- coding: utf-8 -*-

def principal():
    print("Introduce la IP (acepto notación CIDR: 'IP/[0-32]' )")
    ip_principal_decimal = pedir_ip()
    contenido = ip_principal_decimal.rpartition('/')
    notacion_es_CIDR = True if contenido[1] == '/' else False
    # Si hay número CIDR:
    if notacion_es_CIDR:
        ip_es_valida = True if comprobar_ip(contenido[0]) else False
        # Si el número CIDR es válido y la IP también
        if ip_es_valida:
            # guardo IP y CIDR
            ip_principal = contenido[0]
            print("IP: %s" % ip_principal)
            # si CIDR es válido guardarlo, si no pedir máscara.
            if 0 <= int(contenido[2]) <= 32:
                CIDR = contenido[2]
                print("CIDR: %s" % CIDR)
            else:
                pedir_mascara()
        # si la IP no es válida, la pido de nuevo junto con la máscara.
        elif not ip_es_valida:
            principal()
    # si no se ha metido notación CIDR, comprobar si lo introducido es una IP y es válida.
    elif not notacion_CIDR:
        pass

def error(tipo_error, IP):
    simbolo = "\033[93;1m[\033[91;1m-\033[93;1m]\033[0m"
    print("%s %s '%s' errónea!! Pon más atención la próxima vez." % (simbolo, tipo_error, IP))

def comprobar_ip(IP):
    valores_IP = IP.split('.')
    valido = True if (len(valores_IP) == 4) else False
    # Si hay numero IP
    if valido:
        for x in valores_IP:
            # Si hay un número entero IP fuera de rango
            if not 0 <= int(x) <= 255:
                error('IP', IP)
                return False
    # Si los 4 número son correctos
    return True

def pedir_ip():
    IP = raw_input("IP: ")
    return IP

principal()    
