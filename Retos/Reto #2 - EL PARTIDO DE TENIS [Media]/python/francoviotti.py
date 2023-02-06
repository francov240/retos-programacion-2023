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

player1_score = 0
player2_score = 0

def tennis_score(player):
    score_list = ["Love", "15", "30", "40", "Deuce"]
    '''
    first_time_in = 0
    if first_time_in == 0:
        player1_score = 0
        player2_score = 0
        first_time_in = False
    '''
    if(player == "P1"):
        player1_score += 1
    elif(player == "P2"):
        player2_score += 1

    if player1_score == 4 and player2_score < 4:
        print("Player 1 wins!")
        player1_score == 0
        player2_score == 0
        return
    elif player2_score == 4 and player1_score < 4:
        print("Player 2 wins!")
        player1_score == 0
        player2_score == 0
        return
    elif player2_score == 4 and player1_score == 4:
        print("Deuce")
        return
    
    
    print(score_list[player1_score] +" "+score_list[player2_score])

while(True):
    tennis_score(input())

'''
Va tomando forma. Falta controlar quien gana y el tema de los empates
'''