# from django.db import models

# class Result(models.Model):
#     roll_no = models.CharField(max_length=10, unique=True)
#     linear_algebra = models.CharField(max_length=2)
#     oop_theory = models.CharField(max_length=2)
#     oop_practical = models.CharField(max_length=2)
#     pakistan_studies = models.CharField(max_length=2)
#     islamic_studies = models.CharField(max_length=2)
#     digital_logic_theory = models.CharField(max_length=2)
#     digital_logic_practical = models.CharField(max_length=2)
#     communication_skills = models.CharField(max_length=2)
    
#     def __str__(self):
#         return self.roll_no    




from django.db import models

# Semester 2 Results Model
class Result(models.Model):
    roll_no = models.CharField(max_length=10, unique=True)
    linear_algebra = models.CharField(max_length=2)
    oop_theory = models.CharField(max_length=2)
    oop_practical = models.CharField(max_length=2)
    pakistan_studies = models.CharField(max_length=2)
    islamic_studies = models.CharField(max_length=2)
    digital_logic_theory = models.CharField(max_length=2)
    digital_logic_practical = models.CharField(max_length=2)
    communication_skills = models.CharField(max_length=2)

    def __str__(self):
        return self.roll_no


# Semester 1 Results Model
class Result1(models.Model):
    roll_no = models.CharField(max_length=10, unique=True)
    applied_physics_theory = models.CharField(max_length=2)
    applied_physics_practical = models.CharField(max_length=2)
    calculus_and_analytical_geometry = models.CharField(max_length=2)
    functional_english = models.CharField(max_length=2)
    intro_to_info_and_comm_techns_theory = models.CharField(max_length=2)
    intro_to_info_and_comm_techns_practical = models.CharField(max_length=2)
    programming_fundamentals_theory = models.CharField(max_length=2)
    programming_fundamentals_practical = models.CharField(max_length=2)

    def __str__(self):
        return self.roll_no
