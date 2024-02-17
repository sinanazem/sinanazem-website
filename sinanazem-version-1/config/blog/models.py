from django.db import models

class Article(models.Model):
    CHOICES_OPTION_STATUS = (
        ("D","Draft"),
        ("P", "Publish")
    )
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    abstract = models.TextField()
    image = models.ImageField(upload_to="images")
    content = models.TextField()
    status = models.CharField(max_length=1, choices=CHOICES_OPTION_STATUS)
    publish = models.DateField()
    updatetime = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    
