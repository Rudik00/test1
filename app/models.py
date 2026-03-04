from dataclasses import dataclass

@dataclass
class URLReport:
    url: str
    status_code: int | None
    response_time: float | None
    size_bytes: int | None
    error: str | None