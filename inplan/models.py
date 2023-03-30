from django.db import models


class Works(models.Model):
    name = models.CharField(max_length=255, verbose_name="Жумуштун түрү: ")
    slug = models.SlugField(blank=True)


class Completion(models.Model):
    name = models.CharField(max_length=255, verbose_name="Аткарылгандыгы жонүнду белги: ")

    def __str__(self):
        return self.name


class Study_methods(models.Model):
    work = models.ForeignKey(Works, on_delete=models.CASCADE)
    scope_of_work = models.IntegerField(verbose_name="Жумуштун көлөмү 1-жарым жылдык: ")
    completion = models.ForeignKey(Completion, on_delete=models.SET_NULL, null=True,
                                           verbose_name="Аткарылгандыгы жөнүндө белги 1-жарым жылдык ")
    cause = models.TextField(verbose_name="Аткарылбаса себеби көрсөтүлсүн: ")
    scope_of_work2 = models.IntegerField(verbose_name="Жумуштун көлөмү 2- жарым жылдык: ")
    completion2 = models.ForeignKey(Completion, on_delete=models.SET_NULL, null=True,
                                              verbose_name="Аткарылгандыгы жөнүндө белги 2-жарым жылдык")
    cause2 = models.TextField(verbose_name="Аткарылбаса себеби көрсөтүлсүн: ")


class Organization_of_students_independent_work(models.Model):
    pass
    # work = models.ForeignKey(Works, on_delete=models.CASCADE)
    # scope_of_work = models.IntegerField(verbose_name="Жумуштун көлөмү 1-жарым жылдык: ")
    # sign_of_completion = models.ForeignKey(Sign_of_completion, on_delete=models.SET_NULL, null=True,
    #                                        verbose_name="Аткарылгандыгы жөнүндө белги 1-жарым жылдык ")
    # cause = models.TextField(verbose_name="Аткарылбаса себеби көрсөтүлсүн: ")
    # scope_of_work2 = models.IntegerField(verbose_name="Жумуштун көлөмү 2- жарым жылдык: ")
    # sign_of_completion2 = models.ForeignKey(Sign_of_completion, on_delete=models.SET_NULL, null=True,
    #                                         verbose_name="Аткарылгандыгы жөнүндө белги 2-жарым жылдык")
    # cause2 = models.TextField(verbose_name="Аткарылбаса себеби көрсөтүлсүн: ")
