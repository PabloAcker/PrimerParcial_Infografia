import arcade
import time
from frogger_game import Frog, Enemy

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 750
SCREEN_TITLE = "Frogger Game"

NUM_LIVES = 3

class FroggerGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.background = arcade.load_texture("imagenes/fondo.PNG")
        self.player_sprite = Frog(["imagenes/frog_arriba.png", "imagenes/frog_abajo.png", "imagenes/frog_izquierda.png", "imagenes/frog_derecha.png", "imagenes/frog_aplastada.png"], scale=0.11, initial_x=400, initial_y=30)

        self.lives = NUM_LIVES

        self.show_victory = False

        self.coin_collided_time = 0

        self.enemy_sprites = arcade.SpriteList()
        enemy_image_path = "imagenes/auto2.png"  
        enemy_image_path2 = "imagenes/auto.png"
        enemy_image_path3 = "imagenes/auto3.png"
        enemy_image_path4 = "imagenes/cocodrilo.png"
        enemy_image_path5 = "imagenes/tiburon.png"
        enemy_speed = 2  # velocidad del enemigo

        #autos
        enemy1 = Enemy(enemy_image_path, scale=0.2, initial_x=0, initial_y=180, speed=enemy_speed)
        enemy2 = Enemy(enemy_image_path2, scale=0.2, initial_x=800, initial_y=110, speed=-(enemy_speed-0.5))  # Movimiento hacia la izquierda
        enemy3 = Enemy(enemy_image_path3, scale=0.2, initial_x=800, initial_y=250, speed=-(enemy_speed+0.7))  # Movimiento hacia la izquierda
        enemy6 = Enemy(enemy_image_path, scale=0.2, initial_x=0, initial_y=330, speed=(enemy_speed+1.4))
        #enemigos del rio
        enemy4 = Enemy(enemy_image_path4, scale=0.015, initial_x=0, initial_y=475, speed=(enemy_speed+0.7))
        enemy5 = Enemy(enemy_image_path5, scale=0.20, initial_x=800, initial_y=530, speed=-(enemy_speed+1)) # Movimiento hacia la izquierda
        enemy7 = Enemy(enemy_image_path4, scale=0.015, initial_x=0, initial_y=580, speed=(enemy_speed+1.4))
        enemy8 = Enemy(enemy_image_path5, scale=0.20, initial_x=800, initial_y=640, speed=-(enemy_speed+2)) # Movimiento hacia la izquierda
        
        self.enemy_sprites.extend([enemy1, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7, enemy8])

        # Agregar monedas
        self.coin_sprites = arcade.SpriteList()
        coin_image_paths = ["imagenes/nenufar_win.png", "imagenes/nenufar_win.png", "imagenes/nenufar_win.png", "imagenes/nenufar_win.png"]
        coin_positions = [(95, 710), (310, 710), (510, 710), (700, 710)]

        for path, (x, y) in zip(coin_image_paths, coin_positions):
            coin = arcade.Sprite(path, scale=0.07, center_x=x, center_y=y)
            self.coin_sprites.append(coin)
        
        # Contador de monedas
        self.coin_count = 0

    def on_draw(self):
        arcade.start_render()
        # Dibuja el fondo de la imagen
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        if self.coin_count == 4:
            victory_image = arcade.load_texture("imagenes/win.png")
            arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 300, 300, victory_image)
        else:
            if self.lives > 0:
                # Dibuja al jugador (rana)
                self.player_sprite.draw()

                # Dibuja a los enemigos
                self.enemy_sprites.draw()

                # Dibuja las monedas
                self.coin_sprites.draw()

                # Dibuja el contador de vidas
                arcade.draw_text(f"VIDAS: {self.lives}", 10, 420, arcade.color.BLACK, 14)

                # Dibuja el contador de monedas
                arcade.draw_text(f"NENUFARES: {self.coin_count}", 10, 385, arcade.color.BLACK, 14)
            else:
                # Dibuja la imagen cuando las vidas llegan a cero
                game_over_image = arcade.load_texture("imagenes/game_over.png")
                arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 300, 300, game_over_image)

    def on_key_press(self, key, modifiers):
        if not self.player_sprite.collided and self.lives > 0:  # Verifica si la rana ha colisionado y que tenga vidas
        # Control de movimiento al presionar las teclas de flecha
            if key == arcade.key.UP:
                self.player_sprite.move_up()
            elif key == arcade.key.DOWN:
                self.player_sprite.move_down()
            elif key == arcade.key.LEFT:
                self.player_sprite.move_left()
            elif key == arcade.key.RIGHT:
                self.player_sprite.move_right()

    def on_key_release(self, key, modifiers):
        # Detiene el movimiento cuando se suelta la tecla
        self.player_sprite.stop_moving()

    def on_update(self, delta_time):
        self.player_sprite.update()
        self.enemy_sprites.update()

        if not self.player_sprite.collided:
            # Verificar colisiones entre la rana y los enemigos
            for enemy in self.enemy_sprites:
                if arcade.check_for_collision(self.player_sprite, enemy):
                    self.player_sprite.change_image(4)  # Cambiar a la imagen de colisión
                    self.player_sprite.collided = True
                    self.player_sprite.collided_time = time.time()
                    self.lives -= 1

                    # implementacion para que la rana desaparezca cuando llegue la vida a cero
                    #if self.lives <= 0:
                    #    self.player_sprite.remove_from_sprite_lists()

                    break  # Salir del bucle una vez que se encuentre una colisión

        # Restablecer la rana a las coordenadas de inicio si ha pasado el tiempo suficiente
        if self.player_sprite.collided and time.time() - self.player_sprite.collided_time >= 1:
            self.player_sprite.center_x = 400
            self.player_sprite.center_y = 30
            self.player_sprite.change_image(0)  # Cambiar a la imagen original (hacia arriba)
            self.player_sprite.collided = False

        # Restablecer la rana a las coordenadas de inicio después de tomar una moneda
        if self.coin_collided_time != 0 and time.time() - self.coin_collided_time >= 0.05:
            self.player_sprite.center_x = 400
            self.player_sprite.center_y = 30
            self.player_sprite.change_image(0)  # Cambiar a la imagen original (hacia arriba)
            self.coin_collided_time = 0

        # Restablecer el estado de la rana al volver a las coordenadas de inicio
        if not self.player_sprite.collided and self.player_sprite.center_x == 400 and self.player_sprite.center_y == 30:
            self.player_sprite.returned_to_start = True

        # Verificar colisiones entre la rana y las monedas
        coins_to_remove = []
        for coin in self.coin_sprites:
            if arcade.check_for_collision(self.player_sprite, coin):
                self.coin_count += 1
                coins_to_remove.append(coin)
                self.coin_collided_time = time.time()  # Actualiza el tiempo de colisión con la moneda

        for coin in coins_to_remove:
            coin.remove_from_sprite_lists()

        # Mostrar la imagen de victoria si se recogen todas las monedas
        if self.coin_count == 4:
            self.show_victory = True

def main():
    game = FroggerGame()
    arcade.run()

if __name__ == "__main__":
    main()