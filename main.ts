// 01 - Kaia's Room
tiles.setCurrentTilemap(tilemap`KaiaBedroom`)
// 02 Kaia Sprite Setup
let Kaia = sprites.create(img`
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
`, SpriteKind.Player)
// set scale (Kaia)
Kaia.setScale(0.8, ScaleAnchor.Middle)
// Kaia Run Animation
animation.runImageAnimation(Kaia, [img`
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
`, img`
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
`, img`
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
`, img`
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
`], 500, true)
// Spawn Kaia on Bed
tiles.placeOnRandomTile(Kaia, img`
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
`)
// Controlling Kaia
controller.moveSprite(Kaia)
// Camera follow Kaia
scene.cameraFollowSprite(Kaia)
// Changing the animation in relaton to the direction the sprite is looking at 
function on_update() {
    if (controller.left.isPressed()) {
        animation.runImageAnimation(Kaia, [img`
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
        `, img`
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
        `, img`
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
        `, img`
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
        `], 500, true)
    } else if (controller.right.isPressed()) {
        animation.runImageAnimation(Kaia, [img`
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
        `, img`
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
        `, img`
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
        `, img`
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
        `], 500, true)
    } else if (controller.up.isPressed()) {
        animation.runImageAnimation(Kaia, [img`
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
        `, img`
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
        `, img`
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
        `, img`
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
        `], 500, true)
    } else if (controller.down.isPressed()) {
        animation.runImageAnimation(Kaia, [img`
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
        `, img`
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
        `, img`
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
        `, img`
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
        `], 500, true)
    }
    
}

// Set kaia life to 8
info.setLife(8)
// #################### LEVEL 1 STARTS HERE ###########################
// 03a when kaia touches wardrobe she gets transported
// 04 Ghouls and Cupcakes
// 04a Ghoul 01 creation
let Ghoul1 = sprites.create(img`
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
`, SpriteKind.Enemy)
// set scale (Ghoul1)
Ghoul1.setScale(0.8, ScaleAnchor.Middle)
// Ghoul 01 Movement - NOT DONE YET
Ghoul1.setPosition(0, 0)
// 04b Ghoul 02 creation
let Ghoul2 = sprites.create(img`
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
`, SpriteKind.Enemy)
// set scale (Ghoul2)
Ghoul2.setScale(0.8, ScaleAnchor.Middle)
// Ghoul 02 Movement - NOT DONE YET
Ghoul2.setPosition(0, 0)
// 04c Ghoul 03 creation
let Ghoul3 = sprites.create(img`
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
`, SpriteKind.Enemy)
// set scale (Ghoul3)
Ghoul3.setScale(0.8, ScaleAnchor.Middle)
// Ghoul 03 Movement - NOT DONE YET
Ghoul3.setPosition(0, 0)
// 04d Cupcake 01 creation
let Cupcake1 = sprites.create(img`
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
`, SpriteKind.Enemy)
// set scale (Cupcake1)
Cupcake1.setScale(0.8, ScaleAnchor.Middle)
// Cupcake 01 Movement - NOT DONE YET
Cupcake1.setPosition(0, 0)
// 04e Cupcake 02 creation
let Cupcake2 = sprites.create(img`
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
`, SpriteKind.Enemy)
// set scale (Cupcake2)
Cupcake2.setScale(0.8, ScaleAnchor.Middle)
// Cupcake 02 Movement - NOT DONE YET
Cupcake2.setPosition(0, 0)
// 04f Cupcake 03 creation
let Cupcake3 = sprites.create(img`
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
    `, SpriteKind.Enemy)
// set scale (Cupcake3)
Cupcake3.setScale(0.8, ScaleAnchor.Middle)
// Cupcake 03 Movement - NOT DONE YET
Cupcake3.setPosition(0, 0)
// 05 Kaia overlapping w/ stuff
// 05a When Kaia Touches the Orb, she goes back to the room (End Game)
// 05b When Kaia touches the Enemies
// Ghoul 01
// Show lose life text - DO THIS LATER
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function on_overlap(Kaia: Sprite, Ghoul1: Sprite) {
    // Reduce life by 1
    info.changeLifeBy(-1)
    // Go Back to spawn point
    tiles.placeOnRandomTile(Kaia, img` `)
})
// Ghoul 02
// Show lose life text - DO THIS LATER
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function on_overlap2(Kaia: Sprite, Ghoul2: Sprite) {
    // Reduce life by 1
    info.changeLifeBy(-1)
    // Go Back to spawn point
    tiles.placeOnRandomTile(Kaia, img` `)
})
// Ghoul 03
// Show lose life text - DO THIS LATER
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function on_overlap3(Kaia: Sprite, Ghoul3: Sprite) {
    // Reduce life by 1
    info.changeLifeBy(-1)
    // Go Back to spawn point
    tiles.placeOnRandomTile(Kaia, img` `)
})
// Cupcake 01
// Show lose life text - DO THIS LATER
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function on_overlap4(Kaia: Sprite, Cupcake1: Sprite) {
    // Reduce life by 1
    info.changeLifeBy(-1)
    // Go Back to spawn point
    tiles.placeOnRandomTile(Kaia, img` `)
})
// Cupcake 02
// Show lose life text - DO THIS LATER
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function on_overlap5(Kaia: Sprite, Cupcake2: Sprite) {
    // Reduce life by 1
    info.changeLifeBy(-1)
    // Go Back to spawn point
    tiles.placeOnRandomTile(Kaia, img` `)
})
// Cupcake 03
// Show lose life text - DO THIS LATER
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function on_overlap6(Kaia: Sprite, Cupcake3: Sprite) {
    // Reduce life by 1
    info.changeLifeBy(-1)
    // Go Back to spawn point
    tiles.placeOnRandomTile(Kaia, img` `)
})
// ######################### LEVEL 2 STARTS HERE #################################
// 06a when kaia touches staircase01 she gets transported
// Set points for SmileyStars
scene.onOverlapTile(SpriteKind.Player, img` `, function on_overlap_tile3(Kaia: Sprite, location: tiles.Location) {
    // Show Hallway of Teonders
    tiles.setCurrentTilemap(tilemap` `)
    // Spawn Kaia at Level 1 spawn point
    tiles.placeOnRandomTile(Kaia, img`
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
`)
    // Show Hallway of Gloops and Gloom
    tiles.setCurrentTilemap(tilemap` `)
    // Spawn Kaia at Level 2 spawn point
    tiles.placeOnRandomTile(Kaia, img`
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
    `)
    // Set point for Ghosts
    tiles.placeOnRandomTile(null, img` `)
})
// 07 Ghosts
// 07a Ghoul 01 creation
let Ghost1 = sprites.create(img`
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
`, SpriteKind.Enemy)
// set scale (Ghost1)
Ghost1.setScale(0.8, ScaleAnchor.Middle)
// Ghost01 Movement
Ghost1.follow(Kaia)
// 07b Ghost 02 creation
let Ghost2 = sprites.create(img`
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
`, SpriteKind.Enemy)
// set scale (Ghost2)
Ghost2.setScale(0.8, ScaleAnchor.Middle)
// Ghost02 Movement
Ghost2.follow(Kaia)
// 7c Ghost 03 Creation
let Ghost3 = sprites.create(img`
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
`, SpriteKind.Enemy)
// set scale (Ghost3)
Ghost3.setScale(0.8, ScaleAnchor.Middle)
// Ghost03 Movement
Ghost3.follow(Kaia)
// 7d Ghost 04 Creation
let Ghost4 = sprites.create(img`
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
`, SpriteKind.Enemy)
// set scale (Ghost4)
Ghost4.setScale(0.8, ScaleAnchor.Middle)
// Ghost04 Movement
Ghost4.follow(Kaia)
// 7e SmileyStar01 Creation
let SmileyStar1 = sprites.create(img`
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
`, SpriteKind.Player)
// set scale (Ghost4)
SmileyStar1.setScale(0.8, ScaleAnchor.Middle)
// 7f SmileyStar02 Creation
let SmileyStar2 = sprites.create(img`
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
`, SpriteKind.Player)
// set scale (Ghost4)
SmileyStar2.setScale(0.8, ScaleAnchor.Middle)
// 7g SmileyStar03 Creation
let SmileyStar3 = sprites.create(img`
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
`, SpriteKind.Player)
// set scale (Ghost4)
SmileyStar3.setScale(0.8, ScaleAnchor.Middle)
// 08 Kaia overlapping w/ stuff
// 08a When Kaia Touches the smiling stars, she adds one life
// Smiley Star 01
sprites.onOverlap(SpriteKind.Player, SpriteKind.Player, function on_overlap7(Kaia: Sprite, SmileyStar1: Sprite) {
    info.changeLifeBy(1)
    sprites.destroy(SmileyStar1)
})
// Smiley Star 02
sprites.onOverlap(SpriteKind.Player, SpriteKind.Player, function on_overlap8(Kaia: Sprite, SmileyStar2: Sprite) {
    info.changeLifeBy(1)
    sprites.destroy(SmileyStar2)
})
// Smiley Star 03
sprites.onOverlap(SpriteKind.Player, SpriteKind.Player, function on_overlap9(Kaia: Sprite, SmileyStar3: Sprite) {
    info.changeLifeBy(1)
    sprites.destroy(SmileyStar3)
})
// 05b When Kaia touches the Enemies
// Ghost 01
// Show lose life text - DO THIS LATER
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function on_overlap10(Kaia: Sprite, Ghost1: Sprite) {
    // Reduce life by 1
    info.changeLifeBy(-1)
    // Go Back to spawn point
    tiles.placeOnRandomTile(Kaia, img` `)
})
// Ghost 02
// Show lose life text - DO THIS LATER
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function on_overlap11(Kaia: Sprite, Ghost2: Sprite) {
    // Reduce life by 1
    info.changeLifeBy(-1)
    // Go Back to spawn point
    tiles.placeOnRandomTile(Kaia, img` `)
})
// Ghost 03
// Show lose life text - DO THIS LATER
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function on_overlap12(Kaia: Sprite, Ghost3: Sprite) {
    // Reduce life by 1
    info.changeLifeBy(-1)
    // Go Back to spawn point
    tiles.placeOnRandomTile(Kaia, img` `)
})
// Ghost 04
// Show lose life text - DO THIS LATER
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function on_overlap13(Kaia: Sprite, Ghost4: Sprite) {
    // Reduce life by 1
    info.changeLifeBy(-1)
    // Go Back to spawn point
    tiles.placeOnRandomTile(Kaia, img` `)
})
