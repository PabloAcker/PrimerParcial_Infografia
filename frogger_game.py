import arcade

# Definición de constantes
PLAYER_SPEED = 5

class Frog(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__("frog.png")
        self.center_x = x
        self.center_y = y

    def update(self):
        # Control de movimiento de la rana
        if arcade.key.LEFT in arcade.get_keys():
            self.center_x -= PLAYER_SPEED
        if arcade.key.RIGHT in arcade.get_keys():
            self.center_x += PLAYER_SPEED
        if arcade.key.UP in arcade.get_keys():
            self.center_y += PLAYER_SPEED
        if arcade.key.DOWN in arcade.get_keys():
            self.center_y -= PLAYER_SPEED

class Obstacle(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__("car.png")
        self.center_x = x
        self.center_y = y

def setup_obstacles():
    obstacles = arcade.SpriteList()
    # Crear obstáculos y agregarlos a la lista
    for i in range(5):
        obstacle = Obstacle(i * 150 + 75, 100)
        obstacles.append(obstacle)
    return obstacles

class FroggerGame:
    def __init__(self):
        self.player = None
        self.obstacles = None

    def setup(self):
        self.player = Frog(400, 50)
        self.obstacles = setup_obstacles()

    def update(self, delta_time):
        self.player.update()
        # Actualizar los obstáculos
        self.obstacles.update()

    def draw(self):
        self.player.draw()
        self.obstacles.draw()

    def on_key_press(self, symbol, modifiers):
        pass

    def on_key_release(self, symbol, modifiers):
        pass
