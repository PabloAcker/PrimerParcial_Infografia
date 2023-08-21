import arcade

# Definición de constantes
PLAYER_SPEED = 5

class Frog(arcade.Sprite):
    def __init__(self, image: str, x, y):
        super().__init__(image, 1)
        self.center_x = x
        self.center_y = y
        self.speed = 0

    def update(self):
        # Control de movimiento de la rana
        self.center_x += self.speed
        self.center_y += self.speed

class Obstacle(arcade.Sprite):
    def __init__(self, image, x, y):
        super().__init__(image, 1)
        self.center_x = x
        self.center_y = y

class FroggerGame:
    def __init__(self):
        self.player = None
        self.obstacles = None

    def setup(self):
        self.player = Frog("imagenes/frog2.png", 400, 50)
        self.obstacles = arcade.SpriteList()
        # Crear obstáculos y agregarlos a la lista
        for i in range(5):
            obstacle = Obstacle("imagenes/auto.png", i * 150 + 75, 100)
            self.obstacles.append(obstacle)

    def update(self, delta_time):
        self.player.update()
        # Actualizar los obstáculos
        self.obstacles.update()

    def draw(self):
        self.player.draw()
        self.obstacles.draw()

    def on_key_press(self, symbol, modifiers):
        if symbol in (arcade.key.UP, arcade.key.RIGHT):
            self.player.speed = PLAYER_SPEED
        if symbol in (arcade.key.DOWN, arcade.key.LEFT):
            self.player.speed = -PLAYER_SPEED

    def on_key_release(self, symbol, modifiers):
        if symbol in (arcade.key.UP, arcade.key.DOWN, arcade.key.LEFT, arcade.key.RIGHT):
            self.player.speed = 0
