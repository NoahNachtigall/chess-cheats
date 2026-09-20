import chess
import chess.engine

# Configuration (CHANGE THIS TO YOUR ACTUAL STOCKFISH PATH)
STOCKFISH_PATH = r"C:\Users\noah\Downloads\stockfish-windows-x86-64-universal\stockfish\stockfish-windows-x86-64-universal.exe"


def main():
    
    board = chess.Board()
    
    try:
        engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)
        print(":) Stockfish connected successfully!")
    except Exception as e:
        print(f":( Error loading Stockfish. Check your path. Details: {e}")
        return

    print("\n--- Chess Cheat Terminal Started ---")
    print("Moves must be entered in UCI format (e.g., e2e4, g1f3).")
    print("Type 'quit' to exit.\n")

    
    color_input = input("Are you playing as White or Black? (w/b): ").strip().lower()
    user_is_white = color_input == 'w'

    
    while not board.is_game_over():
        
        if board.turn == user_is_white:
            print("\nCalculating best move...")
            
            result = engine.play(board, chess.engine.Limit(time=1.0))
            print(f"RECOMMENDED MOVE: {result.move}")
            
            
            board.push(result.move)
        else:
            
            opp_move_str = input("\nEnter opponent's move: ").strip()
            
            if opp_move_str.lower() == 'quit':
                break
                
            try:
                opp_move = chess.Move.from_uci(opp_move_str)
                if opp_move in board.legal_moves:
                    board.push(opp_move)
                else:
                    print("[X] Illegal move for this position! Try again.")
            except ValueError:
                print("[X] Invalid format. Use UCI format like 'e2e4'.")

    
    print("\nGame Over. Result: ", board.result())
    engine.quit()

if __name__ == "__main__":
    main()
