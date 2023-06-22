from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.username
class CarOwner(models.Model):
    Car_owner_ID = models.AutoField(primary_key=True)
    national_ID = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    tel=models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class CarHirer(models.Model):
    hirer_ID = models.AutoField(primary_key=True)
    national_ID = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact_info = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
class Car(models.Model):
    car_ID = models.AutoField(primary_key=True)
    car_owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    car_hirer = models.ForeignKey(CarHirer, on_delete=models.SET_NULL, null=True, blank=True)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=20)
    license_plate = models.CharField(max_length=20)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='car_images', null=True, blank=True)

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"
    
class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name

class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"Booking ID: {self.booking_id}, Car: {self.car}, Customer: {self.customer}"

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    comments = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review ID: {self.review_id}, Car: {self.car}, Customer: {self.customer}"