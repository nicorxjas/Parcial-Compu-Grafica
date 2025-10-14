### crea el VBO, el IBO y VAO con el ShaderProgram y el format de atributos (en este caso “3f 3f”, “in_pos”, “in_color”). Implementa el método render() para renderizar el VAO en el context, según los valores y funciones indicados en el ShaderProgram.

class Graphics:
    def __init__(self, ctx, shader_program, vertices, indices):
        self.ctx = ctx
        self.shader_program = shader_program
        # VBO, IBO Y VAO
        # VBO: Vertex Buffer Object: almacena los datos de los vértices
        # IBO: Index Buffer Object: almacena los índices para dibujar los vértices
        # VAO: Vertex Array Object: combina VBO e IBO y define el formato de los datos
        self.vbo = ctx.buffer(vertices.tobytes())
        self.ibo = ctx.buffer(indices.tobytes())
        self.vao = ctx.vertex_array(shader_program.prog, [
            (self.vbo, '3f 3f', 'in_pos', 'in_color')
        ], self.ibo)

    def set_shader(self, shader_program):
        self.shader_program = shader_program.prog
    
    def set_uniform(self, name, value):
        self.shader_program.set_uniform(name, value)