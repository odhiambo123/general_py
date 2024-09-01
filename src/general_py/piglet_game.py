import pyglet

class PigletGame:
    def __init__(self):
        self.window = pyglet.window.Window()
        self.label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=self.window.width//2, y=self.window.height//2,
                          anchor_x='center', anchor_y='center')

    def run(self):
        @self.window.event
        def on_draw():
            self.window.clear()
            self.label.draw()

        pyglet.app.run()

if __name__ == '__main__':
    game = PigletGame()
    game.run()
# Compare this snippet from src/general_py/pygame_game.py:
# import pygame