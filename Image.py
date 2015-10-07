from pygame import *

startImage = image.load("Images/startscreen.jpg") # Start Screen Image
boardImage = image.load("Images/board.jpg") # Chess Board Image

buttonImage = image.load("Images/button.png") # Button Image

#-------------------------------Chess Piece Images------------------------------
blackPond = image.load("Images/Pieces/Black_Pond.png") # Black Pond Image
small_blackPond = transform.scale(blackPond, (34, 50)) # Small Black Pond for side bars

blackRook = image.load("Images/Pieces/Black_Rook.png") # Black Rook Image
small_blackRook = transform.scale(blackRook, (40, 50)) # Small Black Rook for side bars

blackKnight = image.load("Images/Pieces/Black_Knight.png") # Black Knight Image
small_blackKnight = transform.scale(blackKnight, (47, 50)) # Small Black Knight for side bar

blackBishop = image.load("Images/Pieces/Black_Bishop.png")  # Black Bishop
small_blackBishop = transform.scale(blackBishop, (50, 49)) # Small Black Bishop for side bar

blackQueen = image.load("Images/Pieces/Black_Queen.png") # Black Queen
small_blackQueen = transform.scale(blackQueen, (50, 49)) # Small Black Queen for side bar

blackKing = image.load("Images/Pieces/Black_King.png") # Black King
small_blackKing = transform.scale(blackKing, (50, 50)) # Small Black King for side bar

whitePond = image.load("Images/Pieces/White_Pond.png") # White Pond
small_whitePond = transform.scale(whitePond, (34, 50)) # Small White Pond for side bar

whiteRook = image.load("Images/Pieces/White_Rook.png") # White Rook
small_whiteRook = transform.scale(whiteRook, (40, 50)) # Small White Rook for side bar

whiteKnight = image.load("Images/Pieces/White_Knight.png") # White Knight
small_whiteKnight = transform.scale(whiteKnight, (47, 50)) # Small White King for side bar

whiteBishop = image.load("Images/Pieces/White_Bishop.png") # White Bishop
small_whiteBishop = transform.scale(whiteBishop, (50, 49)) # Small White Bishop for side bar

whiteQueen = image.load("Images/Pieces/White_Queen.png") # White Queen
small_whiteQueen = transform.scale(whiteQueen, (50, 49)) # Small White Queen for side bar

whiteKing = image.load("Images/Pieces/White_King.png") # White King
small_whiteKing = transform.scale(whiteKing, (50, 50)) # Small White 
#-------------------------------------------------------------------------------