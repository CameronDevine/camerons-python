__all__ = ["Lowpass"]


class Lowpass:
    def __init__(self, timeconstant, default=0):
        self.timeconstant = timeconstant
        self.default = default
        self.reset()

    def alpha(self, dt):
        return dt / (self.timeconstant + dt)

    def filter(self, val, dt):
        alpha = self.alpha(dt)
        self.last_val = alpha * val + (1 - alpha) * self.last_val
        return self.last_val

    def reset(self):
        self.last_val = self.default
