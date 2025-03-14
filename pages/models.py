from django.db import models
import uuid

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()

class Jobs(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    benefits  = models.TextField()
    requirements = models.TextField()
    date = models.DateField(auto_created=True)
    locations = models.CharField(max_length=200)
    skills = models.CharField(max_length=100)

class Applicant(models.Model):
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=10)
    resume = models.FileField(upload_to='resumes/')
    portfolio = models.CharField(max_length=300, blank=True)
    coverletter = models.TextField()

class Events(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
    eventdate = models.DateField()
    cost = models.IntegerField()
    image = models.FileField(blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Ticket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    purchaseDate = models.DateField(auto_now_add=True)
    email = models.EmailField()

    def __str__(self): 
        return f"Ticket {self.id} - {self.email}"

class Invoice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tickets = models.ManyToManyField(Ticket, blank=True)
    email = models.EmailField(max_length=254)
    cost = models.IntegerField()
    event = models.TextField()
    verified = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=200)
    payment_intent_id = models.CharField(max_length=400)
    last_name = models.CharField(max_length=200)
    sent = models.BooleanField(default=False)
    numTickets = models.IntegerField()

    def __str__(self):
        return f"Invoice {self.id} - {self.email}"

    