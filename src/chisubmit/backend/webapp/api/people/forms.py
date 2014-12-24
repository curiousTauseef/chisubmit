from wtforms import Form
from wtforms.validators import InputRequired, Optional,\
    Length, Email
from wtforms.fields import StringField, BooleanField


class CreatePersonInput(Form):
    id = StringField(validators=[Length(max=36), InputRequired()])
    first_name = StringField(validators=[Length(max=36), InputRequired()])
    last_name = StringField('last_name',
                            validators=[Length(max=36, min=5),
                                        InputRequired()])
    email = StringField(
        validators=[InputRequired(), Length(max=128, min=10), Email()])
    git_server_id = StringField('git_server_id',
                                validators=[Length(max=36, min=5),
                                            Optional()])
    git_staging_server_id = StringField('git_staging_server_id',
                                        validators=[Length(max=36, min=5),
                                                    Optional()])


class UpdatePersonInput(Form):
    first_name = StringField(validators=[Length(max=36), InputRequired()])
    last_name = StringField('last_name',
                            validators=[Length(max=36, min=5),
                                        Optional()])
    email = StringField(
        validators=[InputRequired(), Length(max=128, min=10), Email()])
    git_server_id = StringField('git_server_id',
                                validators=[Length(max=36, min=5),
                                            Optional()])
    git_staging_server_id = StringField('git_staging_server_id',
                                        validators=[Length(max=36, min=5),
                                                    Optional()])

class GenerateAccessTokenInput(Form):
    password = StringField(validators=[InputRequired()])
    reset = BooleanField(validators=[Optional()])
