import glm 

class Hit:
    def __init__(self, position=(0,0,0), scale=(1,1,1)):
        self.__position = glm.vec3(*position)
        self.__scale = glm.vec3(*scale)

    @property
    def position(self):
        return self.__position
    
    @property
    def scale(self):
        return self.__scale
    
    def check_hit(self, origin, direction):
        raise NotImplementedError("Subclasses must implement this method")
    
class HitBox(Hit):
    def __init__(self, position=(0,0,0), scale=(1,1,1)):
        super().__init__(position, scale)

    def check_hit(self, origin, direction):
        origin = glm.vec3(origin)
        direction = glm.normalize(glm.vec3(direction))

        min_bounds = self.position - self.scale 
        max_bounds = self.position + self.scale

        tmin = (min_bounds - origin) / direction 
        tmax = (max_bounds - origin) / direction 

        t1 = glm.min(tmin, tmax)
        t2 = glm.max(tmin, tmax)

        t_near = max(t1.x, t1.y, t1.z)
        t_far = min(t2.x, t2.y, t2.z)

        return t_near <= t_far and t_far >= 0