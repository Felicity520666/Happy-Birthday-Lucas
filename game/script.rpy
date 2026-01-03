# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define f = Character("Felisha", color="#E10072")
define l = Character("Lucas", color="#ffcccc")
define i = Character("Isla", color="#FF5400")

transform smallright:
    zoom 0.7
    xalign 1.8
    yalign 1.0

transform smallleft:
    zoom 0.7
    xalign -0.7
    yalign 1.0

label scene_loop:
    $ i = 0
    while i < 6:
        scene sleep
        pause 0.25
        scene open
        pause 0.25
        $ i += 1
    return


# The game starts here.

label start:
    play music "snoring-71560.mp3"
    scene sleep with pixellate
    pause 6.0
    play music "happy-background-music-442792.mp3"
    call scene_loop
    scene yawn
    play sound "yawning-6096.mp3" volume 8.0
    pause 2.5
    show glad
    play sound "aw-86103.mp3"
    f "Aw! Oh my gosh! I'm so excited today!"
    hide glad
    show confident
    f "It's my brother Lucas' birthday! Yeah!"
    hide confident
    show yes
    f "I've gotta make him the best birthday card!"
    hide yes
    show scared
    f "But... I suck at making cards..."
    hide scared
    show believe
    f "I have to mke a perfect birthday card for my perfect little bro!"
    hide believe
    show glad
    f "Oh oh I know! I'll reach out to my bestie Isla!"
    hide glad
    show confident
    f "She can totally help me with this!"
    hide confident
    show yes
    f "Art's her major after all, she's definitely the expert!"
    hide yes
    show glad
    f "Yeah! Let me text her!"
    scene 1 with ease
    play sound "message.mp3"
    pause 1.0
    play sound "message.mp3"
    pause 3.0
    scene 2 with fade
    play sound "ping.mp3"
    # This ends the game.

    return
