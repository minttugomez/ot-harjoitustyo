from memorygame import MemoryGame
from ui import UI

def main():
    cards = list(range(1, 37)) # create 36 cards with a different number on them
    memorygame = MemoryGame(cards)
    ui = UI(memorygame)

    ui.start()

if __name__ == "__main__":
    main()
