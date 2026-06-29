from django.db import models
 
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/') # Requires Pillow library: pip install Pillow
    technologies = models.CharField(max_length=255, help_text="Comma-separated list of technologies")
    live_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
 
    def __str__(self):
        return f"{self.title} | {self.technologies}"
