import json
import os
from dataclasses import dataclass

import chess.pgn
from PIL import Image, ImageDraw, ImageFont

WIDTH = 1000
HEIGHT = 1000

BOARD_OFFSET = 180

TEXT_X_POS = 140
TEXT_Y_POS = 900

FONT = ImageFont.truetype("assets/GTWalsheimPro-Regular.ttf", 16)


@dataclass
class Attribute:
    trait_type: str
    value: str

    def json(self):
        return {
            "trait_type": self.trait_type,
            "value": self.value,
        }


@dataclass
class GameMetadata:
    name: str
    description: str
    image: str

    attributes: list[Attribute] = None

    def json(self):
        return {
            "name": self.name,
            "description": self.description,
            "image": self.image,
            "attributes": [attribute.json() for attribute in self.attributes],
        }


class GamesParser:
    def __init__(self, games_folder: int):
        self.games_folder = games_folder

    def get_games(self) -> list[chess.pgn.Game]:
        games = []
        for name in os.listdir(self.games_folder):
            file = open(f"{self.games_folder}/{name}")
            while True:
                game = chess.pgn.read_game(file)

                if game is None:
                    break

                games.append(game)
        return games

    def parse_game(self, game_id: int, game: chess.pgn.Game) -> GameMetadata:
        attributes = [
            Attribute("Event", game.headers["Event"]),
            Attribute("White", game.headers["White"]),
            Attribute("Black", game.headers["Black"]),
            Attribute("Result", game.headers["Result"]),
            Attribute("Date", game.headers["Date"]),
        ]

        metadata = GameMetadata(
            name=f"Kasparov's Legacy #{game_id}",
            description="Discover the mind-bending brilliance of chess legend Garry Kasparov in our NFT collection. Immerse yourself in the strategic battles and masterful moves that defined his illustrious career. Each NFT captures a moment of chess history, offering a unique glimpse into the world of the grandmaster.",
            image=None,
            attributes=attributes,
        )

        with open(f"out/metadata/{game_id}.json", "w") as f:
            f.write(json.dumps(metadata.json()))

        return metadata

    def _render_text(
        self, draw: ImageDraw, game: chess.pgn.Game, game_id: int
    ):
        date = game.headers["Date"]

        result = game.headers["Result"].split("-")[0].strip()
        if result == "1":
            winner = "White"
        elif result == "1/2":
            winner = "Draw"
        else:
            winner = "Black"

        draw.text(
            (TEXT_X_POS, TEXT_Y_POS),
            f"{game.headers['White']} · {game.headers['Black']}",
            font=FONT,
            fill=(255, 255, 255),
            align="center",
        )

        draw.text(
            (TEXT_X_POS, TEXT_Y_POS + 28),
            f"Date: {date}",
            font=FONT,
            fill=(75, 75, 75),
            align="left",
        )

        draw.text(
            (TEXT_X_POS, TEXT_Y_POS + (18 * 2) + 10),
            f"Winner: {winner}",
            font=FONT,
            fill=(75, 75, 75),
            align="left",
        )

        _, _, w, _ = draw.textbbox(
            (0, 0),
            f"#{game_id}",
            font=FONT,
        )

        draw.text(
            (860 - w, TEXT_Y_POS),
            f"#{game_id}",
            font=FONT,
            fill=(75, 75, 75),
            align="right",
        )

    def generate_image(self, game_id: int, game: chess.pgn.Game):
        base = Image.open("assets/board.png")

        draw = ImageDraw.Draw(base)
        self._render_text(draw, game, game_id)

        board = game.end().board()

        for index, symbol in enumerate(
            str(board).replace(" ", "").replace("\n", "")
        ):
            if symbol == ".":
                continue

            x = (index % 8) * 80 + BOARD_OFFSET
            y = (index // 8) * 80 + BOARD_OFFSET

            if symbol.isupper():
                color = "White"
            else:
                color = "Black"

            if symbol.lower() == "p":
                piece = "Pawn"
            elif symbol.lower() == "r":
                piece = "Rook"
            elif symbol.lower() == "n":
                piece = "Knight"
            elif symbol.lower() == "b":
                piece = "Bishop"
            elif symbol.lower() == "q":
                piece = "Queen"
            elif symbol.lower() == "k":
                piece = "King"

            image = Image.open(f"assets/{piece}{color}.png")
            base.paste(image, (x, y), image)

        base.save(f"out/images/{game_id}.png")


p = GamesParser("games")

games = p.get_games()
for i, game in enumerate(games):
    print(p.parse_game(i, game).name)
    p.generate_image(i, game)
