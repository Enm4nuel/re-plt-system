from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


#class DataForm(ModelForm):
#	class Meta:
#		model = Data
#		fields = '__all__'