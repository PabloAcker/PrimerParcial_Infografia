import arcade
from frogger_game import FroggerGame

# Definición de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Frogger Game"

def main():
    game = FroggerGame()
    game.setup()

    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    @window.event
    def on_draw():
        arcade.start_render()
        game.draw()

    @window.event
    def update(delta_time):
        game.update(delta_time)

    @window.event
    def on_key_press(symbol, modifiers):
        game.on_key_press(symbol, modifiers)

    @window.event
    def on_key_release(symbol, modifiers):
        game.on_key_release(symbol, modifiers)

    arcade.run()

if __name__ == "__main__":
    main()