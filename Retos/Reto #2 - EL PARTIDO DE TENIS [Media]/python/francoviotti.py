'''
 Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 gane cada punto del juego.
  
 - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
   15 - Love
   30 - Love
   30 - 15
   30 - 30
   40 - 30
   Deuce
   Ventaja P1
   Ha ganado el P1
 - Si quieres, puedes controlar errores en la entrada de datos.   
 - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
 '''

def tennis_score(player):
    score_list = ["Love", "15", "30", "40", "Deuce"]
    first_time_in = True
    if first_time_in:
        player1_score = 0
        player2_score = 0
        first_time_in = False
    if(player == "P1"):
        player1_score += 1
    elif(player == "P2"):
        player2_score += 1

    if
    
    print(score_list[player1_score] +" "+score_list[player2_score])

tennis_score("P1")

'''
Va tomando forma. Falta controlar quien gana y el tema de los empates
'''