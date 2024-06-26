import math
class Point:
  definition: str = "Abstract geometric entity representing a location in space."

  def __init__(self, x: float = 0, y: float = 0):
    self.__x = x
    self.__y = y

  def compute_distance(self, point) -> float:
    return round(
        ((self.__x - point.__x)**2 + (self.__y - point.__y)**2)**(0.5), 2)

  def magnitude(self):
    return round((self.__x**2 + self.__y**2)**(0.5), 2)

  def dot_product(self, point):
    return self.__x * point.__x + self.__y * point.__y

  def sum(self, i_point):
    return Point(self.__x + i_point.__x, self.__y + i_point.__y)

  def real_product(self, i_number: float):
    return Point(self.__x * i_number, self.__y * i_number)

  def get_x(self):
    return self.__x

  def get_y(self):
    return self.__y


class Line:
  definition: str = "It's a join between two points"

  def __init__(self, start_point: Point, end_point: Point):
    self.__start_point = start_point
    self.__end_point = end_point

  def length(self):
    return self.__start_point.compute_distance(self.__end_point)

  def get_starting_point(self):
    return self.__start_point

  def get_ending_point(self):
    return self.__end_point

  def to_vector(self):
    return self.__end_point.sum(self.__start_point.real_product(-1))

  def compute_angle(self, i_line):
    self_vector = self.to_vector()
    i_vector = i_line.to_vector()

    magnitude_product = (self_vector.magnitude() * i_vector.magnitude())
    cos = self_vector.dot_product(i_vector) / magnitude_product

    return math.degrees(math.acos(cos))

  def reverse(self):
    return Line(self.__end_point, self.__start_point)

class Shape:

  def __init__(self, vertices: list):
    self.__vertices = vertices

    self.__edges = []
    for i in range(len(vertices) - 1):
      self.__edges.append(Line(vertices[i], vertices[i + 1]))
    if vertices[0] != vertices[-1]:
      self.__edges.append(Line(vertices[-1], vertices[0]))
      self.__vertices.append(vertices[0])


    self.__is_regular = True
    #compare lenghts
    for i in range(len(self.__edges) - 1):
      if self.__edges[i].length() != self.__edges[i + 1].length():
        self.__is_regular = False
        break

    angles = self.compute_inner_angles()
    for i in range(len(angles) - 1):
      if angles[i] != angles[i + 1]:
        self.__is_regular = False
        break

  def compute_area(self):
    pass

  def compute_perimeter(self):
    perimeter = 0.0
    for line in self.__edges:
      perimeter += line.legnth()
    return perimeter

  def compute_inner_angles(self):
    angles = []
    for i in range(0, len(self.__edges) - 1):
      angle = self.__edges[i].reverse().compute_angle(self.__edges[i + 1])
      angles.append(angle)
    angles.append(self.__edges[0].compute_angle(self.__edges[-1].reverse()))
    return angles
    #TODO: the method does not know if the angle it is calculating is an 
    #internal or external angle, we need a way to know that and subtract the 
    #external angle from 2pi if it is an external angle to get the internal angle

  def is_regular(self):
    return self.__is_regular

  def get_vertices(self):
    return self.__vertices

  def get_edges(self):
    return self.__edges
  
my_shape = Shape(
    [Point(0, 0),
     Point(0, 2),
     Point(1, 1),
     Point(2, 2),
     Point(2, 0)])
#vertices = [Point(x=0, y=0), Point(x=1, y=4), Point(x=2, y=0)]
#my_shape = Shape(vertices=vertices)
print()
print(my_shape.compute_inner_angles())
