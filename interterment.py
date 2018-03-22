import fresh_tomatoes
import media
toy_story=media.Movie("Toy Story",
                      "Toy Story Detials",
                      "C:\Users\mahmoude.SUDATEL\PycharmProjects\Moves\img/1 (1).JPG",
                      "https://www.youtube.com/watch?v=rNk1Wi8SvNc")

King_fo=media.Movie("King Fo Fiter",
                      "King Fo Fiter Detials",
                      "C:\Users\mahmoude.SUDATEL\PycharmProjects\Moves\img/1 (2).JPG",
                      "https://www.youtube.com/watch?v=rEt7qASyNIo")

Missi=media.Movie("Miss Story",
                      "Miss Story Detials",
                      "C:\Users\mahmoude.SUDATEL\PycharmProjects\Moves\img/1 (3).JPG",
                      "https://www.youtube.com/watch?v=c9fqYzn_9H8")

Animal=media.Movie("Animal Fiter",
                      "Animal Fiter Detials",
                      "C:\Users\mahmoude.SUDATEL\PycharmProjects\Moves\img/1 (4).JPG",
                      "https://www.youtube.com/watch?v=ohBpYckm2Ww")
moves=[toy_story,King_fo,Missi,Animal]
fresh_tomatoes.open_movies_page(moves)