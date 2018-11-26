from django import forms
from .models import Friend
from .models import Message

class HelloForm(forms.Form):
    name = forms.CharField(label ='Name') #labelはhtmlファイルの表示方法を変えている
    mail = forms.CharField(label = 'Mail')
    gender = forms.BooleanField(label='Gender', required=False)
    age = forms.IntegerField(label = 'Age')
    birthday = forms.DateField(label='Birth', required=False)

class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name', 'mail', 'gender', 'age', 'birthday']


class CheckForm(forms.Form):
    str = forms.CharField(label='String')

    def clean(self):
        cleaned_data = super().clean()
        str = cleaned_data['str']
        if (str.lower().startswith('no')):
            raise forms.ValidationError('You input "No!"')

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['title', 'content', 'friend']