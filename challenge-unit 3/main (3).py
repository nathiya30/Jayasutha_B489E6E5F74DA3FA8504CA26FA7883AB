def linearsearchproduct(ProductList,
                        targetProduct):
  indices = []

  for index, product in enumerate(ProductList):
    if product == targetProduct:
      indices.append(index)

  return indices



products = ["shoes", "boot", "loafer","shoes", "sandal", "shoes"]
target = "shoes"
result = linearsearchproduct(products, target)
print(result)