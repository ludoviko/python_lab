# Write your code here
import random, re


class PieceScored:
    piece = []
    score = 0

    def __str__(self):
        return f'Piece {self.piece}, score {self.score}'

def find_piece_in_set(a_set, a_piece):
    a_set.remove(a_piece)
    return a_piece


def generate_set(a_source):
    a_set = []

    for i in range(0, 7):
        a_set.append(a_source.pop())

    return a_set


def generate_main_set():
    main_set = []

    for i in range(0, 7):
        for j in range(i, 7):
            piece = []
            piece.append(i)
            piece.append(j)
            main_set.append(piece)

    return main_set


def inverse_piece(a_piece):
    a_piece.reverse()


def read_head_and_tail(gamer_pieces):
    return [gamer_pieces[0][0], gamer_pieces[-1][1]]


def init_game():
    pieces = []
    player = []
    computer = []

    domino_snake = []

    while True:
        pieces = generate_main_set()
        random.shuffle(pieces)
        player = generate_set(pieces)
        computer = generate_set(pieces)

        if six_double in computer:
            domino_snake.append(find_piece_in_set(computer, six_double))
            status = status_player
            break
        elif six_double in player:
            domino_snake.append(find_piece_in_set(player, six_double))
            status = status_computer
            break
        elif six_five in computer:
            domino_snake.append(find_piece_in_set(computer, six_five))
            status = status_player
            break
        elif six_five in player:
            domino_snake.append(find_piece_in_set(player, six_five))
            status = status_computer
            break

    return [pieces, computer, player, domino_snake, status]


def play_gamer(gamer_pieces, snake_pieces, stock_pieces, move_num):
    if move_num > 0:
        move_num = move_num - 1
        a_piece = gamer_pieces.pop(move_num)

        snake_head_tail = read_head_and_tail(snake_pieces)

        # check head: snake_head_tail[0]
        if snake_head_tail[1] in a_piece:
            if a_piece[1] == snake_head_tail[1]:
                inverse_piece(a_piece)

            snake_pieces.append(a_piece)

        # check tail: snake_head_tail[1]
    elif move_num < 0:
        move_num = move_num + 1

        a_piece = gamer_pieces.pop(abs(move_num))

        snake_head_tail = read_head_and_tail(snake_pieces)

        if snake_head_tail[0] in a_piece:
            if a_piece[0] == snake_head_tail[0]:
                inverse_piece(a_piece)

            snake_pieces.insert(0, a_piece)
    elif move_num == 0:
        if len(stock_pieces) > 0:
            a_piece = stock_pieces.pop()
            gamer_pieces.append(a_piece)


def play_computer_gamer(gamer_pieces, snake_pieces, stock_pieces, a_piece_scored_array):

    any_good_piece = False
    snake_head_tail = read_head_and_tail(snake_pieces)

    for a_piece_scored in a_piece_scored_array:
        if a_piece_scored.piece[0] in snake_head_tail:
            gamer_pieces.remove(a_piece_scored.piece)

            if a_piece_scored.piece[0] == snake_head_tail[0]:
                inverse_piece(a_piece_scored.piece)
                snake_pieces.insert(0, a_piece_scored.piece)
            elif a_piece_scored.piece[0] == snake_head_tail[1]:
                snake_pieces.append(a_piece_scored.piece)

            return
        elif a_piece_scored.piece[1] in snake_head_tail:
            gamer_pieces.remove(a_piece_scored.piece)

            if a_piece_scored.piece[1] == snake_head_tail[0]:
                snake_pieces.insert(0, a_piece_scored.piece)
            elif a_piece_scored.piece[1] == snake_head_tail[1]:
                inverse_piece(a_piece_scored.piece)
                snake_pieces.append(a_piece_scored.piece)

            return

    if len(stock_pieces) > 0:
        a_piece = stock_pieces.pop()
        gamer_pieces.append(a_piece)


def check_permanent_stop(a_snake):
    max_repetitions = 7
    counter = 0
    a_digit = None

    if a_snake[0][0] == a_snake[-1][1]:
        a_digit = a_snake[0][0]
    else:
        return False

    for a_piece in a_snake:
        if a_digit in a_piece:
            counter = counter + 1

    return counter == max_repetitions


def check_legal_move(gamer_pieces, snake_pieces, move_num):
    if move_num > 0:
        move_num = move_num - 1

        # a peek is simulated
        a_piece = gamer_pieces.pop(move_num)
        gamer_pieces.insert(move_num, a_piece)

        snake_head_tail = read_head_and_tail(snake_pieces)

        if a_piece[0] == snake_head_tail[1] or a_piece[1] == snake_head_tail[1]:
            return True
        else:
            return False
    elif move_num < 0:
        move_num = move_num + 1

        # a peek is simulated
        a_piece = gamer_pieces.pop(abs(move_num))
        gamer_pieces.insert(abs(move_num), a_piece)

        snake_head_tail = read_head_and_tail(snake_pieces)

        if a_piece[0] == snake_head_tail[0] or a_piece[1] == snake_head_tail[0]:
            return True
        else:
            return False
    else:
        return True


def print_pieces(gamer_pieces):
    pieces_s = ""
    if len(gamer_pieces) < 7:
        for each in gamer_pieces:
            pieces_s = pieces_s + str(each)
        print(pieces_s)
    else:
        print("{}{}{}...{}{}{}".format(gamer_pieces[0], gamer_pieces[1], gamer_pieces[2],
                                       gamer_pieces[-3], gamer_pieces[-2], gamer_pieces[-1]))


def print_info(p_data_game):
    print("======================================================================")
    print("Stock size:", len(p_data_game[0]))
    print("Computer pieces:", len(p_data_game[1]))
    print()
    # Print snake
    print_pieces(p_data_game[3])
    print()

    i = 1
    print("Your pieces:")
    for each in p_data_game[2]:
        print("{}:{}".format(i, each))
        i = i + 1

    print()
    if p_data_game[4] == status_player:
        print("Status: It's your turn to make a move. Enter your command.")
    else:
        print("Status: Computer is about to make a move. Press Enter to continue...")


def count_occurrences(n, array_pieces):
    counter = 0

    for a_piece in array_pieces:
        for element in a_piece:
            if element == n:
                counter = counter + 1

    return counter


def update_map_occurrences(a_map, array_pieces):

    for i in range(0, 7):
        a_map[i] = count_occurrences(i, array_pieces) + a_map.get(i, 0)


def get_score(a_piece, a_map):
    score = a_map.get(a_piece[0], 0)
    score = a_map.get(a_piece[1], 0) + score

    return score


def create_piece_scored_array(array_pieces, a_map):
    piece_scored_array = []

    for a_piece in array_pieces:
        score = get_score(a_piece, a_map)
        a_piece_scored = PieceScored()
        a_piece_scored.piece = a_piece
        a_piece_scored.score = score

        piece_scored_array.append(a_piece_scored)

    return piece_scored_array


def my_field(element):
  return element.score


# Start of the program.
six_double = [6, 6]
six_five = [5, 6]
status_player = "Player"
status_computer = "Computer"
patternInteger = re.compile("^[+-]?[0-9]+$")

all_pieces, computer_pieces, player_pieces, domino_snake, status = init_game()

move = ""
move_n = None
piece = None

while True:
    print_info([all_pieces, computer_pieces, player_pieces, domino_snake, status])

    if status == status_player:
        move = input()

        while True:
            while not patternInteger.match(move) or abs(int(move)) > len(player_pieces):
                print("Invalid input. Please try again.")
                move = input()

            # The piece does not fit into the snake.
            if not check_legal_move(player_pieces, domino_snake, int(move)):
                print("Illegal move. Please try again.")
                move = input()
            else:
                break

        play_gamer(player_pieces, domino_snake, all_pieces, int(move))
    else:
        # read enter as computer plays
        input()

        map_occurrences = {}
        update_map_occurrences(map_occurrences, domino_snake)
        update_map_occurrences(map_occurrences, computer_pieces)

        piece_scored_array = create_piece_scored_array(computer_pieces, map_occurrences)

        piece_scored_array.sort(key=my_field, reverse=True)

        head_and_tail = read_head_and_tail(domino_snake)

        play_computer_gamer(computer_pieces, domino_snake, all_pieces, piece_scored_array)

    if status == status_player:
        status = status_computer
    else:
        status = status_player

    if len(computer_pieces) == 0 or len(player_pieces) == 0 or check_permanent_stop(domino_snake):
        print_info([all_pieces, computer_pieces, player_pieces, domino_snake, status])

        break


if len(computer_pieces) == 0 and len(player_pieces) == 0:
    print("Status: The game is over. It's a draw!")
elif len(computer_pieces) == 0:
    print("Status: The game is over. The computer won!")
elif len(player_pieces) == 0:
    print("Status: The game is over. You won!")
elif check_permanent_stop(domino_snake):
    print("Status: The game is over. It's a draw!")
