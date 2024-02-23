
class Background_object:

    def __init__(self, x, y, width, height, color):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__color = color


    def Get_x(self):
        return self.__x
    
    def Get_y(self):
        return self.__y
    
    def Get_color(self):
        return self.__color
    
    def Get_width(self):
        return self.__width
    
    def Get_height(self):
        return self.__height


    def Set_x(self, value):
        self.__x = value

    def Set_y(self, value):
        self.__y = value


All_bakcground_objects = [
    Background_object(0, 0, 800, 800, "purple"),
    Background_object(0, -800, 800, 800, "green"),
    Background_object(800, 0, 800, 800, "yellow"),
    Background_object(0, 800, 800, 800, "blue"),
    Background_object(-800, 0, 800, 800, "orange"),
    Background_object(-800, -800, 800, 800, "silver"),
    Background_object(-800, 800, 800, 800, "pink"),
    Background_object(800, 800, 800, 800, "grey"),
    Background_object(800, -800, 800, 800, "gold")    
]

#TODO: przerobić
