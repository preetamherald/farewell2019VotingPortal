from django import forms
from students.models import UserDetail

class VoteForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields = ('Mr_VSIT', 'Ms_VSIT', 'Popular', 'vote4') 

    def save(self, user=None):
        user_detail = super(VoteForm, self).save(commit=False)
        if user:
            user_detail.user = user
            user_detail.voted = True
        user_detail.save()
        return user_detail