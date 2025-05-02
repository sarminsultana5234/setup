from django import forms
from .models import userpost


class userpoststatus(forms.ModelForm):
    class Meta:
        model=userpost 
        fields=['user_name','post']
        
   


