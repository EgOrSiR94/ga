x = 300
z = "p"
c = 255
v = 0
b = 0
n = 300
m = 300
k = 300
l = 300
def setup():
    size(600,600)
def draw():
    global x, z,c,v,b,n,m,k,l
    background(255, 255, 255)
    ellipse(l, 300, 100,100)
    if mousePressed:
        fill(0,0,random(0,255))
 
        if z == "p":
            x += 1
        else:
            x -= 1
        if z == "p":
            n += 2
        else:
            n -= 2
        if z == "p":
            m += 3
        else:
            m -= 3
        if z == "p":
            k += 4
        else:
            k -= 4
        if z == "p":
            l += 5
        else:
            l -= 5
    
    if x ==550:
        z = "l"
    elif x == 50:    
        z = "p"
    if n ==550:
        z = "l"
    elif n == 50:    
        z = "p"
    if m ==550:
        z = "l"
    elif m == 50:    
        z = "p"
    if k ==550:
        z = "l"
    elif k == 50:    
        z = "p"
    if l ==550:
        z = "l"
    elif l == 50:    
        z = "p"
