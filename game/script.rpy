# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define f = Character("Felisha", color="#ffcccc")
define l = Character("Lucas", color="#ffcccc")


# The game starts here.

label start:
    play music "happy-background-music-442792.mp3"
    
    scene bg room
    f ""
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
