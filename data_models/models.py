class Startup:
    name: str
    country: str
    cpi_index: float
    seed_funding_index: float
    success_value: float
    is_successful: bool

    def __init__(self, name: str, country: str, cpi_index: float, seed_funding_index: float):
        self.name = name
        self.country = country
        self.cpi_index = cpi_index
        self.seed_funding_index = seed_funding_index

    def __str__(self) -> str:
        return f"Name: {self.name}\nCountry: {self.country}\nCPI: {self.cpi_index}\nSeed fund: {self.seed_funding_index}"