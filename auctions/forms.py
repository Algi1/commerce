from django import forms
from .models import Listing, Bid, Comment, Category


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description',
                  'image', 'starting_price', 'category', 'is_active']


class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['bid_amount']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
