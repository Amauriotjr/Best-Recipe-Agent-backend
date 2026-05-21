class RecipeMatcherTool:

    def match(
        self,
        user_ingredients: list[str],
        recipes: list[dict],
        max_results: int = 5
    ) -> list[dict]:

        user_ingredient_set = set(user_ingredients)
        recommendations = []

        for recipe in recipes:
            recipe_ingredients = recipe.get("ingredients", [])

            normalized_recipe_ingredients = [
                ingredient.strip().lower()
                for ingredient in recipe_ingredients
                if ingredient and ingredient.strip()
            ]

            recipe_ingredient_set = set(normalized_recipe_ingredients)

            if not recipe_ingredient_set:
                continue

            available_ingredients = sorted(
                user_ingredient_set.intersection(recipe_ingredient_set)
            )

            missing_ingredients = sorted(
                recipe_ingredient_set.difference(user_ingredient_set)
            )

            match_score = round(
                (len(available_ingredients) / len(recipe_ingredient_set)) * 100,
                2
            )

            if match_score > 0:
                recommendations.append(
                    {
                        "id": recipe.get("id"),
                        "name": recipe.get("name", "Unknown Recipe"),
                        "category": recipe.get("category", "unknown"),
                        "area": recipe.get("area", "unknown"),
                        "difficulty": recipe.get("difficulty", "unknown"),
                        "source": recipe.get("source", "local database"),
                        "match_score": match_score,
                        "available_ingredients": available_ingredients,
                        "missing_ingredients": missing_ingredients,
                        "image_url": recipe.get("image_url"),
                        "source_url": recipe.get("source_url"),
                        "youtube_url": recipe.get("youtube_url")
                    }
                )

        recommendations.sort(
            key=lambda recipe: recipe["match_score"],
            reverse=True
        )

        return recommendations[:max_results]