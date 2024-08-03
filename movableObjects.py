{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "34ceb8c4-cf00-49b2-ae29-3421e9a42aba",
   "metadata": {},
   "outputs": [],
   "source": [
    "#import numpy as np\n",
    "from abc import ABC, abstractmethod, abstractproperty\n",
    "#import abс\n",
    "\n",
    "class Moving(ABC):\n",
    "\n",
    "    @abstractmethod\n",
    "    def move(): pass\n",
    "    \n",
    "    @abstractproperty\n",
    "    def Velocity(): pass\n",
    "\n",
    "class Rotate(ABC):\n",
    "\n",
    "    @abstractmethod\n",
    "    def rotate(): pass\n",
    "\n",
    "    @abstractproperty\n",
    "    def angVelocity(): pass\n",
    "    \n",
    "\n",
    "class Movable_obj(Moving): \n",
    "    def __init__(self, x, y, vx, vy):\n",
    "# Устанавливаем начальные координаты и значения мгновенных скоростей        \n",
    "        self.__x = x\n",
    "        self.__y = y\n",
    "        self.__vx = vx\n",
    "        self.__vy = vy\n",
    "    \n",
    "    def get_location(self):\n",
    "        if self.__x is None or self.__y is None:\n",
    "            raise ValueError(\"Cannot read position\")\n",
    "        return (self.__x, self.__y)\n",
    "\n",
    "    def set_location(self, x, y):\n",
    "        if self.__x is None or self.__y is None:\n",
    "            raise ValueError(\"Cannot set position\")\n",
    "        self.__x = x\n",
    "        self.__y = y\n",
    "        \n",
    "    def move(self):\n",
    "        if self.__x is None or self.__y is None:\n",
    "            raise ValueError(\"Cannot read position\")\n",
    "        if self.__vx is None or self.__vy is None:\n",
    "            raise ValueError(\"Cannot read velocity\")\n",
    "        new_x = self.__x + self.__vx\n",
    "        new_y = self.__y + self.__vy\n",
    "        self.set_location(new_x, new_y)\n",
    "\n",
    "    @property\n",
    "    def Velocity(self):\n",
    "        return (self.__vx, self.__vy)\n",
    "    \n",
    "    @Velocity.setter\n",
    "    def Velocity(self, new_velocity):\n",
    "        if self.__vx is None or self.__vy is None:\n",
    "            raise ValueError(\"Cannot read velocity\")\n",
    "        self.__vx = new_velocity[0]\n",
    "        self.__vy = new_velocity[1]\n",
    "\n",
    "class Rotatable_obj(Rotate):\n",
    "    def __init__(self, alfa, angVelocity):\n",
    "# Устанавливаем начальные значения угла и угловой скорости\n",
    "        self.__alfa = alfa\n",
    "        self.__angVelocity = angVelocity\n",
    "\n",
    "    def get_angle(self):\n",
    "        return self.__alfa\n",
    "\n",
    "    def set_angle(self, new_alfa):\n",
    "        if self.__alfa is None:\n",
    "            raise ValueError(\"Cannot read angle\")\n",
    "        self.__alfa = new_alfa\n",
    "\n",
    "    def rotate(self):\n",
    "        if self.__alfa is None or self.__angVelocity is None:\n",
    "            raise ValueError(\"Cannot read angle or angular velocity\")\n",
    "        new_alfa = self.__alfa + self.__angVelocity\n",
    "        self.set_angle(new_alfa)\n",
    "\n",
    "    @property\n",
    "    def angVelocity(self):\n",
    "        return self.__angVelocity\n",
    "\n",
    "    @angVelocity.setter\n",
    "    def angVelocity(self, new_angVelocity):\n",
    "        if self.__angVelocity is None:\n",
    "            raise ValueError(\"Cannot read set angular velocity\")\n",
    "        self.__angVelocity = new_angVelocity\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "0fbf765c-2784-4513-b76f-0572845d50af",
   "metadata": {},
   "outputs": [],
   "source": [
    "spcship = Movable_obj(12, 5, -7, 3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "d0d77c47-6f09-4dc5-91e3-dcddc7b2dd16",
   "metadata": {},
   "outputs": [],
   "source": [
    "spcship.move()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "2ac1433b-0dcb-4499-9544-dfeeb35e9e7c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(8, 18)"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "spcship.get_location()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "b8e29bc5-d172-4e54-b721-bb6f1bdd20b7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(3, 10)\n"
     ]
    }
   ],
   "source": [
    "print(spcship.Velocity)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "f80e8fd3-425a-4919-a230-46de682164ab",
   "metadata": {},
   "outputs": [],
   "source": [
    "spcship.Velocity = [3, 10]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "49cb6708-0120-4995-9899-caed8b5705ef",
   "metadata": {},
   "outputs": [],
   "source": [
    "r_obj = Rotatable_obj(3, 12)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "141425aa-3a2e-4a5a-b1b3-f9240973feea",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "20"
      ]
     },
     "execution_count": 93,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "r_obj.get_angle()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "a3c2f54b-4765-47a5-b7cd-57ac809c9cb0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "r_obj.angVelocity"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "ee842d22-e67e-40c9-bd6b-5d9a3b73b41d",
   "metadata": {},
   "outputs": [],
   "source": [
    "r_obj.rotate()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "d55b77c6-b3ad-493a-a7ad-dafc7f73a0b2",
   "metadata": {},
   "outputs": [],
   "source": [
    "r_obj.angVelocity = 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3499b8d0-db7f-4d2f-9bfd-1155df2a5dc1",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
