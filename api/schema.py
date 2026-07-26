from pydantic import BaseModel


class PredictionInput(BaseModel):

    Moisture: float
    Ash: float
    Volatile_Matter: float
    Fixed_Carbon: float
    Carbon: float
    Hydrogen: float
    Oxygen: float
    Nitrogen: float
    Particle_Size: float
    Temperature: float
    Heating_Rate: float
    Flow_Rate: float
    Biochar_Yield: float
    Gas_Yield: float
    Biomass_species: str