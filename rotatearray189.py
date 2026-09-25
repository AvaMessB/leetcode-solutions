def changevar(var: list):
    var[:] = [4,5]

var = [1, 3]
changevar(var)
print(var)