with open('input.txt') as f:
    contents = f.readlines()

w = 101
h = 103
seconds = 100
q1=0
q2=0
q3=0
q4=0
for c in contents:
    spl = c.split(" ")
    p_spl = spl[0].split("=")[1].split(",")
    p = (int(p_spl[1]), int(p_spl[0]))

    v_spl = spl[1][:-1].split("=")[1].split(",")
    v = (int(v_spl[1]), int(v_spl[0]))

    end_p = ((p[0] + v[0] * seconds) % h, (p[1] + v[1] * seconds) % w)

    #check quadrant
    if end_p[0] < (h-1) / 2 and end_p[1] < (w-1)/2:
        q1 += 1
    elif end_p[0] < (h-1) / 2 and end_p[1] > (w-1)/2:
        q2 += 1
    elif end_p[0] > (h-1) / 2 and end_p[1] < (w-1)/2:
        q3 += 1
    elif end_p[0] > (h-1) / 2 and end_p[1] > (w-1)/2:
        q4 += 1

print(q1 * q2 * q3 * q4)
