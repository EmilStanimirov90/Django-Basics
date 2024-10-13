from django import forms
from pip._vendor.chardet.metadata.languages import Language

from forumApp.posts.choices import LanguageChoice
from forumApp.posts.models import Post


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class PostForm(forms.Form):

    title = forms.CharField(
        max_length=100,
    )
    content = forms.CharField(
        widget=forms.Textarea,

    )

    author = forms.CharField(
        max_length=30,

    )

    created_at = forms.DateTimeField()

    languages = forms.ChoiceField(
        choices=LanguageChoice.choices
    )

# EXAMPLE:
# class PersonForm(forms.Form):
#     STATUS_CHOICES = (
#         (1, "Draft"),
#         (2, "Published"),
#         (3, "Archived"),
#     )
#     person_name = forms.CharField(
#         required=True,
#         error_messages={'required': 'Please enter your name'},
#         widget=forms.TextInput(attrs={'placeholder': 'Your name'}),
#         label="Add person name please",
#         max_length=10 ,
#     )
#     birth_date = forms.DateField()
#     file = forms.FileField()
#     person_name2 = forms.CharField(
#         label="",
#         initial="toshko", #podava stoinost v poleto
#         max_length=10,
#     )
#     age = forms.IntegerField()
#
#     is_lecturer = forms.BooleanField()
#
#     terms_of_service = forms.BooleanField()
#
#     status = forms.ChoiceField(
#         choices=STATUS_CHOICES,
#     )
#
#     status2 = forms.CharField(
#         widget=forms.Select(choices=STATUS_CHOICES),
#     )
#     status3 = forms.IntegerField(
#         widget=forms.RadioSelect(choices=STATUS_CHOICES),
#     )
#     checkboxes = forms.MultipleChoiceField(
#         choices=STATUS_CHOICES
#     )
#
#     checkboxes2 = forms.CheckboxSelectMultiple(
#         choices=STATUS_CHOICES
#     )
#
