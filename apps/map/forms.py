from django import forms
from .models import Marker


class MarkerUpdateForm(forms.ModelForm):
    """Form to update Marker."""

    class Meta:
        """Meta objects."""

        model = Marker
        fields = ['latitude', 'longitude', 'email', 'description', 'category', 'sub_category']

    def clean(self):

        # data from the form is fetched using super function
        super(MarkerUpdateForm, self).clean()

        # extract the username and text field from the data
        description = self.cleaned_data.get('description')

        # conditions to be met for the username length
        if len(description) < 5:
            self._errors['description'] = self.error_class([
                'Minimum 5 characters required'])

        # return any errors if found
        return self.cleaned_data

    def save(self):
        """Overriding the save method."""
        import pdb;pdb.set_trace()
        data = self.cleaned_data

