w=400
h=400
Xof=80
Yof=80
r=Yof/2-10
of=30
def setup():
    size(w, h)
    stroke(255)
def niv(n):
    return n*Yof
 
def cer(x,n):
    stroke(255)
    circle(x,niv(n),r)    
    line(x,niv(n),x+(Xof/n),niv(n+1))
    line(x,niv(n),x-(Xof/n),niv(n+1))

def X(x,n,semn):
    return x+semn*(Xof/(n-1))

def draw():
    translate(w/2,0)
    background(0)
    strokeWeight(4)
    #for i in range(5):
        #for j
    
    cer(0,1)
    
    n=2
    cer(X(0,n,-1),n)
    cer(X(0,n,+1),n)
    
    cer(X(X(0,n,-1),n+1,-1),3)
    cer(X(X(0,n,+1),n+1,-1),3)
    cer(X(X(0,n,-1),n+1,+1),3)
    cer(X(X(0,n,+1),n+1,+1),3)
