import arcade
from frogger_game import FroggerGame

# Definición de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Frogger Game"
SPEED = 5

class App(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.LIGHT_GREEN)
        self.game = FroggerGame()
        self.game.setup()

    def on_draw(self):
        arcade.start_render()
        self.game.draw()

    def on_update(self, delta_time: float):
        self.game.update(delta_time)

    def on_key_press(self, symbol: int, modifiers: int):
        self.game.on_key_press(symbol, modifiers)

    def on_key_release(self, symbol: int, modifiers: int):
        self.game.on_key_release(symbol, modifiers)

def main():
    app = App()
    arcade.run()

if __name__ == "__main__":
    main()