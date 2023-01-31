#this is the way you can bring the teams scores
init python:
    class Team:
        def __init__ (self, score_nm1, score_nm2, score_nm3, score_nm4, score_nm5, score_nm6, score_hd1, score_hd2, score_hd3, score_hr1, score_hr2, score_hr3, score_dt1, score_dt2, score_dt3, score_dt4, score_fm1, score_fm2, score_fm3, score_tb):
            self.score_nm1 = score_nm1
            self.score_nm2 = score_nm2
            self.score_nm3 = score_nm3
            self.score_nm4 = score_nm4
            self.score_nm5 = score_nm5
            self.score_nm6 = score_nm6
            self.score_hd1 = score_hd1
            self.score_hd2 = score_hd2
            self.score_hd3 = score_hd3
            self.score_hr1 = score_hr1
            self.score_hr2 = score_hr2
            self.score_hr3 = score_hr3
            self.score_dt1 = score_dt1
            self.score_dt2 = score_dt2
            self.score_dt3 = score_dt3
            self.score_dt4 = score_dt4
            self.score_fm1 = score_fm1
            self.score_fm2 = score_fm2
            self.score_fm3 = score_fm3
            self.score_tb = score_tb
    
    class Map:
        def __init__ (self, name):
            self.name = name
            self.picked = False
            self.banned = False
$maps [Map("NM1"), Map("NM2")]        


# Declare characters used by this game. The color argument colorizes the 
# name of the character.

define Manten = Character("Manten", color="#add8e6")
define Crystal = Character("Crystal", color="#e455a8")
define lardon = Character("lardon", color="#44a8eb")
define Hawk = Character("NyghtHawk", color="#a9a9a9")
define Taevas = Character("Taevas", color="#972768")
define Nelou = Character("Nelou", color="#154863")
define Terli = Character("TerliManor", color="#df3096")
define KIHCA = Character("KIHCA", color="#814e0b" )
define Nagi = Character("MomoNagi", color="#9b194f")
define smun = Character("smun", color="#bd1a1a")
define Ayziar = Character("Ayziar", color="#323531")
define Edgar = Character("Eggdarr", color="#ffffff")
define Longar = Character("Longaaaar", color="#456349")
define Nerowo = Character("Nerowo", color="#896543")

#These are the variables we are gonna use 

default nelou_team = 0 
default terli_call_day2 = 0
default entente = 0.80

#These are our special transitions
define fadehold = Fade(0.5, 1.0, 0.5)

#album variables
image France_tryouts = "Cards/fr.png"

# The game starts here.

label start:
        
    "During a sunny day..."
    scene bg gym
    with fade
    show nightmare normal at right 
    with dissolve
    show hobo normal at left 
    with dissolve
    
    "NightmareParty" "Ladies and gentlemen. We are proud to say that we are officially launching a brand new project : the 6 digits World Cup of osu!, second iteration !"
    
    "Hobo" "You have one month to prepare your teams through tryouts in your dedicated training camps, all around Indonesia, and select the 8 players that will represent your countries. Good luck and may the best win !"
    
    hide nightmare normal
    with dissolve
    hide hobo normal
    with dissolve
    
    Manten "It's time for me to shine. In the first iteration, I didn't make it into the team, but this time i'll be able to play for my country. Maybe as a captain, who knows ?"
    
    
    show bg black
    with fade
    play music "audio/SWEET_CANDY.mp3" fadein 1.0 volume 0.7

    "???" "I think everything is set up !"
    
    scene bg salle_principale
    with fade
    show lardon normal at right
    with dissolve
    show crystal normal at left
    with dissolve

    Crystal "Yep, it's gonna be about time to bring as much players as we can in here. Manten, lardon, can you ask everyone you know to join ?"
    Manten "{i}Crystal is our new coach. she was the captain for team France in 6WC1, and she has done a lot of work for the french osu! community while we were waiting for 6WC2, like reffing and commentating matches.{/i}"
    lardon "On my way ! I'll send an invite to the french osu! community discord !"
    Manten "{i}lardon is the previous host of 6WC. He made the whole 6 digits scene dream when he announced the first ever World Cup for our player range. Now, he is a player, just like me.{/i}"
    Manten "Do you have Taevas's contact ? I think he should have decayed back to 6 digits now."
    lardon "He is ? I'll contact him then, he could be a great player for our team."
    
    hide lardon normal
    with dissolve
    show crystal normal at center
    with moveinleft
    
    Crystal "I am gonna pool for tryouts, enjoy the rest of your day !"
    
    hide crystal normal
    with dissolve

    show hawk normal 
    with fade
    "???" "Hello..."
    show hawk normal at right
    with moveinright
    show crystal normal at left 
    with dissolve
    with vpunch

    Crystal "OMFG A NEW PLAYER ! What's your name ? "
    Hawk "Uhhhhh... I'm NyghtHawk. Nice to meet you guys."
    Manten "Nice to meet you too ! We are still preparing the whole thing, but make yourself comfy !"
    Hawk "{b}{i}Th...ks ! I'll s.. you g... ...ter !{/i}{/b}"
    Manten "Ehhh... Excuse me i didn't get what you said."
    Hawk "Oh, it's my throat, it fucks up sometimes. Anyway, i said i'll see you guys later."
    Manten "Okay, see you later NyghtHawk !"   
    
    hide hawk normal
    with dissolve
    hide crystal normal 
    with dissolve 
    show lardon normal at right 
    with dissolve
    show taevas normal at left 
    with dissolve

    lardon "I found a wild Taevas ! And he's down to play with us !"
    Taevas "Hi ! Smh, everything is scuffed here !"
    Manten "Wow our best deranker is here !"

    with vpunch

    Taevas "I'M NOT A DERANKER I ONLY DECAY !!"
    lardon "He totally is a deranker."
    Taevas "Don't bully me lardon... {i}tears up{/i}"
    Manten "There, there. It was just a little joke. Anyway, enjoy being with us !"

    show nelou normal 
    with vpunch

    Nelou "HOLD UP ! I'm the great, massive, FABULOUS Nelyth ! You can call me Nelou, or Nel."
    "in this game, there are choices that are important for the future. Choose carefully !"
    menu: 
        "It's the great Nel ! Welcome bro !":
            Nelou "Oh it's Manten ! Hi bro !"
            $ entente =+ 0.05
        "Shut it you golem. Welcome tho !":
            $ entente =- 0.05
            Nelou "I'm gonna tear you in shreads."

    Manten "{i}Nelyth is one of the players of 6WC1 for team France. I don't know exactly what happened during 6WC1, but he is a great player, no one can deny it.{/i}"

    hide lardon normal 
    with dissolve
    show crystal normal at right
    with dissolve 

    Crystal "I invited Nel to play 6WC again ! Although he will have to play tryouts again."
    Nelou "Who wants to 1v1 me ???? I want to see how good everyone is !"
    Taevas "Sure, come here"

    hide taevas normal 
    hide nelou normal
    with moveoutleft
    pause(3.0)

    show crystal normal
    
    Crystal "Alright, i'll show you guys's rooms where you can rest, play, and do whatever you want !"

    scene bg bedroom
    pause (2.0)

    show crystal normal 
    with moveinleft
    
    Crystal "Here is your {b}totally not messy{/b} room !"
    Manten "That's..."
    menu:
        "very messy":
            Crystal "Fuck you !"
            $ entente =-0.05
        "absolutely great":
            Crystal "See, it's perfect !"
            $ entente =+ 0.05
    Crystal "Anyway, I'll leave you for now. Enjoy your night !"
    Manten "Thanks !"
    
    hide crystal normal
    with dissolve

    Manten "I should call Terli so he knows I am trying out for France..."

    "{color=#00ff00} BEEP BEEP BEEP{/color}"
    stop music fadeout 1.0
    show terli black
    with dissolve
    play music "audio/Terli_Theme.mp3" fadein 1.0

    Terli "{color=#00ff00}Hi Manten ! How is my son doing so far ?"
    Manten "{i}TerliManor is a german player. He played during 6WC1, and we played many tournaments together. He also is my mommy !{/i}"

    Manten "Hi mommy ! I was about to call you !"
    Terli "{color=#00ff00}I saw you registrated for 6WC2 ! How is your room ? Are you comfy enough ?{/color}"
    Manten "The room is fine i'd say, Crystal did everything for us. How about yours ?"
    Terli "{color=#00ff00}Well, we are all in a 5 stars room so... I'd say it's pretty great.{/color}"
    show bg bedroom
    with vpunch
    Manten "WHAT THE FUCK ?! 5 STARS ROOMS FOR EVERYONE ??? HOW RICH IS GERMAN TEAM ACTUALLY ??"
    Terli "{color=#00ff00}Well, NightmareParty and Hobo gave a budget in function of our results in 6WC1... So yeah, Germany is pretty rich{/color}"
    Manten "That explains a lot... France got top 16 so we have a decent campus but not as good as Germany's because you ended your run as 4th."
    Terli "{color=#00ff00}Exactly. We're playing with the absolute best PCs to train, and we have a coaching by two professional coaches. {/color}"
    Manten "That doesn't matter at all. We're gonna beat you, whatever the cost is."
    Terli "{color=#00ff00}All right, I look forward to see your team grow and become stronger. Although, I don't think you will be able to beat us at all.{/color}"
    Manten "I'm gonna sleep mommy, today has been an exhausting day. See you later around our campus !"
    Terli "{color=#00ff00}See you later ! Sleep tight !"
    
    hide terli black
    show bg black
    with fade
    stop music fadeout 1.0
label day_2:
    "The next day..."

    scene bg salle_principale 
    with hpunch 
    
    Taevas "I beat Nel in the match yesterday !"

    show taevas normal at left 
    with moveinleft
    show nelou normal at right
    with easeinright 

    Nelou "I can't believe it... {i}pouts{/i}"
    lardon "So Nel lost ?"

    show lardon normal
    with dissolve
    
    lardon "I mean, Taevas has always been a deranker, so... it was to be expected."
    Taevas "I. AM. NOT. A. DERANKER."
    lardon "Don't care, didn't ask. Also, we have to welcome the new players for today."

    hide nelou normal
    hide taevas normal 
    with fade
    show kihca normal at right
    show pot2fleur normal at left
    with dissolve

    "Pot2Fleur" "Hello ! I bring you a brand new member ! KIHCA, introduce yourself please."
    KIHCA " 78 73 71 71 69 82"
    KIHCA "Those who know are racist btw"
    "Pot2Fleur" "This guy... Anyway, he's a speed and DT player, enjoy your time with him !"

    hide pot2fleur normal
    hide lardon normal
    hide kihca normal
    with dissolve
    show bg black
    with fade

    "And this way, many new players came into the campus."
    "{color=#ff8c00}Yugo, Longaaaar, Noroy, Seiishitsu, smun, MiniQumania, ThePhoenix57, MomoNagi, Mykado le gato, Riperofsouls, Nerowo, Eggdarr Ayziar and many others joined the team. Some Lurkers also came in, like Foudou or MyzeJD.{/color}"
     
    show bg salle_d_entrainement
    with fade
    show nagi normal at right
    with easeinright
    show nelou normal at left 
    with easeinleft

    
    Nagi "Oh wow ! The training rooms are so cool !"
    Nelou "Of course they are. We had the same ones during 6WC1. The PCs are pretty solid !"
    Manten "{i}I remember these training rooms. I participated in scrims here, and many other trainings during 6WC1 tryouts.{/i}"
    Nagi "Hey guys, since there are 8 PCs in this one room, how about we do something cool ? Like, training matches between members of the 6WC2 ?"

    show lardon normal
    with dissolve

    lardon "That's a great idea Nagi ! How about we name this Intrateams ?"
    Manten "Yep, sounds good !"
    Nagi "Should we test this brand new concept right now ? lardon, Manten, you guys will be captains !"
    Manten "Alright, i'll pick first if you are fine with this lardon."
    lardon "Yes sure !"
    Manten "Then i'll pick Nagi."
    lardon "I will pick smun !"
    Manten "and last, but not least i'll pick..."
    menu:
        "Nelyth, the HR player":
            $ nelou_team += 1
            Manten "I pick Nel !"
        "Taevas, the all rounder":
            Manten "I take Taevas !"

    if nelou_team >= 1:
        jump Nelou_IT_Ending
    elif nelou_team < 1:
        jump Taevas_IT_Ending
    
label Nelou_IT_Ending:
    

    $ team1 = Team(1200000, 1400000, 900000, 650000, 1000000, 400000, 1100000, 400000, 800000, 2000000, 1500000, 1900000, 1500000, 2000000, 1200000, 1100000, 1900000, 900000, 800000, 1200000)
    $ team2 = Team(1000000, 1000000, 1400000, 1900000, 1000000, 650000, 1200000, 700000, 1200000, 800000, 800000, 800000, 1400000, 1700000, 1900000, 1800000, 1700000, 1000000, 1000000, 1400000)
    hide lardon normal
    with dissolve
    Nelou "I knew you were gonna choose me, I'm the best after all"
    Manten "We'll see about that when you will play against Taevas again."
    Nagi "Let's do this guys !"
    
    
    hide nagi normal
    hide nelou normal
    with dissolve
    show bg osu 
    with fade
    show nelou normal at left
    show nagi normal at right
    with dissolve

    Manten "Knowing that both Nel and me are on the team, we're almost sure to win every single HR in the pool."
    Nelou "Yeah, I'd not be surprised if they-"
    lardon "{color=#00ff00}We ban HR1 !!{/color}"
    Nelou "Banned an HR."
    Manten "And here, we'll ban..."
    hide nelou normal
    hide nagi normal
    with dissolve
    
    call screen THE_BAN

    call screen THE_PICK
    

    



    # Manten "Alright, noted lardon ! On our side, we will ban HD2 !"
    # Nagi "Sounds good."
    
    # show nelou normal
    # with hpunch

    # Nelou "NOOOOO IT WAS A BANGER !!"
    # Manten "But we are against both lardon and Taevas. We never win this point, there is not a single dimension where this is possible."
    # Nelou "Okay..."
    # Manten "How about we take the first pick ? And insta pick HR2 ?"
    # Nagi "I suck at HR but if you guys can carry this..."
    # Manten "No worries, we should be fine, no one plays precision anyway."

    # hide nelou normal 
    # hide nagi normal 
    # with dissolve
    # show bg osu
    # with fadehold 
    # show nelou normal at left
    # show nagi normal at right
    # with dissolve

    # "Results of HR1 : "
    # "Team Lardon : 1,236,568 - 1,983,320 : Team Manten"
    # "Team Lardon : 0 - 1 : Team Manten"

    # Nelou "WTF, smun got a big combo !"
    # smun "{color=#00ff00}I main precision... But you guys just acc gamed me.{/color}"
    # Manten "Well, I used to main precision maps too so... I guess we will be rivals during the entire tryouts time !"
    # lardon "{color=#00ff00}Well played guys ! We pick HD1 !{/color}"
    # Manten "Oh well, not my best map but i should be decent."
    # Nelou "Care, Taevas obliterated me yesterday on HDs."
    # Nagi "And I'm bad so we are probably gonna lose this point."
    # Manten "Let's just give it a shot, we never know what will happen. Good luck !"

    # hide nelou normal 
    # hide nagi normal 
    # with dissolve
    # show bg osu
    # with fadehold 
    # show nelou normal at left
    # show nagi normal at right
    # with dissolve

    # "Results of HD1 :"
    # "Team Lardon : 1,596,563 - 1,532,960"
    # "Team Lardon : 1 - 1 : Team Manten"

    # Nelou "Ah man, that was so close !!"
    # Manten "Indeed... We got unlucky there."
    # lardon "{color=#00ff00}Wow, I never thought it would be THAT close. Good job guys.{/color}"
    # Manten "Maybe we can pick some DT ?"
    # Nagi "I can play DT2 in general, not much more though."
    # Manten "Alright, DT2 it is !"
    # lardon "{color=#00ff00}Good luck !{/color}"

    # hide nelou normal 
    # hide nagi normal 
    # with dissolve
    # show bg osu
    # with fadehold 
    # show nelou normal at left
    # show nagi normal at right
    # with dissolve

    # "Results of DT2 :"
    # "Team Lardon : 2,012,635 - 1,863,569 : Team Manten"
    # "Team Lardon : 2 - 1 : Team Manten"

    # Manten "Well, I think we just got Taevas'ed. Nice FC !"
    # Taevas "{color=#00ff00}Thanks ! You guys played very well too {/color}"
    # Nelou "No way, I lost to Tae once again ! I'm such a golem bro..."
    # lardon "{color=#00ff00}Losing to Tae is not a bad thing you know, he's cracked.{/color}"
    # Manten "I guess it's time for lardon's Team to pick now !"
    # lardon "{color=#00ff00}Yes, we'll pick DT1 !{/color}"
    # Nagi "Good luck and have fun !"

    # hide nelou normal 
    # hide nagi normal 
    # with dissolve
    # show bg osu
    # with fadehold 
    # show nelou normal at left
    # show nagi normal at right
    # with dissolve

    # "Results of DT1 :"
    # "Team Lardon : 2,153,568 - 1,786,436"
    # "Team Lardon : 3 - 1 : Team Manten"

    # Nelou "What the hell, Taevas is always winning... he's just a crackhead"
    # Manten "Indeed he is. We have to pick now."
    # Nagi "Maybe we should try a NM1 ? The skillcap might work since we have Nel"
    # Manten "Hmmm... Good idea, let's try this. "
    # lardon "{color=#00ff00}Alright ! Good luck !{/color}"

    # hide nelou normal 
    # hide nagi normal 
    # with dissolve
    # show bg osu
    # with fadehold 
    # show nelou normal at left
    # show nagi normal at right
    # with dissolve

    # "Results of NM1 : "
    # "Team Lardon : 2,596,361 - 2,131,727 : Team Manten"
    # "Team Lardon : 4 - 1 : Team Manten"
    # "--- END OF THE MATCH ---"

    # Nelou "OH COME ON I FCED AND IT'S NOT ENOUGH ! Haaaa, well played guys, you were just better... But I'll beat you next time !"
    # lardon "{color=#00ff00}GGWP to everyone ! That was great !{/color}"
    # Manten "Yeah, I really enjoyed this little match. Great idea you got there Nagi."

    # "Matchcosts Top 3 : \n
    # 1 - Taevas (2.93) \n 
    # 2 - Nelyth (2.23) \n
    # 3 - lardon (2.22)"

    
    hide nagi normal
    hide nelou normal
    hide NM1_selection
    hide NM2_selection
    hide NM3_selection
    show bg black
    with fadehold

jump Terli_Call_Day2 

label Taevas_IT_Ending:
    hide lardon normal
    with dissolve
    hide nelou normal
    with dissolve
    show taevas normal at left
    with dissolve
    
    Taevas "Alright, i'll join Manten's team !"
    Manten "Nice, let's destroy them !"
    Taevas "It should be easy :sunglasses:"
    Nagi "Let's do this guys !"

    show bg osu 
    with fade

    Manten "Alright, we know that Nel is a menace when it comes to HR, so how about we just ban it ?"
    Taevas "Sounds good, do whatever you want !"
    Nagi "Yeah, also, i can't play HR."
    Manten "alright, HR1 banelings, it is !"
    lardon "{color=#00ff00}We will ban DT1 !{/color}"
    Manten "Noted ! What will you pick ?"
    lardon "{color=#00ff00}We pick HR2 !{/color}"
    
    hide taevas normal 
    hide nagi normal 
    with dissolve
    show bg osu
    with fadehold 
    show taevas normal at left
    show nagi normal at right
    with dissolve

    "Results of HR2 :"
    "Team Lardon : 997,557 - 1,028,936 : Team Manten"
    "Team Lardon : 0 - 1 : Team Manten"

    Manten "Sheesh, that was close ! Good job everyone !"
    Taevas "Wow that was harder than what i expected... Good job anyway"
    Nagi "I got carried haha, thanks guys !"
    Manten "No probs you will carry us on the next map ! Talking about the next map, what should we pick ?"
    Nagi "Well, i'm decent at DT2 and that's it..."
    Taevas "Then, let's confirm our break point with DT2."
    Manten "Alright, we pick DT2 !"
    lardon "{color=#00ff00}Okay, good luck !"

    hide taevas normal 
    hide nagi normal 
    with dissolve
    show bg osu
    with fadehold 
    show taevas normal at left
    show nagi normal at right
    with dissolve

    "Results of DT2 :"
    "Team Lardon : 1,698,653 - 2,198,003 : Team Manten"
    "Team Lardon : 0 - 2 : Team Manten"

    Manten "Holy shit I fced !"
    Taevas "I broke on nothing aaah ! Good job Manten !"
    Nagi "Wow you guys are so good... I only got 400k points !"
    lardon "{color=#00ff00}Alright, we will pick NM5{/color}"
    Manten "Good luck guys !"

    hide taevas normal 
    hide nagi normal 
    with dissolve
    show bg osu
    with fadehold 
    show taevas normal at left
    show nagi normal at right
    with dissolve


    "Results of NM5 :"
    "Team Lardon : 1,762,563 - 1,634,456 : Team Manten"
    "Team Lardon : 1 - 2 : Team Manten"

    Nagi "I tried my best sorry guys"
    Manten "It's alright, I kinda trolled. Nice FC Taevas !"
    Taevas "Thanks !"
    Nelou "{color=#00ff00}Let's fucking go I out acced Taevas !{/color}"
    lardon "{color=00ff00} Good job Nel !{color=00ff00}"
    Manten "Alright, what do we pick now ?"
    Taevas "We already picked DT earlier so we can't do it again right now... How about we just go with a HD map ?"
    Manten "Sounds good, except I can't play low AR so... HD1 might be our best option."
    Nagi "Oh no consistency..."
    Manten "Don't worry Nagi we got your back !"
    lardon "{color=#00ff00}GLHF!{/color}"

    hide taevas normal 
    hide nagi normal 
    with dissolve
    show bg osu
    with fadehold 
    show taevas normal at left
    show nagi normal at right
    with dissolve
    
    "Results of HD1 :"
    "Team Lardon : 1,149,635 - 1,798,632 : Team Manten"
    "Team Lardon : 1 - 3 : Team Manten"

    show taevas normal
    with vpunch 

    Manten "I FCed !!"
    Taevas "Let's gooo Manten !"
    Nagi "You guys are so good !"
    smun "{color=#00ff00}I just threw super hard, I can't believe it."
    lardon "{color=#00ff00}No worries, we can still win. We'll have to go to Tie Breaker though.{/color}"
    Manten "What will be your pick guys ?"
    Nelou "{color=#00ff00}Go FM1, I want to battle Manten on HR to know how much he improved since last year !{/color}"
    lardon "{color=#00ff00}Okay, FM1 it is ! Good luck guys !"
    Manten "Alright ! I go HR and Taevas goes HD ?"
    Nagi "I'd prefer taking HD to be honest, I'm more comfortable with HD."
    Taevas "I can take whatever. We can also overmod like the gigachads we are !"
    Manten "That could be fun ! Let do this, me on HR, and both of you on HD"
    lardon "{color=#00ff00}Oh overmod ? You guys are confident ! Good luck !{/color}"
    
    hide taevas normal 
    hide nagi normal 
    with dissolve
    show bg osu
    with fadehold 
    show taevas normal at left
    show nagi normal at right
    with dissolve

    "Results of FM1 :"
    "Team Lardon : 2,011,003 - 2,031,657 : Team Manten"
    "Nelyth : 711,963 (HR) - (HR) 823,369 : Manten"
    "Team Lardon : 1 - 4 : Team Manten"
    "--- END OF THE MATCH ---"

    Manten "OMG I combogamed Nel ! GGWP guys !"
    Nelou "{color=#00ff00}... No way... I get beaten twice in a row ? Really ?{/color}"
    Taevas "GGWP, it was a cool match !"
    Nagi "Yep, i enjoyed it too. I hope we can do it again soon !"
    lardon "{color=#00ff00}GGs guys, you deserved that one !{/color}"

    "Matchcosts top 3 :\n
    1 - Taevas (2.72)\n
    2 - Nelyth (2.41)\n
    3 - Manten (2.23)\n"

    show bg black
    with fadehold
    hide nagi normal
    hide taevas normal
    
jump Terli_Call_Day2




label Terli_Call_Day2:

    "After the IT (Intrateams) everyone came back to their room."

    show bg bedroom
    with dissolve

    Manten "Ahhh, that was fun. Maybe I should call mommy."
    "{color=#00ff00}BEEP BEEP BEEP{/color}"

    show terli black
    with dissolve

    Terli "{color=#00ff00}What's up my boy ?{/color}"
    Manten "I'm doing fine, what about you ?"
    Terli "{color=#00ff00}Well, we're doing nicely as well. We created our Scrimmage team, or almost, so we are already able to take on the world before the actual world cup.{/color}"
    Manten "Wow we need to play against each other at some point ! I'll talk about that to Crystal."
    Terli "{color=#00ff00}Did you guys made a team or something ?{/color}"
    Manten "Uhhh... I don't think so, but we'll probably ask some people who registrated to join the crew to beat you."
    Terli "{color=#00ff00}Alright, i'll look forward to it !{/color}"
    Manten "Also, since we are teaming with Tey and SplitRunPro for BQT5, I'd like to spar with Tey to see how good i've become since last year."
    Terli "{color=#00ff00}Alright, i'll sak him. Oh wait he's here.{/color}"
    Terli "{color=#00ff00}TEY !!!{/color}"
    show terli black
    with hpunch 
    Terli "{color=#00ff00}Would you mind playing against Manten some scrimmage ? ... What do you mean yes ?? I don't leave you a choice anyway.{/color}"
    Manten "{i}And there he goes, bullying Tey again.{/i}"
    Terli "{color=#00ff00}Alright, you'll play against each other in two days !{/color}"
    Manten "Sounds good ! I'll tell Crystal about the scrimmage between our two teams later too."
    Terli "{color=#00ff00}Nice ! See you later, sleep tight !{/color}"
    
    hide terli black 
    with dissolve
    show bg black
    with fadehold

$ terli_call_day2 += 1 
jump Day3

label Day3:
#HERE IS THE NEW MINI MAP

#"You now have an access to the map ! (WIP)"

"after a good night of sleep..."

play music "audio/SWEET_CANDY.mp3" fadein 1.0 volume 0.7
show bg salle_principale
with fade
show crystal normal
with dissolve

Crystal "Hello everyone. I hope everyone slept well, because I have a massive announcement to do."
Crystal "As some of you know, we are gonna face some of the other countries before the tryouts start. And we will start today with... United Kingdom."
Crystal "Not the easiest matchup, but we are here to gather as much experience as we can."
Crystal "There is the team for today's match : "
Crystal "KIHCA as captain, MisterBros, bigburgerhumm, Mykado, epge and Juikl T-T. The rest will come in the stadium to cheer for them."
Manten "{i}So both me and lardon are out for the first scrimmage... same for Taevas and Nel ? I'm not too sure of what is happening but let's say Crystal knows what she is doing...{/i}"

show lardon normal at right
with fade

lardon "Good luck to the players, I'll be in backup to help you doing your picks and bans."

hide lardon normal 
hide crystal normal
with fade

Manten "I should go to the germans building to see Terli before the match."

show bg black
with fadehold

"go to the germans building"

call screen map_button


    




return

