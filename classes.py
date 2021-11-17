from dataclasses import dataclass
from typing import Literal


@dataclass(frozen=True)
class Operand:

    immediate: bool
    name: str
    bytes: int
    value: int | None
    adjust: Literal["+", "-"] | None


@dataclass
class Instruction:

    opcode: int
    immediate: bool
    operands: list[Operand]
    cycles: list[int]
    bytes: int
    mnemonic: str
    comment: str = ""