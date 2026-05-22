# Best Recipe Agent - Backend

Best Recipe Agent Backend is a Python FastAPI application that powers an AI- and agent-based recipe recommendation system.

The backend receives ingredients from the user, retrieves candidate recipes from MongoDB, compares available ingredients with recipe requirements, calculates compatibility scores, and returns ranked recipe recommendations through API endpoints.

This project was developed as part of an AI- and agent-based Python software system. It demonstrates agent workflow coordination, external database access, data conversion, testing, API development, and deployment preparation.

---

## Live Deployment

Backend API:

```text
YOUR_RENDER_BACKEND_URL
```

Swagger Documentation:

```text
YOUR_RENDER_BACKEND_URL/docs
```

Frontend Application:

```text
YOUR_VERCEL_FRONTEND_URL
```

Frontend Repository:

```text
https://github.com/Amauriotjr/Best-Recipe-Agent-frontend
```

---

## Project Goal

The goal of this backend is to provide recipe recommendations based on ingredients that the user already has.

Example user input:

```text
flour, sugar, eggs, butter
```

The backend returns:

- recommended recipes;
- match score for each recipe;
- ingredients the user has;
- missing ingredients;
- original recipe ingredients;
- recipe instructions;
- source URL when available.

---

## Main Features

- FastAPI backend API
- Swagger UI documentation
- MongoDB database integration
- Agent-based recommendation workflow
- Ingredient parsing and normalization
- Recipe matching and ranking
- Strict ingredient matching to avoid false positives
- External recipe dataset conversion
- MongoDB import script
- Automated tests with pytest
- Deployment-ready backend for Render

---

## Technologies Used

- Python
- FastAPI
- Uvicorn
- MongoDB Atlas
- PyMongo
- Python Dotenv
- JSON
- Pytest
- Git
- GitHub
- Render

---

## Agent-Based Workflow

The backend uses an agent-based workflow.

The main agent coordinates different tools. Each tool has a specific responsibility, and the user only interacts with the API.

Workflow:

```text
User input
→ Recipe Recommendation Agent
→ Ingredient Parser Tool
→ MongoDB Recipe Database Tool
→ Recipe Matcher Tool
→ Report Generator Tool
→ API Response
```

The agent performs the following steps:

1. Receives raw ingredient input.
2. Parses and cleans the ingredient list.
3. Searches MongoDB for candidate recipes.
4. Compares user ingredients with recipe ingredients.
5. Calculates match scores.
6. Sorts recipes by compatibility.
7. Returns a structured JSON response.

---

## Tools Used by the Agent

### Ingredient Parser Tool

The Ingredient Parser Tool converts raw user input into a clean list.

Example:

```text
Eggs, Flour, Sugar
```

Becomes:

```python
["eggs", "flour", "sugar"]
```

It removes extra spaces, converts text to lowercase, and removes duplicates.

---

### Ingredient Normalizer Tool

The Ingredient Normalizer Tool standardizes ingredient names for comparison.

Examples:

```text
eggs → egg
tomatoes → tomato
all-purpose flour → all purpose flour
```

The normalizer helps compare ingredients consistently while avoiding incorrect partial matches.

For example:

```text
flour does not match brown rice flour
flour does not match flour tortilla
peanut butter does not match butter
```

---

### MongoDB Recipe Database Tool

The MongoDB Recipe Database Tool connects to MongoDB and retrieves candidate recipes.

MongoDB is used because the full converted recipe dataset is too large to store directly in GitHub.

The database stores recipes with normalized ingredients, making recipe search faster and more consistent.

---

### Recipe Matcher Tool

The Recipe Matcher Tool compares the user's ingredients with the ingredients required by each recipe.

The match score is calculated as:

```text
match score = available ingredients / required ingredients
```

Example:

```text
User ingredients:
flour, sugar, eggs

Recipe ingredients:
flour, sugar, eggs, butter

Match score:
3 / 4 = 75%
```

The matcher returns:

- available ingredients;
- missing ingredients;
- compatibility score;
- recipe metadata;
- original ingredients;
- instructions;
- source URL.

---

### Report Generator Tool

The Report Generator Tool creates the final structured response returned by the API.

The response includes:

- user ingredients;
- data source;
- total recommendations;
- summary;
- recommended recipes.

---

## External Dataset

This project uses recipe data adapted from the public GitHub repository:

```text
https://github.com/dpapathanasiou/recipes
```

The external repository is not committed directly into this backend repository.

It should be cloned locally into:

```text
data/external/recipes-github/
```

This folder is ignored by Git.

---

## Data Conversion Process

The original external dataset has a different JSON structure from this project.

The conversion script is located at:

```text
scripts/import_github_recipes.py
```

The script:

- reads recipe JSON files from the external dataset;
- extracts recipe names;
- extracts ingredients;
- extracts instructions;
- extracts source URLs;
- removes invalid recipes;
- removes duplicate recipes;
- cleans ingredient names;
- generates `data/recipes.json`;
- generates `data/recipes_import_summary.json`.

Ingredient cleaning removes:

- quantities;
- fractions;
- Unicode fractions;
- measurement units;
- preparation details;
- unnecessary punctuation.

Examples:

```text
"1/2 cup flour" → "flour"
"½ teaspoon salt" → "salt"
"3 tablespoons olive oil" → "olive oil"
"3/4 cup very warm water" → "water"
```

---

## MongoDB Import Process

After converting the external dataset, the recipes are imported into MongoDB using:

```text
scripts/import_recipes_to_mongodb.py
```

The MongoDB import script:

- reads `data/recipes.json`;
- adds normalized ingredients to each recipe;
- inserts recipes into MongoDB in batches;
- creates indexes for better search performance.

The full `data/recipes.json` file is not committed to GitHub because it can exceed GitHub's file size limit.

---

## Project Structure

```text
Best-Recipe-Agent-backend/
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── agent.py
│   ├── schemas.py
│   │
│   └── tools/
│       ├── __init__.py
│       ├── ingredient_parser.py
│       ├── ingredient_normalizer.py
│       ├── recipe_mongodb.py
│       ├── recipe_matcher.py
│       └── report_generator.py
│
├── scripts/
│   ├── import_github_recipes.py
│   └── import_recipes_to_mongodb.py
│
├── data/
│   ├── recipes_sample.json
│   ├── recipes_import_summary.json
│   └── external/
│       └── recipes-github/
│
├── tests/
│   ├── test_agent.py
│   ├── test_api.py
│   ├── test_import_github_recipes.py
│   ├── test_ingredient_parser.py
│   └── test_recipe_matcher.py
│
├── .env.example
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Environment Variables

Create a `.env` file in the project root.

Example:

```env
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/
MONGODB_DATABASE=recipe_agent
MONGODB_COLLECTION=recipes
```

The `.env` file must not be committed to GitHub.

A safe example file is included as:

```text
.env.example
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Amauriotjr/Best-Recipe-Agent-backend.git
cd Best-Recipe-Agent-backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment.

On Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

---

## Preparing the Dataset Locally

Create the external data folder:

```bash
mkdir -p data/external
```

On Windows PowerShell:

```powershell
mkdir data\external
```

Clone the external recipe dataset:

```bash
git clone --depth 1 https://github.com/dpapathanasiou/recipes.git data/external/recipes-github
```

Convert the external dataset:

```bash
python scripts/import_github_recipes.py
```

This generates:

```text
data/recipes.json
data/recipes_import_summary.json
```

To test with fewer recipes:

```bash
python scripts/import_github_recipes.py --limit 100
```

---

## Importing Recipes into MongoDB

After generating `data/recipes.json`, import the recipes into MongoDB:

```bash
python scripts/import_recipes_to_mongodb.py --clear
```

The `--clear` flag removes existing recipes from the collection before inserting the new data.

Expected result:

```text
Imported recipes into MongoDB.
Database: recipe_agent
Collection: recipes
```

---

## Running the Backend Locally

Start the API server:

```bash
uvicorn src.main:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### GET `/`

Returns a welcome message.

Example:

```text
http://127.0.0.1:8000/
```

---

### GET `/health`

Checks if the API is running.

Example response:

```json
{
  "status": "ok"
}
```

---

### GET `/database/status`

Checks the MongoDB connection.

Example response:

```json
{
  "status": "connected",
  "database": "recipe_agent",
  "collection": "recipes",
  "total_recipes": 50000
}
```

---

### GET `/recipes/search`

Searches candidate recipes from MongoDB.

Example:

```text
http://127.0.0.1:8000/recipes/search?ingredients=flour,sugar,eggs&limit=10
```

---

### POST `/recommend`

Returns recipe recommendations based on ingredients.

Example request:

```json
{
  "ingredients": "flour, sugar, eggs, butter",
  "max_results": 5
}
```

Example response:

```json
{
  "user_ingredients": [
    "flour",
    "sugar",
    "eggs",
    "butter"
  ],
  "data_source": "MongoDB recipe database",
  "total_recommendations": 5,
  "summary": "The best recommendation is Example Recipe with a match score of 75.0%.",
  "recommendations": [
    {
      "name": "Example Recipe",
      "match_score": 75.0,
      "available_ingredients": [
        "flour",
        "sugar",
        "eggs"
      ],
      "missing_ingredients": [
        "butter"
      ],
      "original_ingredients": [
        "1 cup flour",
        "1 cup sugar",
        "2 eggs",
        "1/2 cup butter"
      ],
      "instructions": [
        "Mix the ingredients.",
        "Bake until ready."
      ],
      "source_url": "https://example.com"
    }
  ]
}
```

---

## Running Tests

Run all tests:

```bash
python -m pytest
```

The tests verify:

- ingredient parsing;
- duplicate ingredient removal;
- invalid input handling;
- ingredient cleaning;
- recipe matching;
- strict ingredient comparison;
- plural and singular matching;
- agent workflow;
- API endpoints;
- dataset conversion.

---

## Deployment on Render

This backend is deployed on Render as a Web Service.

Recommended Render configuration:

```text
Runtime:
Python
```

```text
Build Command:
pip install -r requirements.txt
```

```text
Start Command:
uvicorn src.main:app --host 0.0.0.0 --port $PORT
```

Required Render environment variables:

```env
MONGODB_URI=my_mongodb_connection_string
MONGODB_DATABASE=recipe_agent
MONGODB_COLLECTION=recipes
```

---

## CORS Configuration

The backend allows requests from:

```text
http://localhost:5173
http://127.0.0.1:5173
https://best-recipe-agent-frontend.vercel.app
```

If the Vercel frontend URL changes, it must be added to the CORS configuration in `src/main.py`.

---

## GitHub File Size Note

The full generated file below should not be committed to GitHub:

```text
data/recipes.json
```

It can exceed GitHub's file size limit.

The following files and folders are ignored:

```text
data/recipes.json
data/external/recipes-github/
.env
venv/
__pycache__/
.pytest_cache/
```

---

## Deployment Strategy

The deployment strategy uses separate services:

```text
Backend:
Render

Frontend:
Vercel

Database:
MongoDB Atlas
```

This separation improves maintainability because each part of the system has a clear responsibility.

---

## Project Status

Current version: `1.0.0`

The backend currently supports:

- MongoDB recipe search;
- FastAPI routes;
- Swagger documentation;
- recipe recommendation;
- strict ingredient matching;
- recipe instructions in responses;
- external dataset conversion;
- MongoDB import workflow;
- automated tests;
- Render deployment.

## Related Repository

Frontend repository:

```text
https://github.com/Amauriotjr/Best-Recipe-Agent-frontend
```

---

## External Dataset Credit

This project uses recipe data adapted from:

```text
https://github.com/dpapathanasiou/recipes
```

The data is converted into the internal project format and imported into MongoDB.

---

## License

This project is for academic and educational purposes.