from django import forms

class SentimentForm(forms.Form):
	input_sentiment = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'placeholder':'Enter Sentiment Text'}))

