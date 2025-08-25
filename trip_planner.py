import os
from dotenv import load_dotenv
from portia import Portia, DefaultToolRegistry, LLMProvider, Config
from portia.cli import CLIExecutionHooks
from portia.end_user import EndUser

load_dotenv(override=True)

google_config = Config.from_default(llm_provider=LLMProvider.GOOGLE,
    default_model='google/gemini-2.5-flash', 
)

portia = Portia(config=google_config,
    tools=DefaultToolRegistry(config=google_config),
    execution_hooks=CLIExecutionHooks(),
)

end_user = EndUser(
    external_id="trip_planner_demo",
    name="Johnny Test",
)

def get_criteria() -> str:
    """Get trip criteria from user input."""
    trip_planner = input("Please enter Trip Planner Name (Default is The One): ") or "The One"
    trip_plan_country = input("Please enter Trip Country (Default contry is India): ") or "India"
    trip_plan_state = input("Please enter Trip State (Default is Any): ") or "Any"
    trip_plan_budget = input("Please enter Trip Budget (Default is I am Rich): ") or "Any"
    trip_plan_dates = input("Please enter Trip Dates [ e.g.: 2025-Sep-20 to 2025-Sep-22 ] (Default is Any): ") or "Any near future"
    trip_interests = input("Please enter Trip Interests [ e.g.: Adventure, Culture, Food, Nature ] (Default is Any): ") or "Any"
    receipient_email = input("Please enter One Receipient Email* (Mandatory) : ")

    criteria = "Create a detailed trip plan for the country {country} with {state} state, {budget} budget, {dates} dates and {interests} interests and then format in a nice email and add regards with the name '{name}' and email it to '{email}'.".format(country=trip_plan_country, state=trip_plan_state, budget=trip_plan_budget, dates=trip_plan_dates, interests=trip_interests, name=trip_planner, email=receipient_email)
    return criteria

plan = portia.plan(query="""{criteria}""".format(criteria=get_criteria()))

input(f"{plan.model_dump_json(indent=2)}")

plan_run = portia.run_plan(plan)

print(f"{plan_run.model_dump_json(indent=2)}")
