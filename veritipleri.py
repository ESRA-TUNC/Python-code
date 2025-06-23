{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "dc48634d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "veri tipi = <class 'int'>\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "veri tipleri\n",
    "\n",
    "'''\n",
    "a = 45\n",
    "veritipi = type(a)\n",
    "print(\"veri tipi =\",veritipi)  #integer\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "5a392e05",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "veri tipi = <class 'float'>\n"
     ]
    }
   ],
   "source": [
    "a = 45.5\n",
    "veritipi = type(a)\n",
    "print(\"veri tipi =\",veritipi)  #float"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "bc9ed548",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "veri tipi = <class 'str'>\n"
     ]
    }
   ],
   "source": [
    "a = 'ezgi'\n",
    "veritipi = type(a)\n",
    "print(\"veri tipi =\",veritipi)  #string\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "851b9906",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "veri tipi = <class 'float'>\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "veri tiplerini dönüştürme işlemi\n",
    "\n",
    "'''\n",
    "\n",
    "a = 45\n",
    "a = float(a)\n",
    "veritipi = type(a)            # integer veri tipini float'a dönüştürdük.\n",
    "print(\"veri tipi =\",veritipi) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "1d460150",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "veri tipi = <class 'int'>\n"
     ]
    }
   ],
   "source": [
    "a = 45.5\n",
    "a = int(a)\n",
    "veritipi = type(a)            # float veri tipini integer'a dönüştürdük.\n",
    "print(\"veri tipi =\",veritipi) \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b7efa365",
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
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
