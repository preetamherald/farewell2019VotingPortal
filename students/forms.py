from django import forms
from django.contrib.auth.models import User
from django.utils.encoding import smart_text
from students.models import UserDetail

class UserFullnameChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return smart_text(obj.get_full_name())

class VoteForm(forms.ModelForm):

    class Meta:
        model = UserDetail
        fields = ('Mr_VSIT', 'Ms_VSIT') 

    def save(self, user=None):
        user_detail = super(VoteForm, self).save(commit=False)
        if user:
            user_detail.user = user
            f_name = (User.objects.all().filter(username=user).values_list('first_name', flat=True))[0]
            l_name = (User.objects.all().filter(username=user).values_list('last_name', flat=True))[0]
            name = f_name + " " + l_name
            user_detail.name = name
            user_detail.voted = True
        user_detail.save()
        return user_detail
1