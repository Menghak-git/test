color = input (" enter a coter:")
result=''
if color == "red":
    result= "stop!"
elif color == "yellow":
    result = "be careful!"
elif color == "green":
    result = "go!"
else:
    result = "high risk , please check left and right"
print("traffic signal says:",result)
