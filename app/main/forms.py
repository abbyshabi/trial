from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError,SelectField
from wtforms.validators import Required,Email
#from .models import User

class PostForm(FlaskForm):

    title = StringField('Blog title',validators=[Required()])
    post = TextAreaField('Blog', validators=[Required()])
    submit = SubmitField('Publish')
    
   

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
   
    body = TextAreaField('comment', validators=[Required()])
    author = TextAreaField('By', validators=[Required()])
    submit = SubmitField('Submit')

class SubscribeForm(FlaskForm):
    name = StringField("Your Name")
    email = StringField("Email")
    submit= SubmitField('Subscribe')

class PostUpdateForm(FlaskForm):
    title = StringField('Blog title',validators=[Required()])
    body = TextAreaField('Blog', validators=[Required()])
    submit = SubmitField('Publish') 

