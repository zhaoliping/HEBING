from django.db import models

# Create your models here.

		
class Book(models.Model):
    ISBN = models.CharField(primary_key = True,max_length = 10)
    Title = models.CharField(max_length = 20)
    AuthorID = models.ForeignKey(Author)
    Publisher = models.CharField(max_length = 20)
    PublishDate = models.DateField()
    Price = models.FloatField()
    def __unicode__(self):
	    return self.Title
