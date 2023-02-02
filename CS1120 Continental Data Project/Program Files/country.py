from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Country:
    name: str
    currency: str
    literacy_rate: int
    time_zone: float
    continent: str
    main_lang: str
    most_spoken_lang: Optional[str]



