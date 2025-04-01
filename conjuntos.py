conjun={"naranjas", "peras","peras", "mandarinas", "rabanos", "bananos"}
print(len(conjun))
carros={"ford","chevrolett", "mazda", "ford","peras"}

#tienen los metodos de la teoria de conjuntos.
conjun.add("kiwi")
print(conjun.difference(carros))
print(conjun.intersection(carros))
print(conjun.union(carros))
conjun.discard("peras")
print(conjun)
