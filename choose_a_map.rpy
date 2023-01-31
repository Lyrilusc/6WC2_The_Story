
#bans screens    
screen nm1_banned:
    imagebutton:
        xpos 200
        ypos 20
        idle "mods/pNM1.png"
screen nm2_banned:
    imagebutton:
        xpos 200
        ypos 160
        idle "mods/pNM2.png"    
screen nm3_banned:
    imagebutton:
        xpos 200
        ypos 300
        idle "mods/pNM3.png" 
screen nm4_banned:
    imagebutton:
        xpos 200
        ypos 20
        idle "mods/pNM4.png"
screen nm5_banned:
    imagebutton:
        xpos 200
        ypos 160
        idle "mods/pNM5.png"    
screen nm6_banned:
    imagebutton:
        xpos 200
        ypos 300
        idle "mods/pNM6.png" 
screen THE_BAN:
    imagebutton:
        xpos 200
        ypos 20
        idle "mods/NM1.png"
        hover "mods/uNM1.png"
        action [Hide("mods/NM1.png"), Jump("NM1_BAN")]
    imagebutton:
        xpos 200
        ypos 160
        idle "mods/NM2.png"
        hover "mods/uNM2.png"
        action [Hide("mods/NM2_idle.png"), Jump("NM2_BAN")]
    imagebutton:
        xpos 200
        ypos 300
        idle "mods/NM3.png"
        hover "mods/uNM3.png"
        action [Hide("mods/NM3.png"), Jump("NM3_BAN")]  
    imagebutton:
        xpos 200
        ypos 440
        idle "mods/NM4.png"
        hover "mods/uNM4.png"
        action [Hide("mods/NM4.png"), Jump("NM4_BAN")]
    imagebutton:
        xpos 200
        ypos 580
        idle "mods/NM5.png"
        hover "mods/uNM5.png"
        action [Hide("mods/NM5_idle.png"), Jump("NM5_BAN")]
    imagebutton:
        xpos 200
        ypos 720
        idle "mods/NM6.png"
        hover "mods/uNM6.png"
        action [Hide("mods/NM6.png"), Jump("NM6_BAN")]  
#picks screens

screen THE_PICK:
    imagebutton:
        xpos 200
        ypos 20
        idle "mods/NM1.png"
        hover "mods/uNM1.png"
        action [Hide("mods/NM1.png"), Jump("NM1_PICKED")]

