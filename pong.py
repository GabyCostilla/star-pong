import py5

# Variables globales
paddle1_y = paddle2_y = 0
paddle_width = paddle_height = 0
paddle_speed = ball_size = 0
ball_x = ball_y = ball_dx = ball_dy = 0
player1_score = player2_score = 0
paddle_accel1 = paddle_accel2 = 0  
paddle_max_speed = 10  

keys = set()

def setup():
    py5.size(800, 400)
    global paddle_width, paddle_height, paddle_speed, ball_size
    global ball_x, ball_y, ball_dx, ball_dy
    global paddle1_y, paddle2_y, player1_score, player2_score
    paddle_width = 20
    paddle_height = 100
    paddle_speed = 7
    ball_size = 20
    reset_game()

def reset_game():
    global ball_x, ball_y, ball_dx, ball_dy, paddle1_y, paddle2_y
    global player1_score, player2_score
    ball_x = py5.width / 2
    ball_y = py5.height / 2
    ball_dx = 5
    ball_dy = py5.random(-3, 3)  # Velocidad aleatoria en Y
    paddle1_y = py5.height / 2 - paddle_height / 2
    paddle2_y = py5.height / 2 - paddle_height / 2
    player1_score = 0
    player2_score = 0

def draw():
    global ball_x, ball_y, ball_dx, ball_dy, paddle1_y, paddle2_y
    global player1_score, player2_score, paddle_accel1, paddle_accel2

    py5.background(0)
    

    py5.rect(30, paddle1_y, paddle_width, paddle_height)  # Pala izquierda
    py5.rect(py5.width - 30 - paddle_width, paddle2_y, paddle_width, paddle_height)  # Pala derecha
    

    py5.ellipse(ball_x, ball_y, ball_size, ball_size)
    

    py5.text_size(32)
    py5.text_align(py5.CENTER)
    py5.fill(255)
    py5.text(f"{player1_score} - {player2_score}", py5.width / 2, 40)
    

    py5.text_size(16)
    py5.text_align(py5.LEFT)
    py5.fill(255)
    py5.text("Jugador 1: W (Arriba), S (Abajo)", 10, 30)
    py5.text_align(py5.RIGHT)
    py5.text("Jugador 2: O (Arriba), L (Abajo)", py5.width - 10, 30)
    

    ball_x += ball_dx
    ball_y += ball_dy
    
    # Rebote de la pelota en la parte superior e inferior
    if ball_y <= ball_size / 2 or ball_y >= py5.height - ball_size / 2:
        ball_dy *= -1
    
    # Verificar colisiones con los paddles
    if ball_x - ball_size / 2 <= 30 + paddle_width:
        if paddle1_y < ball_y < paddle1_y + paddle_height:
            hit_position = (ball_y - paddle1_y) / paddle_height  
            ball_dx = abs(ball_dx) * 1.05  # Incrementar velocidad
            ball_dy = (hit_position - 0.5) * 8  # Modificar ángulo
            ball_x = 30 + paddle_width + ball_size / 2

    if ball_x + ball_size / 2 >= py5.width - 30 - paddle_width:
        if paddle2_y < ball_y < paddle2_y + paddle_height:
            hit_position = (ball_y - paddle2_y) / paddle_height  
            ball_dx = -abs(ball_dx) * 1.05  # Incrementar velocidad
            ball_dy = (hit_position - 0.5) * 8  # Modificar ángulo
            ball_x = py5.width - 30 - paddle_width - ball_size / 2
    
    # Limitar la velocidad de la pelota
    ball_dx = py5.constrain(ball_dx, -12, 12)
    ball_dy = py5.constrain(ball_dy, -12, 12)
    
    
    if ball_x < 0:
        player2_score += 1
        reset_ball()
    

    if ball_x > py5.width:
        player1_score += 1
        reset_ball()


    if 'w' in keys:
        paddle_accel1 = -1
    elif 's' in keys:
        paddle_accel1 = 1
    else:
        paddle_accel1 = 0  

    if 'o' in keys:
        paddle_accel2 = -1
    elif 'l' in keys:
        paddle_accel2 = 1
    else:
        paddle_accel2 = 0  

    # Aplicar aceleración y fricción
    paddle1_y += paddle_speed * paddle_accel1
    paddle2_y += paddle_speed * paddle_accel2
    

    paddle1_y = py5.constrain(paddle1_y, 0, py5.height - paddle_height)
    paddle2_y = py5.constrain(paddle2_y, 0, py5.height - paddle_height)

def key_pressed():
    global keys
    keys.add(py5.key)

def key_released():
    global keys
    keys.discard(py5.key)

def reset_ball():
    global ball_x, ball_y, ball_dx, ball_dy
    ball_x = py5.width / 2
    ball_y = py5.height / 2
    ball_dx = py5.random(-5, 5)
    ball_dy = py5.random(-3, 3)

if __name__ == "__main__":
    py5.run_sketch()

#supuestamente aceleran y desaceleran debido a su inercia
#cuanto mas al centro pegue la pelota mas recto ira el tiro