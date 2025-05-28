from django.shortcuts import render 
from django.http import JsonResponse
from stockfish import Stockfish

# Use the full absolute path to stockfish.exe
STOCKFISH_PATH = r"C:\Users\hp\ChessGame\chess_backend\stockfish\stockfish.exe"

# Initialize the engine
stockfish = Stockfish(path=STOCKFISH_PATH, depth=15)

def get_best_move(request):
    fen = request.GET.get('fen')
    if not fen:
        return JsonResponse({'error': 'FEN not provided'}, status=400)
    
    stockfish.set_fen_position(fen)
    best_move = stockfish.get_best_move()

    return JsonResponse({'best_move': best_move})
