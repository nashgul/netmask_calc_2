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
        if ip_es_valida and 0 <= int(contenido[2]) <= 32:
# guardo IP y CIDR
            ip_principal = contenido[0]
            CIDR = contenido[2]
            print("IP: %s" % ip_principal)
            print("CIDR: %s" % CIDR)
        elif not ip_es_valida:
# si la IP no es válida, la pido de nuevo junto con la máscara.
            principal()
# si no es válida la notación CIDR, pido máscara.
        else: 
            print("[-] Número CIDR %s incorrecto." % contenido[2])
# si no se ha metido notación CIDR
    elif not notacion_CIDR:
        pass

def error_ip(IP):
    print("[-] IP '%s' errónea!! Pon más atención la próxima vez." % IP)

def comprobar_ip(IP):
    valores_IP = IP.split('.')
    valido = True if (len(valores_IP) == 4) else False
# Si hay numero IP
    if valido:
        for x in valores_IP:
# Si hay un número entero IP fuera de rango
            if not 0 <= int(x) <= 255:
                error_ip(IP)
                return False
# Si los 4 número son correctos
    return True
def pedir_ip():
    IP = raw_input("IP: ")
    return IP

principal()    
