from django.db import models


class Patient(models.Model):
    full_name = models.CharField(max_length=255)
    diagnose = models.TextField()


class Department(models.Model):
    name_of_department = models.CharField(max_length=255)

    def __str__(self):
        return self.name_of_department


class Staff(models.Model):
    full_name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name


class Main_Doctor(models.Model):
    full_name = models.CharField(max_length=255)
    experience = models.PositiveIntegerField()
    age = models.PositiveIntegerField()
    department = models.ManyToManyField(Department)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name


class Hospital(models.Model):
    code_of_hospital = models.PositiveIntegerField(unique=True)
    main_doctor = models.OneToOneField(Main_Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.code_of_hospital)