from django.shortcuts import render, get_object_or_404
from .models import StoryNode

def story_node(request, key='start'):
    node = get_object_or_404(StoryNode, key=key)
    choices = node.choices.all()
    return render(request, 'story/node.html', {'node': node, 'choices': choices})
