# Calorie Intake Recommendation API

This is a Flask-based RESTful API that provides recommendations for daily calorie intake based on height and weight, along with BMI category determination and ideal weight calculation.

## API Endpoints

- **GET /api/bmi_category** or **POST /api/bmi_category**
  - Accepts JSON data or query parameters containing 'height' (in centimeters) and 'weight' (in kilograms).
  - Calculates BMI (Body Mass Index) using the provided height and weight.
  - Determines the BMI category (Underweight, Normal weight, Overweight, Obese).

- **GET /api/calorie_intake** or **POST /api/calorie_intake**
  - Accepts JSON data or query parameters containing 'height' (in centimeters) and 'weight' (in kilograms).
  - Calculates the Basal Metabolic Rate (BMR) using a basic formula.
  - Returns the estimated daily calorie intake recommendation.

- **GET /api/ideal_weight** or **POST /api/ideal_weight**
  - Accepts JSON data or query parameters containing 'height' (in centimeters).
  - Calculates ideal weight using a basic formula (for males only).
  - Returns the calculated ideal weight for both males and females.

## Getting Started

1. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start the Flask server:

```bash
python application.py
```

## Usage

Send GET or POST requests to the API endpoints with appropriate JSON data or query parameters.

Example:

```json
{
  "height": 170,
  "weight": 70
}
```

```bash
GET /api/bmi_category?height=170&weight=70
```
