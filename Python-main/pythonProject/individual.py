def triangle_area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)
def quadrilateral_area(x1, y1, x2, y2, x3, y3, x4, y4):
    area1 = triangle_area(x1, y1, x2, y2, x3, y3)
    area2 = triangle_area(x1, y1, x3, y3, x4, y4)
    return area1 + area2
x1, y1 = 0, 0
x2, y2 = 4, 0
x3, y3 = 4, 3
x4, y4 = 0, 3
area = quadrilateral_area(x1, y1, x2, y2, x3, y3, x4, y4)
print("Площадь четырёхугольника:", area)
