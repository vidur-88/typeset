from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)


class Paragraph(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.TextField()
    priority = models.IntegerField(default=0)


class Comment(models.Model):
    paragraph = models.ForeignKey(Paragraph, on_delete=models.CASCADE)
    text = models.TextField()
