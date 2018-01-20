from django import forms

class CharForm(forms.Form):
    char_name = forms.CharField(label='Character name', max_length=100)
    player_name = forms.CharField(label='Player name', max_length=100)
    max_health = forms.IntegerField()
    strength = forms.IntegerField()
    dexterity = forms.IntegerField()
    constitution = forms.IntegerField()
    intelligence = forms.IntegerField()
    wisdom = forms.IntegerField()
    charisma = forms.IntegerField()
    choices = (
        ('0', 'Acrobatics'),
        ('1', 'Animal Handling'),
        ('2', 'Arcana'),
        ('3', 'Athletics'),
        ('4', 'Deception'),
        ('5', 'History'),
        ('6', 'Insight'),
        ('7', 'Intimidation'),
        ('8', 'Investigation'),
        ('9', 'Medicine'),
        ('10', 'Nature'),
        ('11', 'Perception'),
        ('12', 'Performance'),
        ('13', 'Persuasion'),
        ('14', 'Religion'),
        ('15', 'Sleight of Hand'),
        ('16', 'Stealth'),
        ('17', 'Survival'),
    )
    proficiencies = forms.MultipleChoiceField(choices=choices, widget=forms.CheckboxSelectMultiple)


class CharUpdateForm(forms.Form):
    health = forms.IntegerField()
