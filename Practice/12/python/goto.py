from goto import goto
@goto
def test(5):
   
    s = 0

    label .myLoop

    if n <= 0:
        return s
    s += n
    n -= 1

    goto .myLoop