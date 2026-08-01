from uuid import uuid4

from sqlmodel import Field, Session, SQLModel, create_engine, select

engine = create_engine("sqlite:///database.db")


def create_tables():
    SQLModel.metadata.create_all(engine)


class Game(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid4().hex), primary_key=True)
    text: str


def create_game(game: Game) -> Game:
    with Session(engine) as s:
        s.add(game)
        s.commit()
    return game


def update_game(game_id: str, new_text: str) -> Game | None:
    with Session(engine) as s:
        query = select(Game).where(Game.id == game_id)
        result = s.exec(query).first()
        if result:
            result.text = new_text
            s.commit()
            return result
        return None


def view_games() -> list[Game]:
    with Session(engine) as s:
        query = select(Game)
        results = s.exec(query).all()
    return list(results)


def delete_game(game_id: str) -> bool:
    with Session(engine) as s:
        query = select(Game).where(Game.id == game_id)
        result = s.exec(query).first()
        if result:
            s.delete(result)
            s.commit()
            return True
        return False


if __name__ == "__main__":
    create_tables()
