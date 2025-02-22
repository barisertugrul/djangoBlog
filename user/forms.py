from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, label='Username')
    password = forms.CharField(max_length=50, label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=50, label='Confirm Password', widget=forms.PasswordInput)
    email = forms.EmailField(max_length=50, label='Email')
    first_name = forms.CharField(max_length=50, label='First Name')
    last_name = forms.CharField(max_length=50, label='Last Name')

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Passwords do not match.')

        values = {
            'username': cleaned_data.get('username'),
            'password': password,
            'email': cleaned_data.get('email'),
            'first_name': cleaned_data.get('first_name'),
            'last_name': cleaned_data.get('last_name')
        }
        return values
