def rgb2hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        if g >= b:
            h = ((g - b) / df) * 60
        else:
            h = ((g - b) / df) * 60 + 360
    elif mx == g:
        h = ((b - r) / df) * 60 + 120
    elif mx == b:
        h = ((r - g) / df) * 60 + 240
    if mx == 0:
        s = 0
    else:
        s = df / mx
    v = mx
    H = h / 2
    S = s * 255.0
    V = v * 255.0
    return H, S, V


def rgb22hsv(R, G, B):
    mx = max(R, G, B)
    mn = min(R, G, B)
    V = max(R, G, B)
    S = (mx - mn) / mx
    if mx == mn:
        H = 0

    if R == mx:
        H = (G-B) / (mx-mn) * 60
    if G == mx:
        H = 120+(B-R) / (mx-mn) * 60
    if B == mx:
        H = 240 + (R-G) / (mx-mn) * 60
    if H < 0:
        H = H+ 360
    return H, S, V

# def rgb2hsv(r, g, b):
#     r, g, b = r/255.0, g/255.0, b/255.0
#     mx = max(r, g, b)
#     mn = min(r, g, b)
#     m = mx-mn
#     if mx == mn:
#         h = 0
#     elif mx == r:
#         if g >= b:
#             h = ((g-b)/m)*60
#         else:
#             h = ((g-b)/m)*60 + 360
#     elif mx == g:
#         h = ((b-r)/m)*60 + 120
#     elif mx == b:
#         h = ((r-g)/m)*60 + 240
#     if mx == 0:
#         s = 0
#     else:
#         s = m/mx
#     v = mx
#     H = h / 2
#     S = s * 255.0
#     V = v * 255.0
#     return H, S, V