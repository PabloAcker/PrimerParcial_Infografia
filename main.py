import arcade
from frogger_game import FroggerGame

# Definición de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Frogger Game"
SPEED = 1

class App(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.LIGHT_GREEN)

    def on_draw(self):
        arcade.start_render()
        self.frog.draw() #TODO poner a los enemigos pero ver si es con un for

    def on_update(self, delta_time: float):
        self.frog.update(delta_time) #TODO cambiar esta linea y ver la logica de deteccion de enemigos del tank

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol in (arcade.key.UP, arcade.key.DOWN, arcade.key.LEFT, arcade.key.RIGHT):
            self.frog.speed = SPEED

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol in (arcade.key.UP, arcade.key.DOWN, arcade.key.LEFT, arcade.key.RIGHT):
            self.frog.speed = 0

def main():
    app = FroggerGame()
    arcade.run()

if __name__ == "__main__":
    main()