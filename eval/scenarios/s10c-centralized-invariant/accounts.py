"""Account model for creditline."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Account:
    id: str
    credit_limit: int
