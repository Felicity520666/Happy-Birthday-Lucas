# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define f = Character("Felisha", color="#E10072")
define l = Character("Lucas", color="#66ff00")
define I = Character("Isla", color="#FF5400")

transform smallright:
    zoom 0.7
    xalign 1.6
    yalign 1.0

transform smallleft:
    zoom 0.7
    xalign -0.7
    yalign 1.0

transform extrasmallright:
    zoom 0.3
    xalign 0.8
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
    scene sleep 
    with pixellate
    pause 6.0
    play music "happy-background-music-442792.mp3"
    call scene_loop
    scene yawn
    play sound "yawning-6096.mp3" volume 8.0
    pause 2.5
    show felisha glad
    play sound "aw-86103.mp3"
    f "Aw! Oh my gosh! I'm so excited today!"
    show felisha confident
    f "It's my brother Lucas' birthday! Yeah!"
    show felisha yes
    f "I've gotta make him the best birthday card!"
    show felisha scared
    f "But... I suck at making cards..."
    show felisha believe
    f "I have to mke a perfect birthday card for my perfect little bro!"
    show felisha glad
    f "Oh oh I know! I'll reach out to my bestie Isla!"
    show felisha confident
    f "She can totally help me with this!"
    show felisha yes
    f "Art's her major after all, she's definitely the expert!"
    show felisha glad
    f "Yeah! Let me text her!"
    scene 1 with blinds
    play sound "message.mp3"
    pause 0.5
    play sound "message.mp3"
    pause 3.0
    scene 2 
    with fade
    play sound "ping.mp3"
    pause 3.0
    show felisha glad at smallright 
    with moveinright
    f "Yeah! Isla's agreed to help me!"
    scene 2 
    with None
    show felisha yes at smallleft 
    with moveinright
    f "Off to her pet shop I go!"
    scene room with fade
    play sound "store-entrance-bell-188054.mp3" volume 1.5
    pause 1.0
    show felisha yes at smallleft 
    with moveinleft
    play sound "hello-278029.mp3" volume 5.5
    f "Hello!"
    show isla normal at smallright
    with fade
    play sound "why-hello-there-103596.mp3" volume 5.5
    I "Why hello there!"
    show isla hap at smallright
    with fade
    play sound "chuckle.mp3"
    I "You're lucky girl!"
    I "I just finished my shift at the shop!"
    show isla smile at smallright
    with fade
    I "We can make the card at my house together!"
    I "I apparently have some materials left over from my last art project!"
    show felisha believe at smallleft
    with fade
    f "What..."
    f "Shouldn't we go to the boutique to buy a beautiful and elegant card template?"
    show felisha scared at smallleft
    with fade
    f "Remember, I need the card to be perfect!!!"
    play sound "chuckle.mp3"
    I "Hey girl! Don't stress too much!"
    show isla normal at smallright
    with fade
    I "Bought cards might look nice, but they don't always show how much you truly care about your brother."
    show isla smile at smallright with fade
    I "Just trust me -- come with me, Ill show you!"
    show felisha believe at smallleft 
    with fade
    f "Oh... Okay then..."
    scene house 
    with dissolve
    play music "footsteps-dirt-gravel-6823.mp3" volume 4.5
    pause 2.5
    scene near 
    with fade
    pause 2.5
    scene inside
    play sound "opening-door-411632.mp3"
    play music "golden-sun-318286.mp3" fadein 2.0
    pause 2.5
    show isla normal at smallright 
    with fade
    I "Oh! Home sweet home~"
    I "Com here, Felisha!"
    show felisha smile at smallright 
    with fade
    I "I've got all my materials here!"
    I "I have makers, paper and cardstock, adhesives, cutting tools like scissors and a trimmer, plus stamps and ink!"
    show felisha believe at smallleft 
    with fade
    f "Umm... I don't think I can make a perfect birthday card with your leftover materials..."
    f "I'm not sure it's a good idea..."
    show isla normal at smallright
    I "Okay, listen to me, Felisha."
    I "You don't need a perfect birthday card for your brother."
    I "Nothing is perfect, and no one is perfect..."
    I "What really matters is showing your heart."
    I "Just do your best to show your love toward Lucas..."
    show felisha glad at smallleft 
    with fade
    f "Ummm... Good point... Let's do it then!"
    f "But please help me, Isla!"
    show isla silme at smallright 
    with fade
    play sound "chuckle.mp3"
    I "Of course I will!"
    I "Let's get started!"
    scene later 
    with dissolve
    play music "cutting-paper-303736.mp3"
    pause 5.0
    show felisha yes at smallleft 
    with fade
    f "Yes!!! Finally!!!"
    show felisha glad at smallleft 
    with fade
    f "I definitely put a lot of hard work and heart 💖 into making this birthday card."
    f "It really feels so different from just buying a cute one from the store..."
    show felisha confident at smallleft 
    with fade
    f "This one actually means something!"
    show isla smile at smallright 
    with moveinright
    I "See? Told ya girl! 😄"
    show isla normal at smallright 
    with fade
    I "Anyway, let's hurry over to Lucas' birthday before it's too late and show him the card!"
    scene celebrate 
    with dissolve
    play music "happy-birthday-368842.mp3" fadein 2.0
    pause 3.5
    show felisha yes at smallleft 
    with fade
    f "Hey! We're here, Lucas!"
    f "I have a suprise for you! Come here bro!"
    show lucas normal at extrasmallright 
    with moveinright
    l "Hi Felisha! You're finally here, sis!"
    l "Where have you been? I'm so glad you made it!"
    l "Come sit down and have some drink!"
    show felisha glad at smallleft 
    with fade
    f "Aww... you're so sweet, bro!"
    f "But wait..."
    play music "calm-jazz-220610.mp3" fadein 1.0
    f "I spend a lot of time preparing your card."
    f "I know it's not perfect, but it's made with warmth and sincerity!"
    show felisha confident at smallleft 
    with fade
    f "After all, nothing and no one in this world is {b}perfect{/b}!"
    show felisha glad at smallleft 
    with fade
    f "You are my precious little brother, but sometimes you ncan be a bit lazy and not as hardworking with your studies as you should be."
    show lucas embarrassed at extrasmallright 
    with fade
    show felisha believe at smallleft 
    with fade
    f "I'm saying this honestly because I worry about you..."
    f "I'm afraid you might lise your way, so I get anxious -- and sometimes I even scold you harshly..."
    show felisha glad at smallleft 
    with fade
    f "But you need to know this: {i}I love you{/i}."
    show lucas heart at extrasmallright 
    with fade
    f "I made this birthday card for you by hand."
    f "And even though it isn't perfect, it's just like you -- inperfect, but cute..."
    show felisha confident at smallleft 
    with fade
    f "I wish you a ver happy birday, my brother."
    f "Please always try your best to grow and improve!"
    show lucas pleasant at extrasmallright 
    with fade
    l "Sis... thank you! I really didn't know you were so good at crafts! Haha, thank you so much!"
    l "I'll definitely try my best to improve in the new year and achieve success."
    show lucas heart at extrasmallright 
    with fade
    l "So... thank you, Felisha..."
    l "Your handmmade birthday card is honestly all I could ever ask for."
    l "The time, effort, and love you put into it mean more to me than any gift ever could..."
    l "It truly made day and reminded me how lucky I am to have you in my life..."
    play music "happy-birthday-368842.mp3" fadein 2.0
    show lucas pleasant at extrasmallright 
    with fade
    l "So come on over -- let's slow things down and celebrate properly."
    l "We'll laugh, talk, and enjoy some if your favorite desserts and drinks together!"
    show lucas normal at extrasmallright 
    with fade
    l "No rush, no pressure -- just a simple, happy moment shared between us..."
    show felisha yes at smallleft 
    with fade
    f "Geez, Louis! Since when did you become so polite and charming? 😂"
    f ""
    
    

    # This ends the game.

    return
