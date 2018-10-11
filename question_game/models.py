from __future__ import unicode_literals
from django.utils.timezone import now
from django.db import models


class Game(models.Model):

	game_name = models.CharField(max_length=100, unique=True)
	pub_date = models.DateTimeField('date published', default=now())
	image = models.ImageField(upload_to="gallery", default="default.jpg")

	def __str__(self):
		return self.game_name

class Question( models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published', default=now())
	game = models.ForeignKey(Game, on_delete=models.CASCADE)
	correct_answer = models.CharField(max_length=200)
	needs_image = models.BooleanField(default=False)
	image = models.ImageField(upload_to="gallery", default="default.jpg")

	def __str__(self):
		return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text


class Team( models.Model):
	name = models.CharField(max_length=50, unique=True)
	ip= models.CharField(max_length=50)


	def __str__(self):
		return self.name

	

class Answer( models.Model):
	team = models.ForeignKey(Team, on_delete=models.CASCADE)
	question = models.ForeignKey(Question, on_delete=models.CASCADE )
	choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
	pub_date = models.DateTimeField('date published', default=now()) 

	def __str__(self):
		return '%s - %s - %s' % (str(self.team), str(self.question), str(self.choice))

class Question_game(Game):
	time = models.IntegerField();
	
class Memorama(Game):
	num_of_pairs = models.IntegerField()




'''Tipos de juego


Laberinto : yo

Se muestran un camino con varias opciones, en centro de la pantalla (piso) debe haber una pregunta
en cada camino debe haber una respuesta y dos distractores, se gana cuando se contesta cierto numero 
de preguntas correctas

Sonido de error: Charlie , los LCC

Se despliega genera un sonido, los estudiantes deben decir a que se debe el sonido

-fallas en la ram
-procesador desconectado 
-etc

Memorama: Charlie

memorama normal, en lugar de poner un par de imagenes
en una se pone la definicion y en otra se pone 

globo callendo


se hace una pregunta y en lugar de tiempo se muestra un globo callendo, si el estudiante contesta correctamente
el globo sube, el objetivo es contestar todas las preguntas antes de que el globo toque el piso,
si toca el piso el globo explota y el pinguino muere

Patilio (Pokemon): samuel

igual a pokemon, solo hay un cambio en lugar de ataques, son preguntas, si se falla la pregunta pierdes vida, si no
el enemigo pierde vida

Relacionar fotos con definiciones: Charlie

Hay un grupo de fotos en una columna, en la otra columna estan las definiciones, la idea es colocarlas juntas

Fotos con errores y pasos para resolverlos:

se muestra una/s foto/s de algun problema en una computadora y 

Diagrama esquematico con varias posibilidades de repararse

Contar cable de una fuente de poder 

mario bros

mario bros'

Reporte



'''

	

		

