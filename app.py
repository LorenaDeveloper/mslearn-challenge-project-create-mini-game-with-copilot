import random

ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'

options = [ROCK, PAPER, SCISSORS]

user_score = 0
computer_score = 0
rounds = 0
scores = [user_score, computer_score, rounds]

#pregunta por la opción del jugador
def get_player_option():
    return input('Choose rock, paper or scissors: ').lower()

#genera una opcion aleatoria
def get_random_option():
    return random.choice(options)

#compara las opciones del jugador y la computadora
def get_winner(player_option, computer_option):
    if player_option == computer_option:
        return 'draw'
    if player_option == ROCK and computer_option == SCISSORS:
        return 'player'
    if player_option == PAPER and computer_option == ROCK:
        return 'player'
    if player_option == SCISSORS and computer_option == PAPER:
        return 'player'
    return 'computer'

#muestra resultados de la partida
def show_results(scores, winner):
    if winner == 'player':
        scores[0] += 1
    elif winner == 'computer':
        scores[1] += 1
    scores[2] += 1
    return scores

def play(scores):
    computer_option = get_random_option()
    user_option = get_player_option()

    #comprueba que la opción del jugador sea válida
    while user_option not in [ROCK, PAPER, SCISSORS]:
        print('Invalid option')
        user_option = get_player_option()
        
    print('Computer option:', computer_option)
    print('Player option:', user_option)
    if get_winner(user_option, computer_option) == 'player':
        print('You win!')
        scores = show_results(scores, 'player')
    elif get_winner(user_option, computer_option) == 'computer':
        print('You lose!')
        scores = show_results(scores, 'computer')
    else:
        print('Draw!')
        scores = show_results(scores, 'draw')

play_again = 'yes'
while play_again == 'yes':
    play(scores)
    #mientras play_again sea distinto de 'yes' y de 'no' seguir el bucle
    play_again = input('Do you want to play again? (yes/no): ').lower()
    while play_again not in ['yes', 'no']:
        print('Invalid option')
        play_again = input('Do you want to play again? (yes/no): ').lower()
        
    if play_again == 'no':
        print('User score:', scores[0])
        print('Rounds:', scores[2])
        print('Goodbye!')

