from django import forms
from .models import Review

# way 1
# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your Name", max_length=100, error_messages={
#         "required": "Your name must not be empty!",
#         "max_length": "Please enter a shorter name!"

#     })
#     review_text = forms.CharField(label="Your Feedback", max_length=200, widget=forms.Textarea)
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)

# way 2
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # fields = ['user_name', 'review_text', 'rating']
        fields = '__all__'
        # exclude = ['rating']
        labels = {
            'user_name': 'Your Name',
            'review_text': 'Your Feedback',
            'rating': 'Your Rating'
        }
        error_messages = {
            "user_name":{
                        "required": "Your name must not be empty!",
                        "max_length": "Please enter a shorter name!"
            }
        }