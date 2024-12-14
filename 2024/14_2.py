from PIL import Image

with open('input.txt') as f:
    contents = f.readlines()

w = 101
h = 103

for i in range(10000):
    img = Image.new('1', (w, h))
    for j in range(h):
        for k in range(w):
            img.putpixel((k, j), 1)
            

    for c in contents:
        spl = c.split(" ")
        p_spl = spl[0].split("=")[1].split(",")
        p = (int(p_spl[1]), int(p_spl[0]))

        v_spl = spl[1][:-1].split("=")[1].split(",")
        v = (int(v_spl[1]), int(v_spl[0]))

        end_p = ((p[0] + v[0] * i) % h, (p[1] + v[1] * i) % w)

        img.putpixel((end_p[1], end_p[0]), 0)
    
    img.save("img\\" + str(int(i/1000)*1000) + "\\" + str(i) + ".bmp")

