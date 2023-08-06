import dataclasses


@dataclasses.dataclass
class DatabaseConfiguration:
    connection_string: str
    database: str
    time_out_seconds: int
