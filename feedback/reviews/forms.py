from django import forms
from .models import Review

# class ReviewForm(forms.Form):
#     name = forms.CharField(max_length=100,label="Your Name",error_messages={
#         "required": "Please enter your name"
#     })
#     review_text = forms.CharField(label="Your Feedback",widget=forms.Textarea)
#     rating = forms.IntegerField(label="Your Rating",min_value=1,max_value=5,error_messages={
#         "required": "Please enter your rating"
#     })

# Modelforms

class ReviewForm(forms.ModelForm):
   #Metadata
   class Meta:
       model = Review
       fields = ['name','review_text','rating']
       labels = {
           "name" : "Your Name",
           "review_text":"Your Feedback",
           "rating":"Your Rating"    
       }
       error_messages = {
           "name":{
               "required": "Please enter your name"
           }
       }
