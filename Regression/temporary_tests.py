# Temporary tests
from regression import Regression

x = [1,2,3,4,5,6,7,8,9,10,11,12]
y = [25,38,29,115,82,114,120,160,153,190,239,175]

def temp_runner(cx, cy):
    r2 = Regression()
    r2.receive_data(cx, cy)
    # slope = r2.slope_calculate(r2.x_values_iv, r2.y_values_dv)
    # intercept = r2.intercept_calculate(r2.x_values_iv, r2.y_values_dv)
    significance = r2.slope_significance()


if __name__ == "__main__":
    temp_runner(x, y)
