### posiciona una cámara, administra los objetos y sus Graphics (VBO, VAO, ShaderProgram). Realiza transformaciones a los objetos que están en la escena y actualiza sus shaders. También actualiza viewport en on_resize.

from graphics import Graphics
import glm
import math 
from time import time

class Scene:
    def _init_(self, ctx, camera):
        self.ctx = ctx
        self.objects = []
        self.graphics = {}
        self.camera = camera
        self.model = glm.mat4(1)
        self.view = camera.get_view_matrix()
        self.projection = camera.get_perspective_matrix()
        self.time = 0

    def add_object(self, obj, shader_program=None):
        self.objects.append(obj)
        self.graphics[obj.name] = Graphics(self.ctx, shader_program, obj.vertices, obj.indices)

    def render(self):
        self.time += 0.01 
        for obj in self.objects: 
            obj.rotation.y += 0.57
            obj.rotation.x += 0.52
            obj.position.x += math.sin(self.time) * 0.01
            obj.position.y += math.cos(self.time) * 0.01
            obj.position.z += math.cos(self.time) * 0.01
            model = obj.get_model_matrix()
            mvp = self.projection * self.view * model
            self.graphics[obj.name].set_uniform('Mvp', mvp)
            self.graphics[obj.name].vao.render()

    def on_mouse_click(self, u, v):
        ray = self.camera.raycast(u, v)

        for obj in self.objects:
            if obj.check_hit(ray.origin, ray.direction):
                print(f"¡Golpeaste al objeto {obj.name}!")

    def update(self, dt):
        for obj in self.objects:
            if hasattr(obj, 'update'):
                obj.update()
    
    def on_resize(self, width, height):
        self.ctx.viewport = (0, 0, width, height)
        self.camera.projection = glm.perspective(glm.radians(45), width / height, 0.1, 100)