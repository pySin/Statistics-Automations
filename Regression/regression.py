# Regression


class Regression:

    def __init__(self):
        name = None

    @staticmethod
    def receive_data(x_values_iv, y_values_dv):
        x_mean = sum(x_values_iv) / len(x_values_iv)
        y_mean = sum(y_values_dv) / len(y_values_dv)
        print(f"X mean: {x_mean}")
        print(f"Y mean: {y_mean}")

        xy_summation = 0
        x_2_summation = 0
        for i in range(len(x_values_iv)):
            xy_summation += (x_values_iv[i] - x_mean) * (y_values_dv - y_mean)
            x_2_summation += (x_values_iv[i] - x_mean) ** 2

        slope = xy_summation / x_2_summation
        print(f"Slope: {slope}")

