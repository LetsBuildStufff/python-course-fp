from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField


class CreateGameForm(FlaskForm):
    name = StringField("Unesite ime igrice")
    submit = SubmitField("Dodaj igricu")


class UpdateGameForm(FlaskForm):
    selection = SelectField("Izaberite igricu za ažuriranje", choices=[])
    submit = SubmitField("Ažuriraj igricu")


class DeleteGameForm(FlaskForm):
    selection = SelectField("Izaberite igricu za brisanje", choices=[])
    submit = SubmitField("Obriši igricu")
