# Importa modulo media para criar instancias dos filmes.
import media
import fresh_tomatoes

# Cria instancias para os meus filmes favoritos.
blade_runner_2049 = media.Movie("Blade Runner 2049", "O replicante chamado K "
                                "descobre um segredo que pode abalar a mundo.",
                                "https://upload.wikimedia.org/wikipedia/en/9/"
                                "9b/Blade_Runner_2049_poster.png",
                                "https://www.youtube.com/watch?v=okJdrvOdZFI")

vingadores_guerra_infinita = media.Movie("Vingadores - Guerra Infinita",
                                         "Os Vingadores unem forcas com os "
                                         "Guardioes da Galaxia para enfrentar "
                                         "Thanos, que almeja juntar as Joias "
                                         "do Infinito.",
                                         "https://upload.wikimedia.org/"
                                         "wikipedia/pt/thumb/9/90/"
                                         "Avengers_Infinity_War.jpg/"
                                         "250px-Avengers_Infinity_War.jpg",
                                         "https://www.youtube.com/"
                                         "watch?v=t_ULBP6V9bg")

mad_max_estrada_da_furia = media.Movie("Mad Max - Estrada da Furia",
                                       "Max se junta a Imperatriz Furiosa para"
                                       " fugir do lider cultista Immortan Joe"
                                       " e seu exercito.",
                                       "https://upload.wikimedia.org/"
                                       "wikipedia/pt/thumb/2/23/"
                                       "Max_Mad_Fury_Road_Newest_Poster.jpg/"
                                       "250px-Max_Mad_Fury_Road_Newest_Poster"
                                       ".jpg",
                                       "https://www.youtube.com/"
                                       "watch?v=IVmf82obaaA")

star_wars_despertar_da_forca = media.Movie("Star Wars - O Despertar da Forca",
                                           "Rey encontra BB-8, um drone com "
                                           "informacoes do paradeiro de Luke "
                                           "Skywalker.",
                                           "https://upload.wikimedia.org/"
                                           "wikipedia/pt/thumb/a/ae/"
                                           "Starwars_06.jpg/"
                                           "250px-Starwars_06.jpg",
                                           "https://www.youtube.com/"
                                           "watch?v=4r0287tUEgk")

clube_da_luta = media.Movie("Clube da Luta", "Edward sofre de insonia e visita"
                            " grupos de apoio em busca de libertacao "
                            "emocional.", "https://upload.wikimedia.org/"
                            "wikipedia/pt/thumb/2/2b/FightClubPoster.jpg/"
                            "230px-FightClubPoster.jpg", "https://www.youtube."
                            "com/watch?v=SUXWAEX2jlg")

sociedade_do_anel = media.Movie("O Senhor dos Aneis - A Sociedade do Anel",
                                "O destino da Terra-media esta em risco,"
                                " e o 'Um Anel' precisa ser destruido.",
                                "https://upload.wikimedia.org/wikipedia/pt/"
                                "thumb/0/0c/The_Fellowship_Of_The_Ring.jpg/"
                                "250px-The_Fellowship_Of_The_Ring.jpg",
                                "https://www.youtube.com/watch?v=bXBpqdKJI6k")

# Cria uma lista com os meus filmes favoritos.
filmes = [blade_runner_2049, vingadores_guerra_infinita,
          mad_max_estrada_da_furia, star_wars_despertar_da_forca,
          clube_da_luta, sociedade_do_anel]

# Cria pagina web com a lista dos meus filmes favoritos.
fresh_tomatoes.open_movies_page(filmes)
