from flask import Flask, flash, redirect, render_template, request

from database import Game, create_game, delete_game, update_game, view_games
from forms import CreateGameForm, DeleteGameForm, UpdateGameForm

flask = Flask(__name__)
flask.config["SECRET_KEY"] = "my_secret_key"


# Glavna stranica
# Sadrži
# - Forma za upis igrice
# - Forma za update igrice
# - Forma za brisanje igrice
# - Pregled igrice
@flask.route("/", methods=["GET", "POST"])
def home():
    games = view_games()

    create_game_form = CreateGameForm()
    update_game_form = UpdateGameForm()
    delete_game_form = DeleteGameForm()

    # Populate choices data with game data
    game_choices = [(game.id, game.text) for game in games]
    update_game_form.selection.choices = game_choices
    delete_game_form.selection.choices = game_choices

    # Grab the form "submit button" name (which is a key in a dict in python)
    # Check which condition applies and execute functions
    form_data = request.form
    if form_data.get("create_game") and create_game_form.validate_on_submit():
        game_text = create_game_form.name.data
        if game_text:
            game = Game(text=game_text)
            create_game(game)
            flash("Igrica uspješno spremljena")
            return redirect("/")

    if form_data.get("update_game") and update_game_form.validate_on_submit():
        game_id = update_game_form.selection.data
        new_text = update_game_form.new_name.data

        if game_id and new_text:
            update_game(game_id, new_text)
            flash("Igrica uspješno ažurirana")
            return redirect("/")

    if form_data.get("delete_game") and delete_game_form.validate_on_submit():
        game_id = delete_game_form.selection.data
        delete_game(game_id)
        flash("Igrica uspješno obrisana")
        return redirect("/")

    return render_template(
        "index.html",
        create_game_form=create_game_form,
        update_game_form=update_game_form,
        delete_game_form=delete_game_form,
        games=games,
    )


if __name__ == "__main__":
    flask.run(debug=True)
