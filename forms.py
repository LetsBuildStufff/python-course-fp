from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField


class CreateGameForm(FlaskForm):
    name = StringField("Unesite ime igrice")
    create_game = SubmitField("Dodaj igricu")


class UpdateGameForm(FlaskForm):
    selection = SelectField("Izaberite igricu za ažuriranje", choices=[])
    new_name = StringField("Upišite izmjenu")
    update_game = SubmitField("Ažuriraj igricu")


class DeleteGameForm(FlaskForm):
    selection = SelectField("Izaberite igricu za brisanje", choices=[])
    delete_game = SubmitField("Obriši igricu")
