from wtforms import Form, StringField, TextAreaField, SelectField
from wtforms.fields.simple import FileField
from wtforms import validators, PasswordField


# Forms
class PostForm(Form):
    title = StringField('Заголовок статьи:')
    content = TextAreaField('Текст статьи:', render_kw={'rows': 15})
    category = SelectField('Категория', choices=[])
    picture = FileField('Картинка для статьи')


class Registration(Form):
    '''Форма регистрации'''
    username = StringField('логин *', validators=[validators.DataRequired()])
    first_name = StringField('Имя *', validators=[validators.DataRequired()])
    last_name = StringField('Фамилия *', validators=[validators.DataRequired()])
    phone = StringField('Контактный номер')
    email = StringField('Почта *', validators=[validators.DataRequired()])
    password = PasswordField('Пароль *', validators=[validators.Length(min=1, max=15),
                                                     validators.EqualTo('confirm',
                                                                        message='Пароли должны совпадать')])
    confirm = PasswordField('Подтверждение пароля', validators=[validators.DataRequired()])


class UserLogin(Form):
    '''Форма авторизации'''
    username = StringField('Логин')
    password = PasswordField('Пароль')

















