# Skeleton code for participant solutions to the paint splash problem presented
# in workshop. To run the tests for this problem, run the paint_tests.py script

def paint_splash( pixels, click_point, target_color ):
    # Inputs:
    # pixels: [ [ int ] ]
    # click_point: ( int, int )
    # target_color: int

    # YOUR CODE HERE. Modify pixels in place. Or create a new array, I don't care.
    # In place is better practice though.

    x, y = click_point
    color_at_click_point = pixels[x][y]
    recurse_paint_splash( pixels, color_at_click_point, click_point, target_color )
    return pixels

def recurse_paint_splash( pixels, og_color, current_point, target_color ):
    print current_point
    x, y = current_point
    neighbors_indices = [ (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1) ]
    try:
        current_color = pixels[x][y]
    except:
        return
    if current_color == og_color:
        pixels[x][y] = target_color
        for coords in neighbors_indices:
            recurse_paint_splash( pixels, og_color, coords, target_color )

