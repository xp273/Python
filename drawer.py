import turtle as t  

inputShape = input("Input Shape: (Circle - Square - Triangle)")
if (inputShape == "Circle"):
    inputCircleRadius = float(input("Input circle's radius: "))
    t.circle(inputCircleRadius)
elif (inputShape == "Square"):
    inputSquareLength = float(input("Input square's length: "))
    for i in range(0,4):
        t.fd(inputSquareLength)
        t.rt(90)
elif (inputShape == "Triangle"):
    inputTriangleLength = float(input("Input triangle's length: "))
    t.rt(30)
    t.fd(inputTriangleLength)
    t.rt(120)
    t.fd(inputTriangleLength)
    t.rt(120)
    t.fd(inputTriangleLength)
t.mainloop()