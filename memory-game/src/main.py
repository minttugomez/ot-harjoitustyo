from memorygame import MemoryGame
from ui import UI

def main():
    cards = list(range(1, 37))
    memorygame = MemoryGame(cards)
    ui = UI(memorygame)

    ui.start()

if __name__ == "__main__":
    main()
