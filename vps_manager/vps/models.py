from django.db import models

class VPS(models.Model):
	STATUS_CHOICES = [
		("Start", "Запущено"),
		("Block", "Завершено"),
		("Stop", "Остановлено"),
	]
	
	uid = models.UUIDField(unique=True, primary_key=True)
	cpu = models.PositiveSmallIntegerField(
		verbose_name="Кол-во ядер процессора",
	)
	ram = models.PositiveSmallIntegerField(
		verbose_name="Размер ОЗУ",
	)
	hdd = models.PositiveSmallIntegerField(
		verbose_name="Размер хранилища",
	)
	status = models.CharField(
	verbose_name="Статус сервера", 
	choices=STATUS_CHOICES,
	max_length=10
	)
	
	def __str__(self):
		return f"VPS {self.uid} ({self.status})"
