# Regression


class Regression:

    def __init__(self):
        name = None

    def receive_data(self, x_values_iv, y_values_dv):
        x_mean = sum(x_values_iv) / len(x_values_iv)
        y_mean = sum(y_values_dv) / len(y_values_dv)
        print(f"X mean: {x_mean}")
        print(f"Y mean: {y_mean}")

