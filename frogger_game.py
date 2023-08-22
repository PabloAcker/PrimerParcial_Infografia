import arcade
import time

class Frog(arcade.Sprite):
    def __init__(self, image_paths, scale, initial_x, initial_y):
        super().__init__(image_paths[0], scale)
        self.center_x = initial_x
        self.center_y = initial_y  # Posición inicial en el medio inferior
        self.moving = False
        self.image_paths = image_paths
        self.current_image_index = 0

        self.collided = False
        self.collided_time = 0

        

        # Cargar las texturas de las imágenes
        self.textures = [arcade.load_texture(image_path) for image_path in self.image_paths]

    def change_image(self, index):
        self.set_texture(index)
        self.current_image_index = index

    def move_up(self):
        if not self.moving:
            self.center_y += self.height
            self.change_image(0)  # Cambiar a la imagen para mover hacia arriba
            self.moving = True

    def move_down(self):
        if not self.moving:
            self.center_y -= self.height
            self.change_image(1)  # Cambiar a la imagen para mover hacia abajo
            self.moving = True

    def move_left(self):
        if not self.moving:
            self.center_x -= self.width
            self.change_image(2)  # Cambiar a la imagen para mover hacia la izquierda
            self.moving = True

    def move_right(self):
        if not self.moving:
            self.center_x += self.width
            self.change_image(3)  # Cambiar a la imagen para mover hacia la derecha
            self.moving = True

    def stop_moving(self):
        self.moving = False

    def update(self):
        # Movimiento y límites de la ventana
        self.center_x = max(self.width // 2, min(arcade.get_window().width - self.width // 2, self.center_x + self.change_x))
        self.center_y = max(self.height // 2, min(arcade.get_window().height - self.height // 2, self.center_y + self.change_y))

        if self.collided and time.time() - self.collided_time >= 1:
            self.center_x = 400
            self.center_y = 30
            self.change_image(0)  # Cambiar a la imagen original (hacia arriba)
            self.collided = False
            self.collided_time = 0

class Enemy(arcade.Sprite):
    def __init__(self, image_path, scale, initial_x, initial_y, speed):
        super().__init__(image_path, scale)
        self.center_x = initial_x
        self.center_y = initial_y
        self.speed = speed  # Velocidad del enemigo

    def update(self):
        # Mueve al enemigo a la derecha y reinicia su posición cuando llega al borde derecho
        # Mueve al enemigo a la izquierda y reinicia su posición cuando llega al borde izquierdo
        self.center_x += self.speed
        if self.speed > 0 and self.center_x > arcade.get_window().width + self.width // 2:
            self.center_x = -self.width // 2
        elif self.speed < 0 and self.center_x < -self.width // 2:
            self.center_x = arcade.get_window().width + self.width // 2
