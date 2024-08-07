#import numpy as np
from abc import ABC, abstractmethod, abstractproperty
#import abс

class Moving(ABC):

    @abstractmethod
    def move(): pass
    
    @abstractproperty
    def Velocity(): pass

class Rotate(ABC):

    @abstractmethod
    def rotate(): pass

    @abstractproperty
    def angVelocity(): pass
    

class Movable_obj(Moving): 
    def __init__(self, x, y, vx, vy):
# Устанавливаем начальные координаты и значения мгновенных скоростей        
        self.__x = x
        self.__y = y
        self.__vx = vx
        self.__vy = vy
    
    def get_location(self):
        if self.__x is None or self.__y is None:
            raise ValueError("Cannot read position")
        return (self.__x, self.__y)

    def set_location(self, x, y):
        if self.__x is None or self.__y is None:
            raise ValueError("Cannot set position")
        self.__x = x
        self.__y = y
        
    def move(self):
        if self.__x is None or self.__y is None:
            raise ValueError("Cannot read position")
        if self.__vx is None or self.__vy is None:
            raise ValueError("Cannot read velocity")
        new_x = self.__x + self.__vx
        new_y = self.__y + self.__vy
        self.set_location(new_x, new_y)

    @property
    def Velocity(self):
        return (self.__vx, self.__vy)
    
    @Velocity.setter
    def Velocity(self, new_velocity):
        if self.__vx is None or self.__vy is None:
            raise ValueError("Cannot read velocity")
        self.__vx = new_velocity[0]
        self.__vy = new_velocity[1]

class Rotatable_obj(Rotate):
    def __init__(self, alfa, angVelocity):
# Устанавливаем начальные значения угла и угловой скорости
        self.__alfa = alfa
        self.__angVelocity = angVelocity

    def get_angle(self):
        return self.__alfa

    def set_angle(self, new_alfa):
        if self.__alfa is None:
            raise ValueError("Cannot read angle")
        self.__alfa = new_alfa

    def rotate(self):
        if self.__alfa is None or self.__angVelocity is None:
            raise ValueError("Cannot read angle or angular velocity")
        new_alfa = self.__alfa + self.__angVelocity
        self.set_angle(new_alfa)

    @property
    def angVelocity(self):
        return self.__angVelocity

    @angVelocity.setter
    def angVelocity(self, new_angVelocity):
        if self.__angVelocity is None:
            raise ValueError("Cannot read set angular velocity")
        self.__angVelocity = new_angVelocity

class Rotatable_adapter(Rotate):
    def __init__(self, rotatable_obj):
        r_obj = rotatable_obj

    def get_angle(self):
        return self.r_obj.get_angle()

    def set_angle(self, new_alfa):
        return self.r_obj.set_angle(new_alfa)

    def rotate(self):
        return self.r_obj.rotate()

