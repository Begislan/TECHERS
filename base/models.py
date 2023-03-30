from importlib._common import _

from django.db import models
import datetime
YEAR_CHOICES = [(r,r) for r in range(1984, datetime.date.today().year+1)]


class Person(models.Model):
    universitate = models.ForeignKey('Universitate', on_delete=models.CASCADE, verbose_name="Университет")
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE, verbose_name="Факультет")
    department = models.ForeignKey('Department', on_delete=models.CASCADE, verbose_name="Кафедра")
    job_title = models.ForeignKey('Job', on_delete=models.SET_NULL, null=True, verbose_name="Должность")
    name = models.CharField(max_length=255, verbose_name="Имя")
    first_name = models.CharField(max_length=255, verbose_name="Фамилия")
    last_name = models.CharField(max_length=255, blank=True, verbose_name="Отечество")
    academic_year = models.ForeignKey('Academic_year', on_delete=models.SET_NULL, null=True, verbose_name="Учебный год")
    birthday = models.DateField(verbose_name="Дата рождение: ")
    all_job_positions = models.ForeignKey('All_job_positions', on_delete=models.SET_NULL, null=True,
                                          verbose_name="Все должности работы")
    academic_degree = models.ForeignKey('Academic_degree', on_delete=models.SET_NULL, null=True,
                                        verbose_name="Ученая степень")
    scientific_title = models.ForeignKey('Scientific_title', on_delete=models.SET_NULL, null=True,
                                         verbose_name="научное звание")
    doc_pdf = models.FileField(upload_to='pdf/')

    def __str__(self):
        return f"Имя: {self.name}, Фамилия: {self.first_name}"

    class Meta:
        verbose_name = 'Персонал'
        verbose_name_plural = 'Персонал'


class Universitate(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, help_text="Поля автоматически заполняется")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Университет'
        verbose_name_plural = 'Университет'


class Faculty(models.Model):
    universitate = models.ForeignKey(Universitate, on_delete=models.CASCADE, verbose_name="Университет")
    name = models.CharField(max_length=255, verbose_name="Название факултета")
    slug = models.SlugField(blank=True, help_text="Поля автоматически заполняется")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Факультет'
        verbose_name_plural = 'Факультет'


class Department(models.Model):
    faculti = models.ForeignKey(Faculty,on_delete=models.CASCADE, verbose_name="Факультет: ")
    name = models.CharField(max_length=255, verbose_name="Имя кафедры: ")
    slug = models.SlugField(blank=True, help_text="поля автоматически заполняется")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Кафедра'
        verbose_name_plural = 'Кафедра'


class Job(models.Model):
    name = models.CharField(max_length=255, verbose_name="должность: ")
    slug = models.SlugField(blank=True, help_text="Поля автоматически заполняется")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должность'


class All_job_positions(models.Model):
    job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True, verbose_name="Должность")
    year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    year2 = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    number_order = models.IntegerField(verbose_name="номерр приказа")

    def __str__(self):
        return f"должност:{self.job} С: {self.year} К: {self.year2} Приказ: {self.number_order}"

    class Meta:
        verbose_name = 'Год выступ и поступ'
        verbose_name_plural = 'Год выступ и поступ'


class Academic_year(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "учебный год"
        verbose_name_plural = 'учебный год'


class Academic_degree(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, help_text="Поля автоматически заполняется")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ученая степень'
        verbose_name_plural = 'Ученая степень'


class Scientific_title(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, help_text="Поля автоматически заполняется")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'научное звание'
        verbose_name_plural = 'научное звание'
