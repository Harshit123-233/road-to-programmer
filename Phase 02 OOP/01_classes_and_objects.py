"""Phase 02: OOP
Day: 14th
Part: 01
Topics Learned Today:-
1. What are classes and objects?
2. How to create a class and then create multiple objects with it?"""

class MyFavAnimes:
    score = 10

naruto = MyFavAnimes()
solo_leveling = MyFavAnimes()
one_piece = MyFavAnimes()
one_punch_man = MyFavAnimes()

del one_punch_man #Season 3 sucks

print(naruto.score)
print(solo_leveling.score)
print(one_piece.score)