def linear_regression(coordinates_list: list):
    sigma_x = 0
    sigma_x_square = 0
    sigma_y = 0
    sigma_y_square = 0
    sigma_xy = 0
    n = 0
    for coordinate in coordinates_list:
        sigma_x = sigma_x + coordinate[0]
        sigma_x_square = sigma_x_square + (coordinate[0] ** 2)
        sigma_y = sigma_y + coordinate[1]
        sigma_y_square = sigma_y_square + (coordinate[1] ** 2)
        sigma_xy = sigma_xy + (coordinate[0] * coordinate[1])
        n = n + 1  # n = the number of coordinates

    y_intersect = ((sigma_y * sigma_x_square) - (sigma_x * sigma_xy)) / (
        (n * sigma_x_square) - (sigma_x**2)
    )
    gradient = ((n * sigma_xy) - (sigma_x * sigma_y)) / (
        (n * sigma_x_square) - (sigma_x**2)
    )

    return f"The y-intercept is {y_intersect} and the gradient is {gradient}."
