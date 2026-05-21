from src.tools.recipe_matcher import RecipeMatcherTool


def test_recipe_matcher_calculates_score():
    matcher = RecipeMatcherTool()

    user_ingredients = ["eggs", "cheese", "salt"]

    recipes = [
        {
            "name": "Cheese Omelette",
            "ingredients": ["eggs", "cheese", "salt", "pepper"],
            "category": "breakfast",
            "difficulty": "easy"
        }
    ]

    result = matcher.match(user_ingredients, recipes, max_results=1)

    assert len(result) == 1
    assert result[0]["match_score"] == 75.0
    assert result[0]["missing_ingredients"] == ["pepper"]


def test_recipe_matcher_returns_best_recipe_first():
    matcher = RecipeMatcherTool()

    user_ingredients = ["eggs", "cheese", "salt"]

    recipes = [
        {
            "name": "Recipe A",
            "ingredients": ["rice", "onion"]
        },
        {
            "name": "Recipe B",
            "ingredients": ["eggs", "cheese", "salt", "pepper"]
        }
    ]

    result = matcher.match(user_ingredients, recipes, max_results=2)

    assert result[0]["name"] == "Recipe B"