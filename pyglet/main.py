import pyglet

animation = pyglet.image.load_animation('zero.gif')
sprite = pyglet.sprite.Sprite(animation)

zWidth = sprite.width
zHeight = sprite.height

window = pyglet.window.Window(width=zWidth, height=zHeight)

r, g, b, alpha = 0.5, 0.5, 0.8, 0.5

pyglet.gl.glClearColor(r, g, b, alpha)


@window.event
def on_draw():
    window.clear()
    sprite.draw()


pyglet.app.run()
