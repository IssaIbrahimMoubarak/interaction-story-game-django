from django.db import models

class StoryNode(models.Model):
    key = models.CharField(max_length=100, unique=True)
    text = models.TextField()
    image = models.ImageField(upload_to='images/')
    color = models.CharField(max_length=7, default='#FFFFFF')

    def __str__(self):
        return self.key

class Choice(models.Model):
    node = models.ForeignKey(StoryNode, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    next_node = models.ForeignKey(StoryNode, related_name='next_choices', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.choice_text} -> {self.next_node.key}"
