from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.user.username}'s Account"

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField()

    TRANSACTION_TYPES = [
        ('Income', 'Income'),
        ('Expense', 'Expense'),
        ('Transfer', 'Transfer')
    ]

    CATEGORY_CHOICES = [
        ('Transport', 'Transport'),
        ('Going out', 'Going Out'),
        ('Health', 'Health'),
        ('Groceries', 'Groceries'),
        ('Holiday', 'Holiday'),
        ('Children', 'Children'),
        ('Education', 'Education'),
        ('Gifts', 'Gifts'),
        ('Shopping', 'Shopping'),
        ('Sports', 'Sports'),
        ('Leisure', 'Leisure'),
        ('Savings', 'Savings'),
    ]

    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    transaction_type = models.CharField(max_length=30, choices=TRANSACTION_TYPES, blank=True, null=True)

    def __str__(self):
        return f"{self.amount} {self.get_category_display()} ({self.transaction_type}) - {self.timestamp}"

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, blank=True, null=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"{self.user.username}'s Budget"
