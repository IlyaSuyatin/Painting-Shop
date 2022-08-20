from django.db import models
from django.forms import CharField
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Painting(models.Model):
    SIZES = (
        ("8x10", "8x10"),
        ("10x12", "10x12"),
        ("11x14", "11x14"),
        ("16x20", "16x20"),
        ("20x24", "20x24"),
        ("24x36", "24x36"),
        ("30x40", "30x40"),

    )

    SUBJECTS = (
        ("Traditional landscapes", "Traditional landscapes"),
        ("Local views", "Local views"),
        ("Modern or semi-abstract landscapes", "Modern or semi-abstract landscapes"),
        ("Abstracts", "Abstracts"),
        ("Portraits", "Portraits"),
        ("Figure studies", "Figure studies"),
        ("Seascapes, harbour and beach scenes", "Seascapes, harbour and beach scenes"),
        ("Wildlife", "Wildlife"),
        ("Impressionistic landscapes", "Impressionistic landscapes"),
        ("Surrealism", "Surrealism"),
    )

    name = models.CharField(max_length=100)
    discription = models.TextField()
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    size = models.CharField(choices=SIZES, max_length=7)
    subject = models.CharField(choices=SUBJECTS, max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MaxValueValidator(1000), MinValueValidator(1)])
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    image = models.ImageField()
    slug = models.SlugField(unique=True)
    def __str__(self):
        return f"{self.name} - {self.customer}"
