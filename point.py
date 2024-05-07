class Point:
    def __init__(self, x: int = None, y: int = None):
        self.x = x
        self.y = y
        x = int(input())
        y = int(input())
        print(f'[{x};{y}]')
a = Point()