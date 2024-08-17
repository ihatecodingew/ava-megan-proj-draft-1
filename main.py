#01 - Kaia's Room
tiles.set_current_tilemap(tilemap("""KaiaBedroom"""))

#02 Kaia Sprite Setup
Kaia = sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . b 5 5 b . . .
    . . . . . . b b b b b b . . . .
    . . . . . b b 5 5 5 5 5 b . . .
    . b b b b b 5 5 5 5 5 5 5 b . .
    . b d 5 b 5 5 5 5 5 5 5 5 b . .
    . . b 5 5 b 5 d 1 f 5 d 4 f . .
    . . b d 5 5 b 1 f f 5 4 4 c . .
    b b d b 5 5 5 d f b 4 4 4 4 b .
    b d d c d 5 5 b 5 4 4 4 4 4 4 b
    c d d d c c b 5 5 5 5 5 5 5 b .
    c b d d d d d 5 5 5 5 5 5 5 b .
    . c d d d d d d 5 5 5 5 5 d b .
    . . c b d d d d d 5 5 5 b b . .
    . . . c c c c c c c c b b . . .
"""), SpriteKind.player)

#set scale (Kaia)
Kaia.set_scale(0.8, ScaleAnchor.MIDDLE)

#Kaia Run Animation
animation.run_image_animation(Kaia, [img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . b 5 5 b . . .
    . . . . . . b b b b b b . . . .
    . . . . . b b 5 5 5 5 5 b . . .
    . b b b b b 5 5 5 5 5 5 5 b . .
    . b d 5 b 5 5 5 5 5 5 5 5 b . .
    . . b 5 5 b 5 d 1 f 5 d 4 f . .
    . . b d 5 5 b 1 f f 5 4 4 c . .
    b b d b 5 5 5 d f b 4 4 4 4 b .
    b d d c d 5 5 b 5 4 4 4 4 4 4 b
    c d d d c c b 5 5 5 5 5 5 5 b .
    c b d d d d d 5 5 5 5 5 5 5 b .
    . c d d d d d d 5 5 5 5 5 d b .
    . . c b d d d d d 5 5 5 b b . .
    . . . c c c c c c c c b b . . .
"""),img("""
    . . . . . . . . . . b 5 b . . .
    . . . . . . . . . b 5 b . . . .
    . . . . . . b b b b b b . . . .
    . . . . . b b 5 5 5 5 5 b . . .
    . . . . b b 5 d 1 f 5 d 4 c . .
    . . . . b 5 5 1 f f d d 4 4 4 b
    . . . . b 5 5 d f b 4 4 4 4 b .
    . . . b d 5 5 5 5 4 4 4 4 b . .
    . . b d d 5 5 5 5 5 5 5 5 b . .
    . b d d d d 5 5 5 5 5 5 5 5 b .
    b d d d b b b 5 5 5 5 5 5 5 b .
    c d d b 5 5 d c 5 5 5 5 5 5 b .
    c b b d 5 d c d 5 5 5 5 5 5 b .
    . b 5 5 b c d d 5 5 5 5 5 d b .
    b b c c c d d d d 5 5 5 b b . .
    . . . c c c c c c c c b b . . .
"""),img("""
    . . . . . . . . . . b 5 b . . .
    . . . . . . . . . b 5 b . . . .
    . . . . . . b b b b b b . . . .
    . . . . . b b 5 5 5 5 5 b . . .
    . . . . b b 5 d 1 f 5 5 d f . .
    . . . . b 5 5 1 f f 5 d 4 c . .
    . . . . b 5 5 d f b d d 4 4 . .
    . b b b d 5 5 5 5 5 4 4 4 4 4 b
    b d d d b b d 5 5 4 4 4 4 4 b .
    b b d 5 5 5 b 5 5 5 5 5 5 b . .
    c d c 5 5 5 5 d 5 5 5 5 5 5 b .
    c b d c d 5 5 b 5 5 5 5 5 5 b .
    . c d d c c b d 5 5 5 5 5 d b .
    . . c b d d d d d 5 5 5 b b . .
    . . . c c c c c c c c b b . . .
    . . . . . . . . . . . . . . . .
"""),img("""
    . . . . . . . . . b 5 b . . . .
    . . . . . . . . . b 5 b . . . .
    . . . . . . b b b b b b . . . .
    . . . . . b b 5 5 5 5 5 b . . .
    . . . . b b 5 b c 5 5 d 4 c . .
    . b b b b 5 5 5 b f d d 4 4 4 b
    . b d 5 b 5 5 b c b 4 4 4 4 b .
    . . b 5 5 b 5 5 5 4 4 4 4 b . .
    . . b d 5 5 b 5 5 5 5 5 5 b . .
    . b d b 5 5 5 d 5 5 5 5 5 5 b .
    b d d c d 5 5 b 5 5 5 5 5 5 b .
    c d d d c c b 5 5 5 5 5 5 5 b .
    c b d d d d d 5 5 5 5 5 5 5 b .
    . c d d d d d d 5 5 5 5 5 d b .
    . . c b d d d d d 5 5 5 b b . .
    . . . c c c c c c c c b b . . .
""")], 500, True)

#Spawn Kaia on Bed
tiles.place_on_random_tile(Kaia, img("""
    6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6
    6 9 9 9 6 6 9 9 9 9 6 6 9 9 9 6
    6 9 9 6 6 9 9 c c 9 9 6 6 9 9 6
    6 9 6 6 9 9 c c 6 9 9 9 6 6 9 6
    6 6 6 9 9 9 9 c 6 6 9 9 9 6 6 6
    6 6 9 9 9 9 9 9 6 6 9 9 9 9 6 6
    6 9 9 9 6 6 6 6 9 6 9 9 c 9 9 6
    6 9 c 6 6 6 9 3 3 6 9 c c c 9 6
    6 9 c c c 9 6 9 9 9 6 6 6 c 9 6
    6 9 9 c 9 9 6 9 6 6 6 6 9 9 9 6
    6 6 9 9 9 9 6 6 9 9 9 9 9 9 6 6
    6 6 6 9 9 9 6 6 c 9 9 9 9 6 6 6
    6 9 6 6 9 9 9 6 c c 9 9 6 6 9 6
    6 9 9 6 6 9 9 c c 9 9 6 6 9 9 6
    6 9 9 9 6 6 9 9 9 9 6 6 9 9 9 6
    6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6
"""))

#Controlling Kaia
controller.move_sprite(Kaia)

#Camera follow Kaia
scene.camera_follow_sprite(Kaia)

#Changing the animation in relaton to the direction the sprite is looking at 
def on_update():
    if controller.left.is_pressed():
        animation.run_image_animation(Kaia, [img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . b 5 5 b . . . . . . . . .
            . . . . b b b b b b . . . . . .
            . . . b 5 5 5 5 5 b b . . . . .
            . . b 5 5 5 5 5 5 5 b b b b b .
            . . b 5 5 5 5 5 5 5 5 b 5 d b .
            . . f 4 d 5 f 1 d 5 b 5 5 b . .
            . . c 4 4 5 f f 1 b 5 5 d b . .
            . b 4 4 4 4 b f d 5 5 5 b d b b
            b 4 4 4 4 4 4 5 b 5 5 d c d d b
            . b 5 5 5 5 5 5 5 b c c d d d c
            . b 5 5 5 5 5 5 5 d d d d d b c
            . b d 5 5 5 5 5 d d d d d d c .
            . . b b 5 5 5 d d d d d b c . .
            . . . b b c c c c c c c c . . .
        """),img("""
            . . . . . . . . . . . . . . . .
            . . . b 5 b . . . . . . . . . .
            . . . . b 5 b . . . . . . . . .
            . . . . b b b b b b . . . . . .
            . . . b 5 5 5 5 5 b b . . . . .
            . . b 5 5 5 5 5 5 5 b b b b b .
            . . b 5 5 5 5 5 5 5 5 b 5 d b .
            . . f 4 d 5 f 1 d 5 b 5 5 b . .
            . . c 4 4 5 f f 1 b 5 5 d b . .
            b 4 4 4 4 4 b f d 5 5 5 b d b b
            . b 4 4 4 4 4 5 b 5 5 d c d d b
            . b 5 5 5 5 5 5 5 b c c d d d c
            . b 5 5 5 5 5 5 5 d d d d d b c
            . b d 5 5 5 5 5 d d d d d d c .
            . . b b 5 5 5 d d d d d b c . .
            . . . b b c c c c c c c c . . .
        """),img("""
            . . . b 5 b . . . . . . . . . .
            . . . . b 5 b . . . . . . . . .
            . . . . . c b . . . . . . . . .
            . . . . b b b b b b . . . . . .
            . . . b 5 5 5 5 5 b b . . . . .
            . . f d 5 5 f 1 d 5 b b . . . .
            . . c 4 d 5 f f 1 5 5 b . . . .
            . . 4 4 d d b f d 5 5 b . . . .
            b 4 4 4 4 4 5 5 5 d b b d d d b
            . b 4 4 4 4 4 5 5 b 5 5 5 d b b
            . . b 5 5 5 5 5 d 5 5 5 5 c d b
            . b 5 5 5 5 5 5 b 5 5 d c d d c
            . b 5 5 5 5 5 5 5 b c c d d b c
            . b d 5 5 5 5 5 d d d d d d c .
            . . b b 5 5 5 d d d d d b c . .
            . . . b b c c c c c c c c . . .
        """),img("""
            . . . b 5 b . . . . . . . . . .
            . . . . b 5 b . . . . . . . . .
            . . . . b b b b b b . . . . . .
            . . . b 5 5 5 5 5 b b . . . . .
            . . c 4 d 5 f 1 d 5 b b . . . .
            b 4 4 4 d d f f 1 5 5 b . . . .
            . b 4 4 4 4 b f d 5 5 b . . . .
            . . b 4 4 4 4 5 5 5 5 d b . . .
            . . b 5 5 5 5 5 5 5 5 d d b . .
            . b 5 5 5 5 5 5 5 5 d d d d b .
            . b 5 5 5 5 5 5 5 b b b d d d b
            . b 5 5 5 5 5 5 c d 5 5 b d d c
            . b 5 5 5 5 5 5 d c d 5 d b b c
            . b d 5 5 5 5 5 d d c b 5 5 b .
            . . b b 5 5 5 d d d d c c c b b
            . . . b b c c c c c c c c . . .
        """)], 500, True)
    elif controller.right.is_pressed():    
        animation.run_image_animation(Kaia, [img("""
            . . . . . . . . . . b 5 b . . .
            . . . . . . . . . b 5 b . . . .
            . . . . . . b b b b b b . . . .
            . . . . . b b 5 5 5 5 5 b . . .
            . . . . b b 5 d 1 f 5 d 4 c . .
            . . . . b 5 5 1 f f d d 4 4 4 b
            . . . . b 5 5 d f b 4 4 4 4 b .
            . . . b d 5 5 5 5 4 4 4 4 b . .
            . b b d d d 5 5 5 5 5 5 5 b . .
            b d d d b b b 5 5 5 5 5 5 5 b .
            c d d b 5 5 d c 5 5 5 5 5 5 b .
            c b b d 5 d c d 5 5 5 5 5 5 b .
            c b 5 5 b c d d 5 5 5 5 5 5 b .
            b b c c c d d d 5 5 5 5 5 d b .
            . . . . c c d d d 5 5 5 b b . .
            . . . . . . c c c c c b b . . .
        """),img("""
            . . . . . . . . . . b 5 b . . .
            . . . . . . . . . b 5 b . . . .
            . . . . . . b b b b b b . . . .
            . . . . . b b 5 5 5 5 5 b . . .
            . . . . b b 5 d 1 f 5 d 4 c . .
            . . . . b 5 5 1 f f d d 4 4 4 b
            . . . . b 5 5 d f b 4 4 4 4 b .
            . . . b d 5 5 5 5 4 4 4 4 b . .
            . b b d d d 5 5 5 5 5 5 5 b . .
            b d d d b b b 5 5 5 5 5 5 5 b .
            c d d b 5 5 d c 5 5 5 5 5 5 b .
            c b b d 5 d c d 5 5 5 5 5 5 b .
            c b 5 5 b c d d 5 5 5 5 5 5 b .
            b b c c c d d d 5 5 5 5 5 d b .
            . . . . c c d d d 5 5 5 b b . .
            . . . . . . c c c c c b b . . .
        """),img("""
            . . . . . . . . . . b 5 b . . .
            . . . . . . . . . b 5 b . . . .
            . . . . . . b b b b b b . . . .
            . . . . . b b 5 5 5 5 5 b . . .
            . . . . b b 5 d 1 f 5 5 d f . .
            . . . . b 5 5 1 f f 5 d 4 c . .
            . . . . b 5 5 d f b d d 4 4 . .
            . b b b d 5 5 5 5 5 4 4 4 4 4 b
            b d d d b b d 5 5 4 4 4 4 4 b .
            b b d 5 5 5 b 5 5 5 5 5 5 b . .
            c d c 5 5 5 5 d 5 5 5 5 5 5 b .
            c b d c d 5 5 b 5 5 5 5 5 5 b .
            . c d d c c b d 5 5 5 5 5 d b .
            . . c b d d d d d 5 5 5 b b . .
            . . . c c c c c c c c b b . . .
            . . . . . . . . . . . . . . . .
        """),img("""
            . . . . . . . . . . b 5 b . . .
            . . . . . . . . . b 5 b . . . .
            . . . . . . b b b b b b . . . .
            . . . . . b b 5 5 5 5 5 b . . .
            . . . . b b 5 d 1 f 5 5 d f . .
            . . . . b 5 5 1 f f 5 d 4 c . .
            . . . . b 5 5 d f b d d 4 4 . .
            . b b b d 5 5 5 5 5 4 4 4 4 4 b
            b d d d b b d 5 5 4 4 4 4 4 b .
            b b d 5 5 5 b 5 5 5 5 5 5 b . .
            c d c 5 5 5 5 d 5 5 5 5 5 5 b .
            c b d c d 5 5 b 5 5 5 5 5 5 b .
            . c d d c c b d 5 5 5 5 5 d b .
            . . c b d d d d d 5 5 5 b b . .
            . . . c c c c c c c c b b . . .
            . . . . . . . . . . . . . . . .
        """)], 500, True)
    elif controller.up.is_pressed():
        animation.run_image_animation(Kaia, [img("""
            . . . . . . . . . . b 5 b . . .
            . . . . . . . . . b 5 b . . . .
            . . . . . . b b b b b b . . . .
            . . . . . b b 5 5 5 5 5 b . . .
            . . . . b b 5 d 1 f 5 d 4 c . .
            . . . . b 5 5 1 f f d d 4 4 4 b
            . . . . b 5 5 d f b 4 4 4 4 b .
            . . . b d 5 5 5 5 4 4 4 4 b . .
            . . b d d 5 5 5 5 5 5 5 5 b . .
            . b d d d d 5 5 5 5 5 5 5 5 b .
            b d d d b b b 5 5 5 5 5 5 5 b .
            c d d b 5 5 d c 5 5 5 5 5 5 b .
            c b b d 5 d c d 5 5 5 5 5 5 b .
            . b 5 5 b c d d 5 5 5 5 5 d b .
            b b c c c d d d d 5 5 5 b b . .
            . . . c c c c c c c c b b . . .
        """),img("""
            . . . b 5 b . . . . . . . . . .
            . . . . b 5 b . . . . . . . . .
            . . . . b b b b b b . . . . . .
            . . . b 5 5 5 5 5 b b . . . . .
            . . f d 5 5 f 1 d 5 b b . . . .
            . . c 4 d 5 f f 1 5 5 b . . . .
            . . 4 4 d d b f d 5 5 b . . . .
            b 4 4 4 4 4 5 5 5 5 5 d b b b .
            . b 4 4 4 4 4 5 5 d b b d d d b
            . . b 5 5 5 5 5 5 b 5 5 5 d b b
            . b 5 5 5 5 5 5 d 5 5 5 5 c d c
            . b 5 5 5 5 5 5 b 5 5 d c d b c
            . b d 5 5 5 5 5 d b c c d d c .
            . . b b 5 5 5 d d d d d b c . .
            . . . b b c c c c c c c c . . .
            . . . . . . . . . . . . . . . .
        """),img("""
            . . . b 5 b . . . . . . . . . .
            . . . . b 5 b . . . . . . . . .
            . . . . b b b b b b . . . . . .
            . . . b 5 5 5 5 5 b b . . . . .
            . . c 4 d 5 f 1 d 5 b b . . . .
            b 4 4 4 d d f f 1 5 5 b . . . .
            . b 4 4 4 4 b f d 5 5 b . . . .
            . . b 4 4 4 4 5 5 5 5 d b . . .
            . . b 5 5 5 5 5 5 5 d d d b b .
            . b 5 5 5 5 5 5 5 b b b d d d b
            . b 5 5 5 5 5 5 c d 5 5 b d d c
            . b 5 5 5 5 5 5 d c d 5 d b b c
            . b 5 5 5 5 5 5 d d c b 5 5 b c
            . b d 5 5 5 5 5 d d d c c c b b
            . . b b 5 5 5 d d d c c . . . .
            . . . b b c c c c c . . . . . .
        """),img("""
            . . . . . . . . . . b 5 b . . .
            . . . . . . . . . b 5 b . . . .
            . . . . . . b b b b b b . . . .
            . . . . . b b 5 5 5 5 5 b . . .
            . . . . b b 5 d 1 f 5 5 d f . .
            . . . . b 5 5 1 f f 5 d 4 c . .
            . . . . b 5 5 d f b d d 4 4 . .
            . b b b d 5 5 5 5 5 4 4 4 4 4 b
            b d d d b b d 5 5 4 4 4 4 4 b .
            b b d 5 5 5 b 5 5 5 5 5 5 b . .
            c d c 5 5 5 5 d 5 5 5 5 5 5 b .
            c b d c d 5 5 b 5 5 5 5 5 5 b .
            . c d d c c b d 5 5 5 5 5 d b .
            . . c b d d d d d 5 5 5 b b . .
            . . . c c c c c c c c b b . . .
            . . . . . . . . . . . . . . . .
        """)], 500, True)
    elif controller.down.is_pressed():
        animation.run_image_animation(Kaia, [img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . b 5 b . . .
            . . . . . . . . . b 5 b . . . .
            . . . . . . b b b b b b . . . .
            . . . . . b b 5 5 5 5 5 b . . .
            . b b b b b 5 5 5 5 5 5 5 b . .
            . b d 5 b 5 5 5 5 5 5 5 5 b . .
            . . b 5 5 b 5 d 1 f 5 d 4 f . .
            . . b d 5 5 b 1 f f 5 4 4 c . .
            b b d b 5 5 5 d f b 4 4 4 4 4 b
            b d d c d 5 5 b 5 4 4 4 4 4 b .
            c d d d c c b 5 5 5 5 5 5 5 b .
            c b d d d d d 5 5 5 5 5 5 5 b .
            . c d d d d d d 5 5 5 5 5 d b .
            . . c b d d d d d 5 5 5 b b . .
            . . . c c c c c c c c b b . . .
        """),img("""
            . . . . . . . . . . . . . . . .
            . . . b 5 b . . . . . . . . . .
            . . . . b 5 b . . . . . . . . .
            . . . . b b b b b b . . . . . .
            . . . b 5 5 5 5 5 b b . . . . .
            . . b 5 5 5 5 5 5 5 b b b b b .
            . . b 5 5 5 5 5 5 5 5 b 5 d b .
            . . f 4 d 5 f 1 d 5 b 5 5 b . .
            . . c 4 4 5 f f 1 b 5 5 d b . .
            b 4 4 4 4 4 b f d 5 5 5 b d b b
            . b 4 4 4 4 4 5 b 5 5 d c d d b
            . b 5 5 5 5 5 5 5 b c c d d d c
            . b 5 5 5 5 5 5 5 d d d d d b c
            . b d 5 5 5 5 5 d d d d d d c .
            . . b b 5 5 5 d d d d d b c . .
            . . . b b c c c c c c c c . . .
        """),img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . b 5 b . . .
            . . . . . . . . . b 5 b . . . .
            . . . . . . b b b b b b . . . .
            . . . . . b b 5 5 5 5 5 b . . .
            . b b b b b 5 5 5 5 5 5 5 b . .
            . b d 5 b 5 5 5 5 5 5 5 5 b . .
            . . b 5 5 b 5 d 1 f 5 d 4 f . .
            . . b d 5 5 b 1 f f 5 4 4 c . .
            b b d b 5 5 5 d f b 4 4 4 4 4 b
            b d d c d 5 5 b 5 4 4 4 4 4 b .
            c d d d c c b 5 5 5 5 5 5 5 b .
            c b d d d d d 5 5 5 5 5 5 5 b .
            . c d d d d d d 5 5 5 5 5 d b .
            . . c b d d d d d 5 5 5 b b . .
            . . . c c c c c c c c b b . . .
        """),img("""
            . . . . . . . . . . . . . . . .
            . . . b 5 b . . . . . . . . . .
            . . . . b 5 b . . . . . . . . .
            . . . . b b b b b b . . . . . .
            . . . b 5 5 5 5 5 b b . . . . .
            . . b 5 5 5 5 5 5 5 b b b b b .
            . . b 5 5 5 5 5 5 5 5 b 5 d b .
            . . f 4 d 5 f 1 d 5 b 5 5 b . .
            . . c 4 4 5 f f 1 b 5 5 d b . .
            b 4 4 4 4 4 b f d 5 5 5 b d b b
            . b 4 4 4 4 4 5 b 5 5 d c d d b
            . b 5 5 5 5 5 5 5 b c c d d d c
            . b 5 5 5 5 5 5 5 d d d d d b c
            . b d 5 5 5 5 5 d d d d d d c .
            . . b b 5 5 5 d d d d d b c . .
            . . . b b c c c c c c c c . . .
        """)], 500, True)

#Set kaia life to 8
info.set_life(8)

def on_update2():
    game.on_update(on_update2)

##################### LEVEL 1 STARTS HERE ###########################

#03a when kaia touches wardrobe she gets transported
def on_overlap_tile(Kaia, location):
    #Show Hallway of Teonders
    tiles.set_current_tilemap(tilemap("""level0"""))
    #Spawn Kaia at Level 1 spawn point
    tiles.place_on_random_tile(Kaia, img("""
        6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6
        6 9 9 9 6 6 9 9 9 9 6 6 9 9 9 6
        6 9 9 6 6 9 9 c c 9 9 6 6 9 9 6
        6 9 6 6 9 9 c c 6 9 9 9 6 6 9 6
        6 6 6 9 9 9 9 c 6 6 9 9 9 6 6 6
        6 6 9 9 9 9 9 9 6 6 9 9 9 9 6 6
        6 9 9 9 6 6 6 6 9 6 9 9 c 9 9 6
        6 9 c 6 6 6 9 9 9 6 9 c c c 9 6
        6 9 c c c 9 6 9 9 9 6 6 6 c 9 6
        6 9 9 c 9 9 6 9 6 6 6 6 9 9 9 6
        6 6 9 9 9 9 6 6 9 9 9 9 9 9 6 6
        6 6 6 9 9 9 6 6 c 9 9 9 9 6 6 6
        6 9 6 6 9 9 9 6 c c 9 9 6 6 9 6
        6 9 9 6 6 9 9 c c 9 9 6 6 9 9 6
        6 9 9 9 6 6 9 9 9 9 6 6 9 9 9 6
        6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6
    """))
    #Set point for Ghouls/Cupcakes
    tiles.place_on_random_tile(None, img(""" """))
#Wardrobe tile creation
    scene.on_overlap_tile(SpriteKind.player, img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
"""), on_overlap_tile)


#04 Ghouls and Cupcakes
#04a Ghoul 01 creation
Ghoul1 = sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . b 5 5 b . . .
    . . . . . . b b b b b b . . . .
    . . . . . b b 5 5 5 5 5 b . . .
    . b b b b b 5 5 5 5 5 5 5 b . .
    . b d 5 b 5 5 5 5 5 5 5 5 b . .
    . . b 5 5 b 5 d 1 f 5 d 4 f . .
    . . b d 5 5 b 1 f f 5 4 4 c . .
    b b d b 5 5 5 d f b 4 4 4 4 b .
    b d d c d 5 5 b 5 4 4 4 4 4 4 b
    c d d d c c b 5 5 5 5 5 5 5 b .
    c b d d d d d 5 5 5 5 5 5 5 b .
    . c d d d d d d 5 5 5 5 5 d b .
    . . c b d d d d d 5 5 5 b b . .
    . . . c c c c c c c c b b . . .
"""), SpriteKind.enemy)
#set scale (Ghoul1)
Ghoul1.set_scale(0.8, ScaleAnchor.MIDDLE)
#Ghoul 01 Movement - NOT DONE YET
Ghoul1.set_position(0, 0)

#04b Ghoul 02 creation
Ghoul2 = sprites.create(img("""
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . b 5 5 b . . .
        . . . . . . b b b b b b . . . .
        . . . . . b b 5 5 5 5 5 b . . .
        . b b b b b 5 5 5 5 5 5 5 b . .
        . b d 5 b 5 5 5 5 5 5 5 5 b . .
        . . b 5 5 b 5 d 1 f 5 d 4 f . .
        . . b d 5 5 b 1 f f 5 4 4 c . .
        b b d b 5 5 5 d f b 4 4 4 4 b .
        b d d c d 5 5 b 5 4 4 4 4 4 4 b
        c d d d c c b 5 5 5 5 5 5 5 b .
        c b d d d d d 5 5 5 5 5 5 5 b .
        . c d d d d d d 5 5 5 5 5 d b .
        . . c b d d d d d 5 5 5 b b . .
        . . . c c c c c c c c b b . . .
"""), SpriteKind.enemy)
#set scale (Ghoul2)
Ghoul2.set_scale(0.8, ScaleAnchor.MIDDLE)
#Ghoul 02 Movement - NOT DONE YET
Ghoul2.set_position(0, 0)

#04c Ghoul 03 creation
Ghoul3 = sprites.create(img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . b 5 5 b . . .
            . . . . . . b b b b b b . . . .
            . . . . . b b 5 5 5 5 5 b . . .
            . b b b b b 5 5 5 5 5 5 5 b . .
            . b d 5 b 5 5 5 5 5 5 5 5 b . .
            . . b 5 5 b 5 d 1 f 5 d 4 f . .
            . . b d 5 5 b 1 f f 5 4 4 c . .
            b b d b 5 5 5 d f b 4 4 4 4 b .
            b d d c d 5 5 b 5 4 4 4 4 4 4 b
            c d d d c c b 5 5 5 5 5 5 5 b .
            c b d d d d d 5 5 5 5 5 5 5 b .
            . c d d d d d d 5 5 5 5 5 d b .
            . . c b d d d d d 5 5 5 b b . .
            . . . c c c c c c c c b b . . .
"""), SpriteKind.enemy)
#set scale (Ghoul3)
Ghoul3.set_scale(0.8, ScaleAnchor.MIDDLE)
#Ghoul 03 Movement - NOT DONE YET
Ghoul3.set_position(0, 0)

#04d Cupcake 01 creation
Cupcake1 = sprites.create(img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . b 5 5 b . . .
                . . . . . . b b b b b b . . . .
                . . . . . b b 5 5 5 5 5 b . . .
                . b b b b b 5 5 5 5 5 5 5 b . .
                . b d 5 b 5 5 5 5 5 5 5 5 b . .
                . . b 5 5 b 5 d 1 f 5 d 4 f . .
                . . b d 5 5 b 1 f f 5 4 4 c . .
                b b d b 5 5 5 d f b 4 4 4 4 b .
                b d d c d 5 5 b 5 4 4 4 4 4 4 b
                c d d d c c b 5 5 5 5 5 5 5 b .
                c b d d d d d 5 5 5 5 5 5 5 b .
                . c d d d d d d 5 5 5 5 5 d b .
                . . c b d d d d d 5 5 5 b b . .
                . . . c c c c c c c c b b . . .
"""), SpriteKind.enemy)
#set scale (Cupcake1)
Cupcake1.set_scale(0.8, ScaleAnchor.MIDDLE)
#Cupcake 01 Movement - NOT DONE YET
Cupcake1.set_position(0, 0)

#04e Cupcake 02 creation
Cupcake2 = sprites.create(img("""
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . b 5 5 b . . .
                    . . . . . . b b b b b b . . . .
                    . . . . . b b 5 5 5 5 5 b . . .
                    . b b b b b 5 5 5 5 5 5 5 b . .
                    . b d 5 b 5 5 5 5 5 5 5 5 b . .
                    . . b 5 5 b 5 d 1 f 5 d 4 f . .
                    . . b d 5 5 b 1 f f 5 4 4 c . .
                    b b d b 5 5 5 d f b 4 4 4 4 b .
                    b d d c d 5 5 b 5 4 4 4 4 4 4 b
                    c d d d c c b 5 5 5 5 5 5 5 b .
                    c b d d d d d 5 5 5 5 5 5 5 b .
                    . c d d d d d d 5 5 5 5 5 d b .
                    . . c b d d d d d 5 5 5 b b . .
                    . . . c c c c c c c c b b . . .
"""), SpriteKind.enemy)
#set scale (Cupcake2)
Cupcake2.set_scale(0.8, ScaleAnchor.MIDDLE)
#Cupcake 02 Movement - NOT DONE YET
Cupcake2.set_position(0, 0)

#04f Cupcake 03 creation
Cupcake3 = sprites.create(img("""
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . . . . . . . .
                        . . . . . . . . . b 5 5 b . . .
                        . . . . . . b b b b b b . . . .
                        . . . . . b b 5 5 5 5 5 b . . .
                        . b b b b b 5 5 5 5 5 5 5 b . .
                        . b d 5 b 5 5 5 5 5 5 5 5 b . .
                        . . b 5 5 b 5 d 1 f 5 d 4 f . .
                        . . b d 5 5 b 1 f f 5 4 4 c . .
                        b b d b 5 5 5 d f b 4 4 4 4 b .
                        b d d c d 5 5 b 5 4 4 4 4 4 4 b
                        c d d d c c b 5 5 5 5 5 5 5 b .
                        c b d d d d d 5 5 5 5 5 5 5 b .
                        . c d d d d d d 5 5 5 5 5 d b .
                        . . c b d d d d d 5 5 5 b b . .
                        . . . c c c c c c c c b b . . .
    """), SpriteKind.enemy)
#set scale (Cupcake3)
Cupcake3.set_scale(0.8, ScaleAnchor.MIDDLE)
#Cupcake 03 Movement - NOT DONE YET
Cupcake3.set_position(0, 0)

#05 Kaia overlapping w/ stuff

#05a When Kaia Touches the Orb, she goes back to the room (End Game)
def on_overlap_tile2(sprite, location):
    #Show Bedroom
    tiles.set_current_tilemap(tilemap(""" """))
    #Spawn Kaia onto Bed
    tiles.place_on_random_tile(Kaia, img(""" """))
    #End Game Text
    #Magical Orb Creation
    scene.on_overlap_tile(SpriteKind.player, img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
"""), on_overlap_tile2)

#05b When Kaia touches the Enemies
#Ghoul 01
def on_overlap(Kaia, Ghoul1):
    #Reduce life by 1
    info.change_life_by(-1)
    #Go Back to spawn point
    tiles.place_on_random_tile(Kaia, img(""" """))
    #Show lose life text - DO THIS LATER
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_overlap)

#Ghoul 02
def on_overlap2(Kaia, Ghoul2):
    #Reduce life by 1
    info.change_life_by(-1)
    #Go Back to spawn point
    tiles.place_on_random_tile(Kaia, img(""" """))
    #Show lose life text - DO THIS LATER
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_overlap2)

#Ghoul 03
def on_overlap3(Kaia, Ghoul3):
    #Reduce life by 1
    info.change_life_by(-1)
    #Go Back to spawn point
    tiles.place_on_random_tile(Kaia, img(""" """))
    #Show lose life text - DO THIS LATER
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_overlap3)

#Cupcake 01
def on_overlap4(Kaia, Cupcake1):
    #Reduce life by 1
    info.change_life_by(-1)
    #Go Back to spawn point
    tiles.place_on_random_tile(Kaia, img(""" """))
    #Show lose life text - DO THIS LATER
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_overlap4)

#Cupcake 02
def on_overlap5(Kaia, Cupcake2):
    #Reduce life by 1
    info.change_life_by(-1)
    #Go Back to spawn point
    tiles.place_on_random_tile(Kaia, img(""" """))
    #Show lose life text - DO THIS LATER
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_overlap5)

#Cupcake 03
def on_overlap6(Kaia, Cupcake3):
    #Reduce life by 1
    info.change_life_by(-1)
    #Go Back to spawn point
    tiles.place_on_random_tile(Kaia, img(""" """))
    #Show lose life text - DO THIS LATER
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_overlap6)

########################## LEVEL 2 STARTS HERE #################################

#06a when kaia touches staircase01 she gets transported
def on_overlap_tile3(Kaia, location):
    #Show Hallway of Teonders
    tiles.set_current_tilemap(tilemap(""" """))
    #Spawn Kaia at Level 1 spawn point
    tiles.place_on_random_tile(Kaia, img("""
    6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6
    6 9 9 9 6 6 9 9 9 9 6 6 9 9 9 6
    6 9 9 6 6 9 9 c c 9 9 6 6 9 9 6
    6 9 6 6 9 9 c c 6 9 9 9 6 6 9 6
    6 6 6 9 9 9 9 c 6 6 9 9 9 6 6 6
    6 6 9 9 9 9 9 9 6 6 9 9 9 9 6 6
    6 9 9 9 6 6 6 6 9 6 9 9 c 9 9 6
    6 9 c 6 6 6 9 9 9 6 9 c c c 9 6
    6 9 c c c 9 6 9 9 9 6 6 6 c 9 6
    6 9 9 c 9 9 6 9 6 6 6 6 9 9 9 6
    6 6 9 9 9 9 6 6 9 9 9 9 9 9 6 6
    6 6 6 9 9 9 6 6 c 9 9 9 9 6 6 6
    6 9 6 6 9 9 9 6 c c 9 9 6 6 9 6
    6 9 9 6 6 9 9 c c 9 9 6 6 9 9 6
    6 9 9 9 6 6 9 9 9 9 6 6 9 9 9 6
    6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6
"""))
    #Show Hallway of Gloops and Gloom
    tiles.set_current_tilemap(tilemap(""" """))
    #Spawn Kaia at Level 2 spawn point
    tiles.place_on_random_tile(Kaia, img("""
    6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6
    6 9 9 9 6 6 9 9 9 9 6 6 9 9 9 6
    6 9 9 6 6 9 9 c c 9 9 6 6 9 9 6
    6 9 6 6 9 9 c c 6 9 9 9 6 6 9 6
    6 6 6 9 9 9 9 c 6 6 9 9 9 6 6 6
    6 6 9 9 9 9 9 9 6 6 9 9 9 9 6 6
    6 9 9 9 6 6 6 6 9 6 9 9 c 9 9 6
    6 9 c 6 6 6 9 9 9 6 9 c c c 9 6
    6 9 c c c 9 6 9 9 9 6 6 6 c 9 6
    6 9 9 c 9 9 6 9 6 6 6 6 9 9 9 6
    6 6 9 9 9 9 6 6 9 9 9 9 9 9 6 6
    6 6 6 9 9 9 6 6 c 9 9 9 9 6 6 6
    6 9 6 6 9 9 9 6 c c 9 9 6 6 9 6
    6 9 9 6 6 9 9 c c 9 9 6 6 9 9 6
    6 9 9 9 6 6 9 9 9 9 6 6 9 9 9 6
    6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6
    """))
    #Set point for Ghosts
    tiles.place_on_random_tile(None, img(""" """))
    #Set points for SmileyStars
scene.on_overlap_tile(SpriteKind.player, img(""" """), on_overlap_tile3)

#07 Ghosts
#07a Ghoul 01 creation
Ghost1 = sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . b 5 5 b . . .
    . . . . . . b b b b b b . . . .
    . . . . . b b 5 5 5 5 5 b . . .
    . b b b b b 5 5 5 5 5 5 5 b . .
    . b d 5 b 5 5 5 5 5 5 5 5 b . .
    . . b 5 5 b 5 d 1 f 5 d 4 f . .
    . . b d 5 5 b 1 f f 5 4 4 c . .
    b b d b 5 5 5 d f b 4 4 4 4 b .
    b d d c d 5 5 b 5 4 4 4 4 4 4 b
    c d d d c c b 5 5 5 5 5 5 5 b .
    c b d d d d d 5 5 5 5 5 5 5 b .
    . c d d d d d d 5 5 5 5 5 d b .
    . . c b d d d d d 5 5 5 b b . .
    . . . c c c c c c c c b b . . .
"""), SpriteKind.enemy)
#set scale (Ghost1)
Ghost1.set_scale(0.8, ScaleAnchor.MIDDLE)
#Ghost01 Movement
Ghost1.follow(Kaia)

#07b Ghost 02 creation
Ghost2 = sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . b 5 5 b . . .
    . . . . . . b b b b b b . . . .
    . . . . . b b 5 5 5 5 5 b . . .
    . b b b b b 5 5 5 5 5 5 5 b . .
    . b d 5 b 5 5 5 5 5 5 5 5 b . .
    . . b 5 5 b 5 d 1 f 5 d 4 f . .
    . . b d 5 5 b 1 f f 5 4 4 c . .
    b b d b 5 5 5 d f b 4 4 4 4 b .
    b d d c d 5 5 b 5 4 4 4 4 4 4 b
    c d d d c c b 5 5 5 5 5 5 5 b .
    c b d d d d d 5 5 5 5 5 5 5 b .
    . c d d d d d d 5 5 5 5 5 d b .
    . . c b d d d d d 5 5 5 b b . .
    . . . c c c c c c c c b b . . .
"""), SpriteKind.enemy)
#set scale (Ghost2)
Ghost2.set_scale(0.8, ScaleAnchor.MIDDLE)
#Ghost02 Movement
Ghost2.follow(Kaia)

#7c Ghost 03 Creation
Ghost3 = sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . b 5 5 b . . .
    . . . . . . b b b b b b . . . .
    . . . . . b b 5 5 5 5 5 b . . .
    . b b b b b 5 5 5 5 5 5 5 b . .
    . b d 5 b 5 5 5 5 5 5 5 5 b . .
    . . b 5 5 b 5 d 1 f 5 d 4 f . .
    . . b d 5 5 b 1 f f 5 4 4 c . .
    b b d b 5 5 5 d f b 4 4 4 4 b .
    b d d c d 5 5 b 5 4 4 4 4 4 4 b
    c d d d c c b 5 5 5 5 5 5 5 b .
    c b d d d d d 5 5 5 5 5 5 5 b .
    . c d d d d d d 5 5 5 5 5 d b .
    . . c b d d d d d 5 5 5 b b . .
    . . . c c c c c c c c b b . . .
"""), SpriteKind.enemy)
#set scale (Ghost3)
Ghost3.set_scale(0.8, ScaleAnchor.MIDDLE)
#Ghost03 Movement
Ghost3.follow(Kaia)

#7d Ghost 04 Creation
Ghost4 = sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . b 5 5 b . . .
    . . . . . . b b b b b b . . . .
    . . . . . b b 5 5 5 5 5 b . . .
    . b b b b b 5 5 5 5 5 5 5 b . .
    . b d 5 b 5 5 5 5 5 5 5 5 b . .
    . . b 5 5 b 5 d 1 f 5 d 4 f . .
    . . b d 5 5 b 1 f f 5 4 4 c . .
    b b d b 5 5 5 d f b 4 4 4 4 b .
    b d d c d 5 5 b 5 4 4 4 4 4 4 b
    c d d d c c b 5 5 5 5 5 5 5 b .
    c b d d d d d 5 5 5 5 5 5 5 b .
    . c d d d d d d 5 5 5 5 5 d b .
    . . c b d d d d d 5 5 5 b b . .
    . . . c c c c c c c c b b . . .
"""), SpriteKind.enemy)
#set scale (Ghost4)
Ghost4.set_scale(0.8, ScaleAnchor.MIDDLE)
#Ghost04 Movement
Ghost4.follow(Kaia)

#7e SmileyStar01 Creation
SmileyStar1 = sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . b 5 5 b . . .
    . . . . . . b b b b b b . . . .
    . . . . . b b 5 5 5 5 5 b . . .
    . b b b b b 5 5 5 5 5 5 5 b . .
    . b d 5 b 5 5 5 5 5 5 5 5 b . .
    . . b 5 5 b 5 d 1 f 5 d 4 f . .
    . . b d 5 5 b 1 f f 5 4 4 c . .
    b b d b 5 5 5 d f b 4 4 4 4 b .
    b d d c d 5 5 b 5 4 4 4 4 4 4 b
    c d d d c c b 5 5 5 5 5 5 5 b .
    c b d d d d d 5 5 5 5 5 5 5 b .
    . c d d d d d d 5 5 5 5 5 d b .
    . . c b d d d d d 5 5 5 b b . .
    . . . c c c c c c c c b b . . .
"""), SpriteKind.player)
#set scale (Ghost4)
SmileyStar1.set_scale(0.8, ScaleAnchor.MIDDLE)

#7f SmileyStar02 Creation
SmileyStar2 = sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . b 5 5 b . . .
    . . . . . . b b b b b b . . . .
    . . . . . b b 5 5 5 5 5 b . . .
    . b b b b b 5 5 5 5 5 5 5 b . .
    . b d 5 b 5 5 5 5 5 5 5 5 b . .
    . . b 5 5 b 5 d 1 f 5 d 4 f . .
    . . b d 5 5 b 1 f f 5 4 4 c . .
    b b d b 5 5 5 d f b 4 4 4 4 b .
    b d d c d 5 5 b 5 4 4 4 4 4 4 b
    c d d d c c b 5 5 5 5 5 5 5 b .
    c b d d d d d 5 5 5 5 5 5 5 b .
    . c d d d d d d 5 5 5 5 5 d b .
    . . c b d d d d d 5 5 5 b b . .
    . . . c c c c c c c c b b . . .
"""), SpriteKind.player)
#set scale (Ghost4)
SmileyStar2.set_scale(0.8, ScaleAnchor.MIDDLE)

#7g SmileyStar03 Creation
SmileyStar3 = sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . b 5 5 b . . .
    . . . . . . b b b b b b . . . .
    . . . . . b b 5 5 5 5 5 b . . .
    . b b b b b 5 5 5 5 5 5 5 b . .
    . b d 5 b 5 5 5 5 5 5 5 5 b . .
    . . b 5 5 b 5 d 1 f 5 d 4 f . .
    . . b d 5 5 b 1 f f 5 4 4 c . .
    b b d b 5 5 5 d f b 4 4 4 4 b .
    b d d c d 5 5 b 5 4 4 4 4 4 4 b
    c d d d c c b 5 5 5 5 5 5 5 b .
    c b d d d d d 5 5 5 5 5 5 5 b .
    . c d d d d d d 5 5 5 5 5 d b .
    . . c b d d d d d 5 5 5 b b . .
    . . . c c c c c c c c b b . . .
"""), SpriteKind.player)
#set scale (Ghost4)
SmileyStar3.set_scale(0.8, ScaleAnchor.MIDDLE)

#08 Kaia overlapping w/ stuff

#08a When Kaia Touches the smiling stars, she adds one life
#Smiley Star 01
def on_overlap7(Kaia, SmileyStar1):
    info.change_life_by(1)
    sprites.destroy(SmileyStar1)
sprites.on_overlap(SpriteKind.player, SpriteKind.player, on_overlap7)
#Smiley Star 02
def on_overlap8(Kaia, SmileyStar2):
    info.change_life_by(1)
    sprites.destroy(SmileyStar2)
sprites.on_overlap(SpriteKind.player, SpriteKind.player, on_overlap8)
#Smiley Star 03
def on_overlap9(Kaia, SmileyStar3):
    info.change_life_by(1)
    sprites.destroy(SmileyStar3)
sprites.on_overlap(SpriteKind.player, SpriteKind.player, on_overlap9)

#05b When Kaia touches the Enemies
#Ghost 01
def on_overlap10(Kaia, Ghost1):
    #Reduce life by 1
    info.change_life_by(-1)
    #Go Back to spawn point
    tiles.place_on_random_tile(Kaia, img(""" """))
    #Show lose life text - DO THIS LATER
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_overlap10)

#Ghost 02
def on_overlap11(Kaia, Ghost2):
    #Reduce life by 1
    info.change_life_by(-1)
    #Go Back to spawn point
    tiles.place_on_random_tile(Kaia, img(""" """))
    #Show lose life text - DO THIS LATER
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_overlap11)

#Ghost 03
def on_overlap12(Kaia, Ghost3):
    #Reduce life by 1
    info.change_life_by(-1)
    #Go Back to spawn point
    tiles.place_on_random_tile(Kaia, img(""" """))
    #Show lose life text - DO THIS LATER
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_overlap12)

#Ghost 04
def on_overlap13(Kaia, Ghost4):
    #Reduce life by 1
    info.change_life_by(-1)
    #Go Back to spawn point
    tiles.place_on_random_tile(Kaia, img(""" """))
    #Show lose life text - DO THIS LATER
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_overlap13)

################### LEVEL 3 STARTS HERE######################################

################### LEVEL 4 STARTS HERE ###########################################


######################### LEVEL -3 STARTS HERE ##########################################


######################### LEVEL -2 STARTS HERE ##########################################


######################### LEVEL -1 STARTS HERE ###########################################


######################### HOME SWEET HOME ##################################################