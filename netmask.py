#!/usr/bin/env python
# -*- coding: utf-8 -*-

import curses

def principal():
    ## ESTA FUNCIÓN DEVUELVE LA IP PRINCIPAL, EL NÚMERO CIDR, Y LA MÁSCARA EN ESE ORDEN
    print("%s Introduce la IP (opcionalmente acepto notación CIDR: 'IP[/[0-32]]' )" % simbolo_pregunta)
    entrada_teclado = pedir_ip()
    contenido = entrada_teclado.rpartition('/')
    notacion_es_CIDR = True if contenido[1] == '/' else False
    global ip_principal
    global CIDR
    global mascara
    if notacion_es_CIDR:
        ip_es_valida = True if comprobar_ip(contenido[0]) else False
        if ip_es_valida:
            ip_principal = contenido[0]
            CIDR = contenido[2] if comprobar_mascara(contenido[2]) else False
            if not CIDR:
                mascara = pedir_mascara()
        elif not ip_es_valida:
            principal()
    elif not notacion_es_CIDR:
        ip_principal = entrada_teclado if comprobar_ip(entrada_teclado) else False
        if not ip_principal:
            principal()
        mascara = pedir_mascara()

def pedir_mascara():
    mascara = False
    while not mascara:
        print("%s Introduce la máscara en notación decimal puntuada o número CIDR /[0-32]." % simbolo_pregunta)
        entrada_teclado = pedir_ip()
        mascara = entrada_teclado if comprobar_mascara(entrada_teclado) else False
        if not mascara:
            error("máscara", entrada_teclado)
    return mascara

def comprobar_mascara(numero):
    valores = numero.rpartition('/')
    valores2 = numero.split('.')
    if valores[1] == '/' or len(valores2) == 1:
        if 0 <= int(valores[2]) <= 32:
            return True
        else:
            error('Notación CIDR', valores[2])
            return False
    else:
        if len(valores2) == 4:
            permitidos = (255, 254, 252, 248, 240, 224, 192, 128, 0)
            for x in valores2:
                if not int(x) in permitidos:
                    error('Valor de máscara', x)
                    return False
            return True
        else:
            error('Número', numero)
            return False

def error(tipo_error, IP):
    print("%s %s '%s' errónea!! Pon más atención la próxima vez." % (simbolo_error, tipo_error, IP))

def comprobar_ip(IP):
    valores_IP = IP.split('.')
    valido = True if (len(valores_IP) == 4) else False
    if valido:
        for x in valores_IP:
            if not 0 <= int(x) <= 255:
                error('IP', IP)
                return False
    return True

def pedir_ip():
    IP = raw_input("IP: ")
    return IP


############################## Zona Curses

def iniciar():
    global screen
    screen = curses.initscr()
    curses.noecho()
    curses.curs_set(0)
    screen.keypad(1)
    screen.refresh()
    global posicion_inicial
    posicion_inicial = 0
    crear_menu_principal(screen.getmaxyx())
    elementos_menu(0)
    menu_principal.refresh()
    crear_zona_de_salida(screen.getmaxyx())
    avanza = 0
    pulsacion = 0
    while pulsacion != curses.KEY_EXIT:
        if pulsacion == curses.KEY_RIGHT or pulsacion == curses.KEY_DOWN:
            avanza = avanza + 1
        elif pulsacion == curses.KEY_LEFT or pulsacion == curses.KEY_UP:
            avanza = avanza - 1
        elif pulsacion == curses.KEY_ENTER:
            acceder
        elif pulsacion == curses.KEY_RESIZE:
            refrescar_todo()
        posicion = avanza % 3
        elementos_menu(posicion)
        menu_principal.refresh()
        pulsacion = screen.getch()

    curses.endwin()

def refrescar_todo():
    crear_menu_principal(screen.getmaxyx())
    crear_zona_de_salida(screen.getmaxyx())

def crear_menu_principal(tamanyo):
    global menu_principal
    menu_principal = curses.newwin(3, tamanyo[1], 0, 0)
    menu_principal.border(0)
    screen.refresh()


def elementos_menu(posicion):
    primero = 'IP Principal'
    segundo = 'Calculadora'
    tercero = 'Salir'
    offset = 2
    separacion = 2
    if int(posicion) == 0:
        attrib1 = curses.A_REVERSE
        attrib2 = curses.A_NORMAL
        attrib3 = curses.A_NORMAL
    elif int(posicion) == 1:
        attrib1 = curses.A_NORMAL
        attrib2 = curses.A_REVERSE
        attrib3 = curses.A_NORMAL
    elif int(posicion) == 2:
        attrib1 = curses.A_NORMAL
        attrib2 = curses.A_NORMAL
        attrib3 = curses.A_REVERSE
    menu_principal.addstr(1, offset, primero, attrib1)
    menu_principal.addstr(1, len(primero) + offset + separacion, segundo, attrib2)
    menu_principal.addstr(1, len(primero) + len(segundo) + offset + separacion * 2, tercero, attrib3)
    screen.refresh()

def crear_zona_de_salida(tamanyo):
    global zona_de_salida
    zona_de_salida = curses.newwin(tamanyo[0]-3, tamanyo[1], 3, 0)
    zona_de_salida.border(0)
    zona_de_salida.refresh()

simbolo_error = "\033[93;1m[\033[91;1m - \033[93;1m]\033[0m"
simbolo_info = "\033[93;1m[\033[92;1m + \033[93;1m]\033[0m"
simbolo_pregunta = "\033[93;1m[\033[34;1m ? \033[93;1m]\033[0m"

#principal() 
iniciar()
