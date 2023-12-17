"""
2353. Design a Food Rating System
https://leetcode.com/problems/design-a-food-rating-system/
"""

from sortedcontainers import SortedList


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods_ratings = dict()
        self.foods_cuisines = dict()
        self.cuisines_sorted = dict()

        for i in range(len(foods)):
            self.foods_ratings[foods[i]] = ratings[i]
            self.foods_cuisines[foods[i]] = cuisines[i]
            if not self.cuisines_sorted.get(cuisines[i]):
                self.cuisines_sorted[cuisines[i]] = SortedList(key=lambda x: (-self.foods_ratings[x], x))
            self.cuisines_sorted.get(cuisines[i]).add(foods[i])

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.foods_cuisines[food]
        self.cuisines_sorted[cuisine].discard(food)
        self.foods_ratings[food] = newRating
        self.cuisines_sorted[cuisine].add(food)

    def highestRated(self, cuisine: str) -> str:
        return self.cuisines_sorted[cuisine][0]

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
