from django import forms

class FeedbackForm(forms.Form):
    RATING_CHOICES = [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]
    SATISFACTION_CHOICES = [('yes', 'Yes'), ('no', 'No')]
    DEPARTMENT_CHOICES = [('sale', 'Sale'), ('support', 'Support'), ('finance', 'Finance')]
    TOPIC_CHOICES = [('website', 'Website'), ('product', 'Product'), ('customer_service', 'Customer Service')]

    name = forms.CharField(label='Name', max_length=100)
    email = forms.CharField(label='Email')
    rating = forms.ChoiceField(label='Rating', choices=RATING_CHOICES, widget=forms.RadioSelect)
    comments = forms.CharField(label='Comments', widget=forms.Textarea(attrs={'rows': 6}))
    department = forms.ChoiceField(label='Department', choices=DEPARTMENT_CHOICES, widget=forms.Select)
    topic = forms.ChoiceField(label='Topic', choices=TOPIC_CHOICES, widget=forms.Select)
    satisfaction = forms.ChoiceField(label='Are you Satisfied with our services', choices=SATISFACTION_CHOICES, widget=forms.RadioSelect)
    additional_info = forms.CharField(label='Additional Information', widget=forms.Textarea)