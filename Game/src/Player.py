from utils.Screen_info import Screen_width, Screen_height

class Player:
    def __init__(self):
        self.speed = 200
        self.x = Screen_width / 2
        self.y = Screen_height / 2
    
    def Get_speed(self):
        return self.speed
    
    def Get_x(self):
        return self.x
    
    def Get_y(self):
        return self.y
    

    def Set_speed(self, value):
        self.speed = value

    def Set_x(self, value):
        self.x = value

    def Set_y(self, value):
        self.y = value