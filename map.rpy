label map_start:
screen gameUI:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "map/map_button.png"
        action ShowMenu("MapUI")
    
screen MapUI():
    tag statsUI
    add "map/map_isométrique.png"



