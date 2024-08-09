from django.db import models

class Bank(models.Model):
    name = models.CharField(max_length=100)
    branch_code = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Deposit(models.Model):
    date = models.DateField()
    account_number = models.CharField(max_length=20)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=[
        ('completed', 'Tamamlandı'), 
        ('pending', 'Beklemede')
    ])

    def __str__(self):
        return f"Deposit by {self.customer} - {self.amount} TL on {self.date}"

class Withdrawal(models.Model):
    date = models.DateField()
    account_number = models.CharField(max_length=20)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True) 
    status = models.CharField(max_length=20, choices=[
        ('completed', 'Tamamlandı'), 
        ('pending', 'Beklemede')
    ])

    def __str__(self):
        return f"Withdrawal by {self.customer} - {self.amount} TL on {self.date}"

class Transfer(models.Model):
    date = models.DateField()
    sender_account = models.ForeignKey(Customer, related_name='transfers_sent', on_delete=models.CASCADE)
    receiver_account = models.ForeignKey(Customer, related_name='transfers_received', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True) 
    status = models.CharField(max_length=20, choices=[
        ('completed', 'Tamamlandı'), 
        ('pending', 'Beklemede')
    ])

    def __str__(self):
        return f"Transfer from {self.sender_account} to {self.receiver_account} - {self.amount} TL on {self.date}"

class Collection(models.Model):
    date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=20)
    amount_collected = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=[
        ('completed', 'Tamamlandı'), 
        ('pending', 'Beklemede')
    ])

    def __str__(self):
        return f"Collection from {self.customer} - {self.amount_collected} TL on {self.date}"
