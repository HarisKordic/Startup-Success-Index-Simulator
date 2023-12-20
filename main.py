import numpy as np
import pandas as pd
import csv
import io
import requests
import random
from mimesis.providers import Finance
from data_models.models import Startup
from datetime import datetime

finance_gen = Finance()

# Internal simulation inputs
NUM_SIMULATIONS = 10000
STARTUP_COUNT = 100
CPI_WEIGHT = 0.1
SEED_FUNDING_MEAN = 1000000
SEED_FUNDING_STD_DEV = 600000
SEED_FUNDING_WEIGHT = 1.0

def calculate_success_value(cpi: float, seed_funding: float) -> float:
  # Determines the approximate min and max values returned earlier with a normal distribution
  seed_funding_min = SEED_FUNDING_MEAN - 3 * SEED_FUNDING_STD_DEV
  seed_funding_max = SEED_FUNDING_MEAN + 3 * SEED_FUNDING_STD_DEV
  normalized_cpi = cpi / 100.0
  normalized_seed_funding = seed_funding - seed_funding_min / (seed_funding_max - seed_funding_min)

  return (normalized_cpi + normalized_seed_funding) / 2
  
def determine_success(startups: list[Startup]) -> int:
  startup_success_values = list[float]()
  treshold = 420000 # Arbitrarily taken from the success values
  success_count = 0

  for startup in startups:
    startup.success_value = calculate_success_value(startup.cpi_index, startup.seed_funding_index)
    startup_success_values.append(startup.success_value)
    startup.is_successful = startup.success_value > treshold

    if (startup.is_successful):
      success_count += 1

  return success_count

def get_seed_funding_distribution():
  return np.random.normal(loc=SEED_FUNDING_MEAN, scale=SEED_FUNDING_STD_DEV, size=NUM_SIMULATIONS)

def generate_startups(countries, cpi_dictionary, seed_funding_distribution) -> list[Startup]:  
  startups = list[Startup]()

  for i in range(STARTUP_COUNT):
    random_country = countries[random.randint(0, countries.__len__() - 1)]

    startups.append(Startup(
      country = random_country,
      name = finance_gen.company(),
      cpi_index = cpi_dictionary[random_country],
      seed_funding_index = seed_funding_distribution[random.randint(0, seed_funding_distribution.__len__() - 1)]
    ))

  return startups

def export_to_csv(startups: list[Startup], success_ratios: list[float]):
  current_time = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")

  with open(f"data_{current_time}.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Simulation number', 'Country', 'Company name', 'CPI', 'Seed funding', 'Success value', 'Overall simulation success ratio'])

    for index, startup in enumerate(startups):
      writer.writerow([index, startup.country, startup.name, startup.cpi_index, np.round(startup.seed_funding_index, 2), np.round(startup.success_value, 2), f"{success_ratios[index]}%"])

# Scraping the latest CPI values from tradingeconomics.com
def get_cpi() -> dict[str, float]:
  url = 'https://tradingeconomics.com/country-list/corruption-index?continent=europe'
  user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0'

  response = requests.get(url, headers={'User-Agent': user_agent})
  data_frames = pd.read_html(io.StringIO(response.text))

  return data_frames[0].set_index('Country')['Last'].to_dict()

def run_simulations(country_list: list[str], cpi_dictionary: dict[str, float], most_successful_startups: list[Startup], success_ratios: list[float]):
    for i in range(NUM_SIMULATIONS):
      seed_funding_distribution = get_seed_funding_distribution()
      startups = generate_startups(country_list, cpi_dictionary, seed_funding_distribution)
      success_count = determine_success(startups)
      startups.sort(key=lambda x: x.success_value, reverse=True)
      most_successful_startups.append(startups[0])

      success_ratio = np.round(success_count / startups.__len__() * 100)
      success_ratios.append(success_ratio)

      print(f"Performed simulation {i} with a success ratio of {success_ratio}")

def main():
  cpi_dictionary = get_cpi()
  country_list = []
  most_successful_startups = []
  success_ratios = []

  for key in cpi_dictionary.keys():
    country_list.append(key)

  run_simulations(country_list, cpi_dictionary, most_successful_startups, success_ratios)
  export_to_csv(most_successful_startups, success_ratios)

if (__name__ == "__main__"):
  main()



