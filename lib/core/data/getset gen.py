#Gen getset

varsnames = ["name","passwd","ip","port","max_clients","clients_connected"]

data = """"""
for v in varsnames:
    get = "def get_" + v + "(self):\n\treturn self." + v + "\n"
    set = "def set_" + v + "(self," + v + "):\n\tself." + v + " = " + v + "\n"
    data = data + get + "\n" + set + "\n"

print(data)