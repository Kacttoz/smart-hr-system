from django.db import models
from django.conf import settings
from num2words import num2words # We'll need to install this

class OfferLetter(models.Model):
    DESIGNATION_CHOICES = (
        ('Sales Manager', 'Sales Manager'),
        ('Assistant Sales Manager', 'Assistant Sales Manager'),
        ('Agent Relationship Manager', 'Agent Relationship Manager'),
        ('HR Manager', 'HR Manager'),
        ('HR Executive', 'HR Executive'),
        ('IT Executive', 'IT Executive'),
        ('Sales Executive', 'Sales Executive'),
        ('IT Sales Manager', 'IT Sales Manager'),
        ('IT Manager', 'IT Manager'),
        ('Social Media Manager', 'Social Media Manager'),
        ('Trainer', 'Trainer'),
    )

    STATUS_CHOICES = (
        ('DRAFT', 'Draft'),
        ('SENT', 'Sent'),
        ('FAILED', 'Failed'),
    )

    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    candidate_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Male')
    email = models.EmailField(help_text="Candidate Email")
    designation = models.CharField(max_length=100, choices=DESIGNATION_CHOICES)
    salary = models.DecimalField(max_digits=12, decimal_places=2)
    salary_in_words = models.CharField(max_length=255, blank=True, null=True)
    letter_content = models.TextField(help_text="Custom content or generated HTML")
    joining_date = models.DateField()
    
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='generated_letters')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='DRAFT')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.salary:
            try:
                # Convert salary to Integer for words (ignoring decimals usually or handle them)
                self.salary_in_words = num2words(int(self.salary), lang='en_IN').title()
            except Exception:
                pass
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.candidate_name} - {self.designation}"
