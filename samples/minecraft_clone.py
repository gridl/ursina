from pandaeditor import *


class MinecraftClone(Entity):

    def __init__(self):

        super().__init__()
        self.name = 'minecraft_clone'

        for z in range(32):
            for x in range(32):
                for y in range(1):
                    voxel = Voxel()
                    voxel.parent = self
                    voxel.position = (x, y, z)

        player = FirstPersonController()
        player.parent = self


class Voxel(Entity):

    def __init__(self):
        super().__init__()
        self.name = 'voxel'
        self.model = 'cube'
        self.origin = (0, .5, 0)
        self.collider = 'box'
        self.texture = 'white_cube'
        self.color = color.color(0, 0, random.uniform(.9, 1.0))


    def input(self, key):
        # if not scene.editor or scene.editor.enabled:
        #     return
        if self.hovered:
            if key == 'left mouse down' and self.hovered:
                voxel = Voxel()
                voxel.parent = self.parent
                voxel.position = self.position + mouse.normal

            if key == 'right mouse down':
                destroy(self)


class FirstPersonController(Entity):

    def __init__(self):
        super().__init__()
        self.speed = .1

        cursor = Panel()
        cursor.color = color.light_gray
        cursor.scale *= .008
        cursor.rotation_z = 45
        if not scene.editor:
            self.start()


    def start(self):
        self.position = (0, 2, 1)
        camera.parent = self
        camera.position = (0,0,0)
        camera.rotation = (0,0,0)
        camera.fov = 90
        mouse.locked = True


    def update(self, dt):
        # print(self.left)
        self.position += self.right * held_keys['d'] * self.speed
        self.position += self.forward * held_keys['w'] * self.speed
        self.position += self.left * held_keys['a'] * self.speed
        self.position += self.back * held_keys['s'] * self.speed
        self.position += self.down * held_keys['q'] * self.speed
        self.position += self.up * held_keys['e'] * self.speed

        self.rotation_y += mouse.velocity[0] * 20
        camera.rotation_x -= mouse.velocity[1] * 20
        camera.rotation_x = clamp(camera.rotation_x, -90, 90)

if __name__ == '__main__':
    app = main.PandaEditor()
    # load_scene('minecraft_clone')
    s = MinecraftClone()
    app.run()