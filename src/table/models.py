from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='product/', null=True, blank=True)

    def __str__(self):
        return self.name


class ProdSpec(models.Model):
    name_spec = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    def __str__(self):
        return self.name_spec


class ProdSeria(models.Model):
    name_seria = models.CharField(max_length=100)
    total_result = models.CharField(max_length=50, default=0)
    prod_spec = models.ForeignKey('ProdSpec', on_delete=models.CASCADE)

    def __str__(self):
        return self.name_seria


class Equipment(models.Model):
    name_current_equipment = models.CharField(max_length=100, null=True)
    prod_spec = models.ForeignKey(
        'ProdSpec', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name_current_equipment


class ProdEquipment(models.Model):
    name_equip = models.ForeignKey('Equipment', on_delete=models.CASCADE)
    firm = models.CharField(max_length=100, null=True)
    types = models.CharField(max_length=100)
    characteristics = models.TextField()
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='equipment/', null=True, blank=True)

    def __str__(self):
        return str(self.name_equip)


class Solution(models.Model):
    name_of_solution = models.CharField(max_length=100)
    prod_ser_sol = models.ForeignKey(
        'ProdSeria', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name_of_solution


class ProdSolutions(models.Model):
    target = models.CharField(max_length=150, null=True)
    solution_seria = models.CharField(max_length=150)
    quantity = models.IntegerField()
    solution = models.ForeignKey(
        'Solution', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.solution)


class Cultivation(models.Model):
    name_of_cultivation = models.CharField(max_length=100)
    prod_ser_cult = models.ForeignKey(
        'ProdSeria', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name_of_cultivation


class ProdCultivations(models.Model):
    date = models.DateField(blank=True, null=True)
    concentration_up_to = models.FloatField(blank=True, null=True)
    concentration_after = models.FloatField(blank=True, null=True)
    viability_up_to = models.FloatField(blank=True, null=True)
    viability_after = models.FloatField(blank=True, null=True)
    ph = models.FloatField(blank=True, null=True)
    glucose = models.FloatField(blank=True, null=True)
    lactose = models.FloatField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    cultivation = models.ForeignKey(
        'Cultivation', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.cultivation)
