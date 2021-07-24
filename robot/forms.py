from django import forms

column, row = 2, 12
MONTH = [[0 for _ in range(column)] for _ in range(row) ]

count = 1910
column, row = 2, 113
YEAR = [[0 for _ in range(column)] for _ in range(row) ]

column, row = 2, 31
DAY = [[0 for _ in range(column)] for _ in range(row) ]

class LoginForm(forms.Form):
    username = forms.CharField(label = '姓名', max_length=10)
    password = forms.CharField(label = '密碼(出生年月日)', widget=forms.PasswordInput())

class SignupForm(forms.Form):
    
    for i in range(12):
        for j in range(2):
            MONTH[i][j] = str(i+1)

    for i in range(113):
        for j in range(2):
            YEAR[i][j] = str(count)
        count += 1
            

    for i in range(31):
        for j in range(2):
            DAY[i][j] = str(i+1)

    GENDER = [
        ['MAN', '男'],
        ['WOMAN', '女']
    ]

    username = forms.CharField(label = '姓名', max_length=10)
    year = forms.ChoiceField(label = '出生年', choices = YEAR)
    month = forms.ChoiceField(label = '月', choices = MONTH)
    day = forms.ChoiceField(label = '日', choices = DAY)
    gender = forms.ChoiceField(label = '性別', choices = GENDER)


    

