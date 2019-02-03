# Importa biblioteca utilizada para executar a funcao show_trailer.
import webbrowser

"""
Cria a classe Movie onde serao definidos os atributos dos filmes e a
funcao para exibir o trailer.
"""


class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
