from django import forms
from django.core import validators

class FormCourse(forms.Form):
    code = forms.CharField(
        label="Código del Curso",
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese el Código del Curso',
                'class': 'code_form_course'
            }
        ),
        validators=[
            validators.MinLengthValidator(1, 'El código es corto'),
            validators.RegexValidator('^[A-Za-z0-9nÑ ]*$','El código tiene caracteres inválidos','code_invalido')            
        ] 
    )
    name = forms.CharField(
        label="Nombre del Curso",
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese el Nombre del Curso',
                'class': 'name_form_course'
            }
        ),
        validators=[
            validators.MinLengthValidator(5, 'El nombre es corto'),
            validators.RegexValidator('^[A-Za-z0-9nÑ ]*$','El nombre tiene caracteres inválidos','name_invalido')            
        ] 
    )
    
    hour = forms.IntegerField(
        label = "Horas",
        required=True,
        widget = forms.NumberInput,
        validators=[
            validators.MinValueValidator(1,'El mínimo de horas es 1'),
            validators.MaxValueValidator(10,'Superaste el límite de horas')
        ]
    )
    
    credits = forms.IntegerField(
        label = "Creditos",
        required=True,
        widget = forms.NumberInput,
        validators=[
            validators.MinValueValidator(1,'El mínimo de creditos es 1'),
            validators.MaxValueValidator(10,'Superaste el límite de creditos')
        ]
    )
    
    opciones_state = [
        (1, 'Con Cupos'),
        (0, 'Sin Cupos'),
    ]
    state = forms.TypedChoiceField(
        label = "¿Estado?",
        required=True,
        choices = opciones_state
    )

class FormCareer(forms.Form):
    name = forms.CharField(
        label="Nombre de la Carrera",
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese el Nombre de la Carrera',
                'class': 'name_form_career'
            }
        ),
        validators=[
            validators.MinLengthValidator(5, 'El nombre es corto'),
            validators.RegexValidator('^[A-Za-z0-9nÑ ]*$','El nombre tiene caracteres inválidos','name_invalido')            
        ] 
    )
    
    shortname = forms.CharField(
        label="ShortName de la Carrera",
        max_length=10,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese el ShortName de la Carrera',
                'class': 'shortname_form_career'
            }
        ),
        validators=[
            validators.MaxLengthValidator(5, 'El shortname es largo'),
            validators.RegexValidator('^[A-Za-z0-9nÑ ]*$','El nombre tiene caracteres inválidos','shortname_invalido')            
        ] 
    )
    
    image = forms.ImageField(
        label="Imagen de la Carrera",
        required=False,
        widget=forms.FileInput(
            attrs={
                'class': 'image_form_career'
            }
        )
    )
    
    opciones_state = [
        (1, 'Habilitada'),
        (0, 'No Habilitada'),
    ]
    state = forms.TypedChoiceField(
        label = "¿Estado?",
        required=True,
        choices = opciones_state
    )