class Item:
    name: str
    description: str
    drop_rate: int
    rarity: str
    item_type: str
    stats: dict[str, int]

    def __init__(self, _name, _description, _drop_rate, _rarity, _item_type, _stats):
        self.name = _name
        self.description = _description
        self.drop_rate = _drop_rate
        self.rarity = _rarity
        self.item_type = _item_type
        self.stats = _stats