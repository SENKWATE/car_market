from django.db import models
from django.urls import reverse

class Car(models.Model):
	make = models.CharField(max_length=120)
	model = models.CharField(max_length=120)
	year = models.IntegerField()
	car_img=models.ImageField(null=True, blank=True)

	def __str__(self):
		return "{} {} - {}".format(self.make, self.model, self.year)

	def get_absolute_url(self):
		return reverse('car-detail', kwargs={'car_id':self.id})

# 	def get_image_filename(instance, filename):
#     title = instance.post.title
#     slug = slugify(title)
#     return "post_images/%s-%s" % (slug, filename)  


# class Images(models.Model):
#     post = models.ForeignKey(Post, default=None)
#     image = models.ImageField(upload_to=get_image_filename,
#                               verbose_name='Image)