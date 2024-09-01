from ursina import *

app = Ursina()

cube = Entity(model='cube', color=hsv(300,1,1), scale=2, collider='box')

def spin():
    cube.animate('rotation_y', cube.rotation_y+360, duration=2, curve=curve.in_out_expo)

def update():
    if held_keys['a']:
        cube.x -= 1 * time.dt
    if held_keys['d']:
        cube.x += 1 * time.dt
    if held_keys['w']:
        cube.y += 1 * time.dt
    if held_keys['s']:
        cube.y -= 1 * time.dt
    if held_keys['q']:
        cube.z -= 1 * time.dt
    if held_keys['e']:
        cube.z += 1 * time.dt

def input(key):
    if key == 'space':
        spin()



cube.on_click = spin
EditorCamera()  # add camera controls for orbiting and moving the camera


app.run()


