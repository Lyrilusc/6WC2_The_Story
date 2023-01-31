init python:
    gallery = Gallery()

    gallery.button("France Tryouts")
    gallery.image("Cards/fr.png")
    gallery.image("Cards/Manten.png")
screen players_cards:
    tag menu
    
    hbox:
        xalign 0.5
        yalign 0.5
        spacing 30
       
        grid 2 2:
            add gallery.make_button(name="France Tryouts",unlocked="Cards/fr_small.png",locked="Cards/fr_small.png")
            add gallery.make_button(name="France Tryouts",unlocked="Cards/fr_small.png",locked="Cards/fr_small.png")
            add gallery.make_button(name="France Tryouts",unlocked="Cards/fr_small.png",locked="Cards/fr_small.png")
            add gallery.make_button(name="France Tryouts",unlocked="Cards/fr_small.png",locked="Cards/fr_small.png")
            spacing 15
        textbutton "Return" action Return()