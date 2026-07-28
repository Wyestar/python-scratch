# digital simulation of boardgame mancala

# always move counterclockwise
# choose cell on your side,
# move all pieces to next cells leaving one piece in each until out of pieces
# if last piece lands in your store, go again
# if last piece lands in empty space on your side,
# capture other player pieces in cell across, move pieces to your store
# capture ends turn

# field = pits
# harvest = seeds/stones
# store = store

# board layout
# p2-store | L | K | J | I | H | G | p1-store
# p2-store | A | B | C | D | E | F | p1-store

# p1-store and p2-store are one Cell each
# looped linked list

# june 6
# TODO: core game functoinality working
# work on board visualization, use python library
# try with pygame or pygbag
# pyodide, data visualization. pyscript, this layers on top of pyodide
# put game in web app, allow two users to connect and play
# firebase leaderboard tracking win counts

# TODO: one player mode
# v1: simple AI that just chooses random valid fields on p2 side
# v2: actual localized LLM that considers board state and player actions
