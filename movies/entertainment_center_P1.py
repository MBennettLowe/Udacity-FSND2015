
# packages and modules called to support program
import media_P1
import fresh_tomatoes


# Classes used to create instances of Movies for use with the fresh
# tomatoes.py fil
X_Men = media_P1.Movie(
                        "X Men: Days of Future Past",
                        "The ultimate X-Men ensemble fights a war for the"
                        " survival of the species across time periods"
                        " in X MEN: DAYS OF FUTURE PAST",
                        "Hugh Jackman, James McAvoy, Jennifer Lawrence",
                        "May 23, 2014 (USA)",
                        "http://t3.gstatic.com/images?q=tbn:ANd9GcSp1xUUrh6IW4gwa8j7p8WxU7Yt21mWhLVwZ5CejaXF6KsrOtjs",  # noqa
                        "https://www.youtube.com/watch?v=1LGiUsb6AMM&feature=youtu.be")  # noqa

Fist_of_Legend = media_P1.Movie(
                                 "Fist of Legend",
                                 "In 1937 a Chinese martial artist returns to"
                                 " Shanghai to find his teacher dead and his"
                                 " school harassed by the Japanese.",
                                 "Jet Li, Shinobu Nakayama, Siu-Ho Chin",
                                 "December 22, 1994",
                                 "http://www.framedart.com/product-images/AWAAQAHQ-P182107.jpg",  # noqa
                                 "https://www.youtube.com/watch?v=LPEzoOifD1k")  # noqa

Enter_the_Dragon = media_P1.Movie(
                                   "Enter The Dragon",
                                   "Bruce Lee plays a martial-arts expert"
                                   " determined to help capture the narcotics"
                                   " dealer whose gang was responsible for the"
                                   " death of his sister. Lee enters a kung fu"
                                   " competition in an attempt to fight his"
                                   " way to the dealer's headquarters with the"
                                   " help of some friends.",
                                   "Bruce Lee, John Saxon, Jim Kelly",
                                   "August 19, 1973 (USA)",
                                   "http://t1.gstatic.com/images?q=tbn:ANd9GcRsH21kTB2avWroiM3X28MoN2igjrlYhMgKN4nIL3ast-FaeDmj",  # noqa
                                   "https://www.youtube.com/watch?v=tB-QGOChuQc")  # noqa

The_Dark_Knight_Rises = media_P1.Movie(
                                        "The Dark Knight Rises",
                                        "It has been eight years since Batman"
                                        "(Christian Bale), in collusion with"
                                        " Commissioner Gordon (Gary Oldman),"
                                        " vanished into the night. Assuming"
                                        " responsibility for the death of"
                                        " Harvey Dent, Batman sacrificed"
                                        " everything for what he and Gordon"
                                        " hoped would be the greater good."
                                        " However, the arrival of a cunning"
                                        " cat burglar (Anne Hathaway) and a"
                                        " merciless terrorist named Bane (Tom"
                                        " Hardy) force Batman out of exile and"
                                        " into a battle he may not be able to"
                                        " win.",
                                        "Christian Bale, Tom Hardy, Anne"
                                        "Hathaway",
                                        "July 20, 2012 (USA)",
                                        "http://t1.gstatic.com/images?q=tbn:ANd9GcQSGF8_VbDqKF0B_4IQ0NF87VMDSy7_MPKryawR-qLnSIPQwo5z",  # noqa
                                        "https://www.youtube.com/watch?v=g8evyE9TuYk")  # noqa

Brams_Stoker_Dracula = media_P1.Movie(
                                       "Brams Stoker Dracula",
                                       "Adaptation of Bram Stoker's classic"
                                       " vampire novel. Gary Oldman plays"
                                       " Dracula whose lonely soul is"
                                       ' determined to reunite with his lost'
                                       " love, Mina (Winona Ryder). In Britain"
                                       " Dracula begins a reign of terror and"
                                       " seduction draining the life from her"
                                       " closest friend, Lucy (Sadie Frost)."
                                       " Together they try and drive Dracula"
                                       " away.",
                                       "Gary Oldman, Winona Ryder",
                                       "November 13, 1992 (USA)",
                                       "http://t0.gstatic.com/images?q=tbn:ANd9GcRMqx0vTbNTmr3Ms_byitC6LnBPBOJ_fmbqP1iI_YRRa3SJrRFX",  # noqa
                                       "https://www.youtube.com/watch?v=fgFPIh5mvNc")  # noqa

Cooley_High = media_P1.Movie(
                              "Cooley_High",
                              "Richard (Cochise) Morris (Lawrence-Hilton"
                              "Jacobs) a local basketball hero, and Leroy"
                              " (Preach) Jackson (Glynn Turman), who dreams of"
                              " a career in writing, are likable Chicago high"
                              " school students in 1960s Chicago. They're into"
                              " hanging out with friends, pretty girls and the"
                              " Motown sounds so popular during the era. Each"
                              " wants to make it big in his own way, but not"
                              " everybody they meet is looking out for them,"
                              " as they learn when a seemingly harmless outing"
                              " goes awry.",
                              "Glynn Turman and Lawrence Hilton-Jacobs",
                              "June 25, 1975",
                              "http://www.gstatic.com/tv/thumb/dvdboxart/386/p386_d_v7_aa.jpg",  # noqa
                              "https://www.youtube.com/watch?v=tmw1Llp92PU")  # noqa

# Movie array created for use to call the fresh tomatoes.py file

movies = [X_Men, Fist_of_Legend, Enter_the_Dragon, The_Dark_Knight_Rises,
          Brams_Stoker_Dracula, Cooley_High]
fresh_tomatoes.open_movies_page(movies)
print(media_P1.Movie.__doc__)




