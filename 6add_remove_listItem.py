letters = ["a", "b", "c"]

letters.append("d")  # add items at end
letters.insert(0, "-")

letters.pop()  # it pops off last item, or u can keep an index too to remove that item
letters.remove("b")  # when we dont know index number but then if we same similar multiple elements then the first among them is removed to remove all same item we have to look and remove individually
print(letters)
# with pop method we can remove one item and with the delete method we can delete the range of items
del letters[0:3]
letters.clear()  # remove all items in list
print(letters)
