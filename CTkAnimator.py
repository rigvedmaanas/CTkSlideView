
class CTkAnimator:
    def __init__(self, from_=0, to=100, type=None, acceleration=0.01):
        self.from_ = from_
        self.to = to
        self.type = type
        self.t = 0
        self.completed = False
        self.acceleration = acceleration
    def map_range(self, value, start1, stop1, start2, stop2):
        """
        Maps a value from one range to another range.

        Parameters:
        value (float): The value to be mapped.
        start1 (float): The lower bound of the input range.
        stop1 (float): The upper bound of the input range.
        start2 (float): The lower bound of the output range.
        stop2 (float): The upper bound of the output range.

        Returns:
        float: The mapped value in the second range.
        """
        return start2 + (stop2 - start2) * ((value - start1) / (stop1 - start1))

    def __ease_in_out_quart(self, x, output_start, output_end):
        if x < 0.5:
            return output_start + (output_end - output_start) * (8 * x ** 4)
        else:
            return output_start + (output_end - output_start) * (1 - (-2 * x + 2) ** 4 / 2)

    def get(self):
        if not self.completed:
            if self.t >= 1.0:

                self.completed = True

            self.t += self.acceleration

            if self.type == None:
                x = self.t
                return self.__ease_in_out_quart(x, self.from_, self.to)
    def change_val(self, from_=0, to=100, type=None, acceleration=0.01):
        self.from_ = from_
        self.to = to
        self.type = type
        self.t = 0

        self.completed = False
        self.acceleration = acceleration


