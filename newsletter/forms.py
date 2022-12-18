from django import forms
from .models import Newsletter


class NewsletterForm(forms.ModelForm):
    """
        Form to allow users to subscribe to newsletter.
    """

    class Meta:
        model = Newsletter
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            this_widget = self.fields[field].widget
            this_widget.attrs["placeholder"] = field
            this_widget.attrs["class"] = "border-black"
