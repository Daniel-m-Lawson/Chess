class Bishop:
    def __init__(self, color):
        self.color = color  # 'w' for white, 'b' for black

    def get_color(self):
        return self.color

    def get_name(self):
        return "Bishop"

    def get_possible_moves(self, current_position):
        
        x, y = current_position
        possible_moves = []

        # Bishop
