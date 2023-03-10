"""/*
 * Crea un programa que calcule quien gana mΓ‘s partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La funciΓ³n recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "πΏ" (piedra), "π" (papel),
 *   "βοΈ" (tijera), "π¦" (lagarto) o "π" (spock).
 * - Ejemplo. Entrada: [("πΏ","βοΈ"), ("βοΈ","πΏ"), ("π","βοΈ")]. Resultado: "Player 2".
 * - Debes buscar informaciΓ³n sobre cΓ³mo se juega con estas 5 posibilidades.
 */"""
from enum import Enum

#Utilizamos la libreria enum para dar valores a los movimientos
class Valores(Enum):
    PIEDRA = "πΏ"
    PAPEL = "π"
    TIJERA = "βοΈ"
    LAGARTO = "π"
    SPOCK = "π"

#Definimos la funcion del juego
def game_pptls(game : list[tuple[str,str]]):
    p1_score = 0
    p2_score = 0
    
    for move in game:
        p1_move = move[0]
        p2_move = move[1]
        
        if p1_move != p2_move: #Creamos las condiciones de los movimientos con la suma de puntos
            if (p1_move == "πΏ" and p2_move == "βοΈ") or (p1_move == "π" and p2_move == "πΏ") or (p1_move == "βοΈ" and p2_move == "π") or (p1_move == "π" and p2_move == "π") or (p1_move == "π" and p2_move == "πΏ"):
                p1_score += 1
            else:
                p2_score += 1

#Definimos los resultados segun su puntuacion
    if p1_score == p2_score:
        print('Tie!')
    elif p1_score > p2_score:
        print('Player 1')
    elif p2_score > p1_score:
        print('Player 2')
        
game_pptls([("π","πΏ"),("βοΈ","πΏ"),("π","πΏ")])
game_pptls([("π","π"),("π","π"),("βοΈ","π")])
game_pptls([("π","π"),("π","π"),("π","π"),("πΏ","βοΈ"),("π","πΏ")])