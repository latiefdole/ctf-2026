import struct

# Extracted bytecode from .rodata starting at offset 0x40 (size 311 - 64 = 247)
def get_bytecode():
    filepath = r'C:\Users\ICT-12\Documents\CTF\w3d3\vm2_chall'
    with open(filepath, 'rb') as f:
        elf = f.read()
    
    # .rodata offset: 8192, bytecode offset inside .rodata: 64
    bytecode_start = 8192 + 64
    # The bytecode size: we read 247 bytes
    bytecode = elf[bytecode_start : bytecode_start + 247]
    return bytecode

def simulate_raw_operands(bytecode):
    print("\n--- Simulating with Raw Operands ---")
    pc = 0
    stack = []
    output = []
    steps = 0
    
    while pc < len(bytecode) and steps < 1000:
        op = bytecode[pc]
        if op == 0x01: # PUSH
            val = bytecode[pc+1]
            stack.append(val)
            pc += 2
        elif op == 0x02: # POP
            if stack:
                stack.pop()
            pc += 1
        elif op == 0x03: # XOR
            if len(stack) >= 2:
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(v1 ^ v2)
            pc += 1
        elif op == 0x04: # PRINT
            if stack:
                val = stack.pop()
                output.append(chr(val))
            pc += 1
        elif op == 0x05: # JMP
            offset = bytecode[pc+1]
            if offset > 127:
                offset -= 256
            pc = pc + 2 + offset
        elif op == 0x06: # HALT
            print("HALT reached.")
            break
        else:
            print(f"Unknown opcode 0x{op:02x} at PC={pc}")
            break
        steps += 1
        
    print(f"Output: {''.join(output)}")
    print(f"Final stack: {stack}")

def simulate_lookup_operands(bytecode):
    print("\n--- Simulating with Lookup Operands ---")
    pc = 0
    stack = []
    output = []
    steps = 0
    
    while pc < len(bytecode) and steps < 1000:
        op = bytecode[pc]
        if op == 0x01: # PUSH
            idx = bytecode[pc+1]
            val = bytecode[idx]
            stack.append(val)
            pc += 2
        elif op == 0x02: # POP
            if stack:
                stack.pop()
            pc += 1
        elif op == 0x03: # XOR
            if len(stack) >= 2:
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(v1 ^ v2)
            pc += 1
        elif op == 0x04: # PRINT
            if stack:
                val = stack.pop()
                output.append(chr(val))
            pc += 1
        elif op == 0x05: # JMP
            idx = bytecode[pc+1]
            offset = bytecode[idx]
            if offset > 127:
                offset -= 256
            pc = pc + 2 + offset
        elif op == 0x06: # HALT
            print("HALT reached.")
            break
        else:
            print(f"Unknown opcode 0x{op:02x} at PC={pc}")
            break
        steps += 1
        
    print(f"Output: {''.join(output)}")
    print(f"Final stack: {stack}")

if __name__ == '__main__':
    bytecode = get_bytecode()
    print(f"Bytecode length: {len(bytecode)} bytes")
    print(f"Bytecode hex: {bytecode.hex()}")
    
    simulate_raw_operands(bytecode)
    simulate_lookup_operands(bytecode)
