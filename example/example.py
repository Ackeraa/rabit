import rabit

def draw():
    r.begin_hide()
    for i in range(5):
        for j in range(5):
            r.draw_rect(i, j)
            r.draw_text(i, j, str(i * 5 + j))
    r.end_hide()

    r.draw_line(0, 0, 5, 5)

    r.speed(15)
    for i in range(5):
        for j in range(5):
            r.paint_rect(i, j, color="red")

    r.begin_hide()
    for i in range(5):
        for j in range(5):
            r.paint_rect(i, j, color="blue", cover=True)
    r.end_hide()

r = rabit.Rabit(5, 600)
rabit.convert2gif(draw, 10, 10)

