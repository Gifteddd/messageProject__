from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def save(self, room, commit=True):
        instance = super().save(commit=False)
        instance.room = room
        instance.user = self.user
        if commit:
            instance.save()
        return instance

