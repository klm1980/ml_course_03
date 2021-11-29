"""
simple modules
"""


class HousePriceModel:

    def __init__(self) -> None:
        pass

    def __call__(self, *, n_floors: int, area: float, heating: str) -> float:
        heating_bonus_dict = {
            "A": 100,
            'B': 20,
            "C": 10,
            "D": 0,
        }
        return 100*n_floors + 5 * area + heating_bonus_dict[heating]

class SantimentModel:
    
    def __init__(self) -> None:
        self.vocabulary = {
            'good': 2,
            "bad": -2,
            "nice": 5,
            "excelent": 8,
            "ugly": 5
        }
    
    def __call__(self, *, text: str) -> int:
        processed_text = text.lower()

        score = 0

        for word, bal in self.vocabulary.items():
            if word in processed_text:
                score += bal
        
        return 1 if score > 0 else -1 if score < 0 else 0


    

