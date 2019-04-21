from django import forms
from django.contrib.auth.models import User
from django.utils.encoding import smart_text
from students.models import UserDetail

class UserFullnameChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return smart_text(obj.get_full_name())

class VoteForm(forms.ModelForm):

    Ms_VSIT = UserFullnameChoiceField(queryset = User.objects.all().filter(is_superuser = 'False').order_by('first_name','last_name'))
    Mr_VSIT = UserFullnameChoiceField(queryset = User.objects.all().filter(is_superuser = 'False').order_by('first_name','last_name'))

    class Meta:
        model = UserDetail
        fields = ('Mr_VSIT', 'Ms_VSIT') 

    def save(self, user=None):
        user_detail = super(VoteForm, self).save(commit=False)
        if user:
            user_detail.user = user
            user_detail.voted = True
        user_detail.save()
        return user_detail