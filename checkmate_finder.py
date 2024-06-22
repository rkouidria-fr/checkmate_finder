"""
 Ce module vérifie si un échec et mat est possible en moins de 5 coups à partir
 de la dernière position d'un fichier .pgn.
"""

import os
import chess
import chess.pgn

PGN_FILE = os.path.join(os.getcwd(), "checkmate.pgn")
DEPTH = 5  # le nombre de tours à explorer

def mate_exists(board, depth=DEPTH * 2):
    """
    Vérifie si un échec et mat peut être atteint en moins de DEPTH coups
    complets (10 demi-coups).

    Args:
        board (chess.Board): Instance représentant la position actuelle
        depth (int, optional): Profondeur maximale de calcul en nombre de tour.
            Defaults to None.

    Returns:
        bool: True si un échec et mat est possible en moins de DEPTH coups,
            False sinon.
    """
    if not depth:
        return False

    # Parcourir tous les moves legaux
    for move in board.legal_moves:
        board.push(move)
        if board.is_checkmate():
            board.pop()
            return True

        # Appel récursif pour explorer les mouvements suivants
        if not mate_exists(board, depth - 1):
            board.pop()
        else:
            board.pop()
            return True
    return False  # Aucun mate n'a été trouvé

def get_last_pos(pgn_file):
    # genere moi la docstring en francais au format google
    """
    Lit le fichier .pgn et retourne l'échiquier de la dernière position.

    Args:
        pgn_file (str): Chemin vers le fichier .pgn.

    Returns:
        chess.Board: Instance de chess.Board représentant la dernière position.
    """
    with open(pgn_file, encoding='utf-8') as pgn:
        game = chess.pgn.read_game(pgn)
        if not game:
            print("unreadable game")
            return None
        last_pos = game.end()
    print(last_pos.board())
    return last_pos.board()

# Obtenir l'échiquier de la dernière position
chess_board = get_last_pos(PGN_FILE)

if chess_board:
    print("Calcul en cours")
    if mate_exists(chess_board):
        print("Un échec et mat est possible en moins de 5 coups.")
    else:
        print("Pas d'échec et mat en moins de 5 coups.")
else:
    print("Impossible de lire la dernière position du fichier .pgn.")
