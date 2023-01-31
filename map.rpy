screen minimap:
    frame:
        imagemap:
            ground "map/map_isométrique.png"
            hotspot (156, 136, 259, 386) action Jump("german_building")
            hotspot (623, 505, 483, 248) action Jump("terrain")


screen map_button:
    imagebutton:
        xpos 1600
        ypos 50
        idle "map/map_button.png"
        action Jump("map")

label map:
    call screen minimap 


label terrain:
    show bg terrain
    "you went to the football field."
    "nothing else to see here"
    hide bg terrain
    call screen map_button 

label german_building:
    show germany_entrance
    "you entered the Germany building."
    "no one is here for now (WIP)"
    hide germany_entrance
    call screen map_button
