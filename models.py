from dataclasses import dataclass, field


@dataclass
class RegisterRow:
    article: str
    rest: int | None
    price_standard: float | None
    price_dealer: float | None
    price: float | None = field(init=False)

    def __post_init__(self):
        self.price = (
            min(self.price_standard, self.price_dealer)
            if self.price_standard is not None and self.price_dealer is not None
            else self.price_standard or self.price_dealer
        )

    @property
    def processed_data(self):
        return [self.article, self.price, self.rest]


class Register:
    header = ["Артикул", "Стоимость", "Остаток"]
    data: list[RegisterRow] = []

    def __iter__(self):
        yield self.header
        for row in self.data:
            yield row.processed_data
