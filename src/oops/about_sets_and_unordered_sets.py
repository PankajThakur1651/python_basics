from ordered_set import OrderedSet

ordered_set_age = OrderedSet({1, 2, 4})

ordered_set_age.add(11)
ordered_set_age.add(29)

ordered_set_age.add(11)

ordered_set_age.add(99)
ordered_set_age.add(100)


print(f"Ordered set of age {ordered_set_age}")
#Ordered set of age OrderedSet([1, 2, 4, 11, 29, 99, 100])

unordered_set_age = set({1, 2, 4})

unordered_set_age.add(11)
unordered_set_age.add(29)

unordered_set_age.add(11)

unordered_set_age.add(99)
unordered_set_age.add(100)

print(f"Unordered set of age {unordered_set_age}")
#Unordered set of age {1, 2, 99, 4, 100, 11, 29}
