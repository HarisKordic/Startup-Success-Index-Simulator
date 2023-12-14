import numpy as np
from mimesis.providers import Finance
import random
from data_models.models import Startup

finance_gen = Finance()

# Internal simulation inputs
# TODO: Smarter way to calculate weights for CPI and seed funding
num_simulations = 10000
cpi_mean = 50
cpi_std_dev = 10
cpi_weight = 0.7
seed_funding_mean = 700000
seed_funding_std_dev = 100000
seed_funding_weight = 0.4

# Draw samples from a uniform distribution for CPI values
cpi_distribution = np.round(np.random.normal(loc=cpi_mean, scale=cpi_std_dev, size=num_simulations))

# Draw samples from a uniform distribution for funding values
seed_funding_distribution = np.random.normal(loc=seed_funding_mean, scale=seed_funding_std_dev, size=num_simulations)


european_countries = [
    'Albania', 'Andorra', 'Austria', 'Belarus', 'Belgium', 'Bosnia and Herzegovina', 'Bulgaria', 'Croatia', 
    'Cyprus', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 
    'Iceland', 'Ireland', 'Italy', 'Kosovo', 'Latvia', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Malta', 
    'Moldova', 'Monaco', 'Montenegro', 'Netherlands', 'North Macedonia', 'Norway', 'Poland', 'Portugal', 
    'Romania', 'Russia', 'San Marino', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 
    'Ukraine', 'United Kingdom', 'Vatican City'
]

startups = [Startup(
  country = european_countries[random.randint(0, european_countries.__len__() - 1)],
  name = finance_gen.company(),
  cpi_index = cpi_distribution[random.randint(0, cpi_distribution.__len__() - 1)],
  seed_funding_index = seed_funding_distribution[random.randint(0, seed_funding_distribution.__len__() - 1)]
) for i in range(num_simulations)]


def calculate_success_value(cpi: int, seed_funding: float) -> float:
  return (cpi_weight * cpi) - (seed_funding_weight * seed_funding)
  
def determine_success(startups: list[Startup]) -> int:
  startup_success_values = list[float]()
  treshold = -200000
  success_count = 0

  for startup in startups:
    startup.success_value = calculate_success_value(startup.cpi_index, startup.seed_funding_index)
    startup_success_values.append(startup.success_value)
    startup.is_successful = startup.success_value > treshold

    if (startup.is_successful):
      success_count += 1

  return success_count


success_count = determine_success(startups)
success_rate = success_count / startups.__len__()

for startup in startups:
  print(startup.__str__())
  print(f"Success value: {startup.success_value}\n")
  print(f"Is successful: {startup.is_successful}")

print(f"Success rate: {success_rate}")
