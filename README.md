# Trip Planner Agent

This project is a **Trip Planner Agent** built on **Portia** and the **Google Gemini API**. It is designed to simplify the process of generating personalized trip plans and delivering them directly via email.

## Features

* Accepts user inputs:

  * **Trip Planner Name** (default: `The One`)
  * **Trip Country** (default: `India`)
  * **Trip State** (default: `Any`)
  * **Trip Budget** (default: `Any`)
  * **Trip Dates** (default: `Any near future`)
  * **Trip Interests** (default: `Any`)
  * **One recipient email** (Mandetory)
* Generates a trip plan based on the provided details.
* If no details are provided, falls back to defaults or generates a generic plan.
* Sends the generated trip plan to the given email address using Portia’s email tool.
* Seeks clarification from the user when email authentication (OAuth) is required.

## Tech Stack

* **Portia SDK**
* **Google Gemini API**
* **Poetry**
* **Python** [ 3.12.X ]

## Compatibility

* **Important**: The current `langchain-google-genai` dependency, as of August 2025, does **not** support Python **3.13.X**.
* Use **Python 3.12.X** for a smooth setup.
* If you already have Python 3.13.X installed, instead of uninstalling it, place the path to Python **3.12.X** **above** the Python paths in your environment variables.

## Setup

1. Clone the repository.
2. Navigate into the project folder.
3. Install dependencies with Poetry:

   ```bash
   poetry install --no-root
   ```
4. Run the project:

   ```bash
   poetry run python trip_planner.py
   ```

## Notes

* In real trip planning we usually don't stick to the first plan we see, so, I've included only one recipient functionality. Users can pick up their favorite plan, and forward it, instead of blasting everyone at once each time...
* Extending the project to handle **multiple recipients** is straightforward (e.g., with a simple for loop function).
* This project demonstrates how Portia can coordinate user inputs, an LLM, and external tools (email).

## Future Improvements

* Multi-recipient support.
* Better input validation (dates, budgets, etc.).
* UI integration for non-CLI users.
* Adding trip cost estimations or booking recommendations.

---

Built by Saurabh Ram
