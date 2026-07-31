from flask import Flask, render_template

from forms import CreateGameForm, DeleteGameForm, UpdateGameForm

flask = Flask(__name__)
flask.config["SECRET_KEY"] = "my_secret_key"


# Glavna stranica
# Sadrži
# - Forma za upis igrice
# - Forma za update igrice
# - Forma za brisanje igrice
# - Pregled igrice
@flask.route("/")
def home():
    create_game_form = CreateGameForm()
    update_game_form = UpdateGameForm()
    delete_game_form = DeleteGameForm()

    return render_template(
        "index.html",
        create_game_form=create_game_form,
        update_game_form=update_game_form,
        delete_game_form=delete_game_form,
    )


if __name__ == "__main__":
    flask.run(debug=True)
