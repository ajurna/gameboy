from classes import Instruction, Operand
import json
from pathlib import Path


def parse_opcode_data(opcode_data):
    instructions = {}
    for opcode, opcode_info in opcode_data.items():
        opcode_number = int(opcode, base=16)
        instruction = Instruction(
            opcode=opcode_number,
            immediate=opcode_info['immediate'],
            operands=[
                Operand(
                    immediate=x['immediate'],
                    name=x['name'],
                    bytes=x.get('bytes', 0),
                    value=x.get('value', None),
                    adjust=x.get('adjust', None)
                ) for x in opcode_info['operands']
            ],
            cycles=opcode_info['cycles'],
            bytes=opcode_info['bytes'],
            mnemonic=opcode_info['mnemonic']
        )
        instructions[opcode_number] = instruction
    return instructions


instruction_data = json.load(Path('Opcodes.json').open('r'))

unprefixed_instructions = parse_opcode_data(instruction_data['unprefixed'])
cbprefixed_instructions = parse_opcode_data(instruction_data['cbprefixed'])

print()