from django.db import models


class CreditCard(models.Model):
    card = models.CharField(max_length=200)
    flag = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.card


class Category(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class BillCard(models.Model):
    cred_card= models.ForeignKey(CreditCard,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,)
    category= models.ForeignKey(Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,)
    place = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    value = models.DecimalField(max_digits=6, decimal_places=2)
    sale_date = models.DateTimeField(auto_now_add=True)
    is_recurrent = models.BooleanField(default=False)
    parcel = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.place} - R$: {self.value}" 

class Bill(models.Model):
    category= models.ForeignKey(Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,)
    place = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    value = models.DecimalField(max_digits=6, decimal_places=2)
    sale_date = models.DateTimeField(auto_now_add=True)
    is_recurrent = models.BooleanField(default=False)
    parcel = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.place} - R$: {self.value}" 


class Income(models.Model):
    category= models.ForeignKey(Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,)
    value = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True)
    sale_date = models.DateTimeField(auto_now_add=True)
    is_recurrent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.category} - R$: {self.value}" 