

class Config:
    image_path = 'images'
    
    speed_move = 10
    GAME_NAME = 'เก็บแยกขยะ'
    SCREEN_W = 800 # ความกว้าง แกน x
    SCREEN_H = 600 # ความสูง แกน y
    FPS = 30

    delay_button_drop_item = 300

    def color(name, red = 0, green = 0, blue = 0):
        if name == "red":
            return (255, 0, 0)
        elif name == "green":
            return (0, 255, 0)
        elif name == "white":
            return (255, 255, 255)
        elif name == "blue":
            return (0, 0, 255)
        elif name == "cyan":
            return (0, 255, 255)
        elif name == "black":
            return (0, 0, 0)
        else:
            return (red, green, blue)