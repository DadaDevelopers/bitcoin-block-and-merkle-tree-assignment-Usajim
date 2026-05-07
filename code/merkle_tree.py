"""
Assignment 6 - Task 2: Merkle Tree Construction
Bitcoin Block 948,362

This script demonstrates how Bitcoin builds a Merkle tree
from transaction hashes to produce the Merkle root.

Think of it like this:
- You have 4 transactions (TxA, TxB, TxC, TxD)
- You hash them in pairs: Hash(TxA+TxB) and Hash(TxC+TxD)
- Then hash those results together to get the Merkle Root
- This gives one single fingerprint for ALL transactions
"""

import hashlib


def double_sha256(data):
    """
    Bitcoin uses double SHA256 hashing everywhere.
    This means we run SHA256 twice on the same data.
    Why twice? Extra security against certain attacks.
    """
    first_hash = hashlib.sha256(data).digest()
    second_hash = hashlib.sha256(first_hash).digest()
    return second_hash


def hash_pair(hash_a, hash_b):
    """
    Combines two transaction hashes into one parent hash.

    Important: Bitcoin reverses the byte order (little-endian)
    before combining, then reverses back after hashing.
    This is a quirk of how Bitcoin was originally coded.

    Args:
        hash_a: First transaction hash (hex string)
        hash_b: Second transaction hash (hex string)

    Returns:
        Combined parent hash (hex string)
    """
    # Convert hex strings to bytes and reverse (little-endian)
    a_bytes = bytes.fromhex(hash_a)[::-1]
    b_bytes = bytes.fromhex(hash_b)[::-1]

    # Combine and double hash
    combined = a_bytes + b_bytes
    result = double_sha256(combined)

    # Reverse back to big-endian and return as hex
    return result[::-1].hex()


def build_merkle_tree(transactions):
    """
    Builds a complete Merkle tree from a list of transaction IDs.

    The process:
    1. Start with all transaction hashes (leaves)
    2. Hash them in pairs to get the next level
    3. If odd number, duplicate the last hash
    4. Repeat until only one hash remains (the root)

    Args:
        transactions: List of transaction ID hex strings

    Returns:
        The Merkle root as a hex string
    """
    if len(transactions) == 0:
        return None

    if len(transactions) == 1:
        return transactions[0]

    current_level = transactions
    level_number = 1

    while len(current_level) > 1:
        print(f"\n  Level {level_number} ({len(current_level)} hashes):")
        for i, h in enumerate(current_level):
            print(f"    [{i}] {h[:16]}...{h[-8:]}")

        next_level = []

        # If odd number of hashes, duplicate the last one
        if len(current_level) % 2 != 0:
            print(f"    (Odd number — duplicating last hash)")
            current_level.append(current_level[-1])

        # Hash each pair
        for i in range(0, len(current_level), 2):
            left = current_level[i]
            right = current_level[i + 1]
            parent = hash_pair(left, right)
            print(f"    Hash({left[:8]}... + {right[:8]}...) = {parent[:16]}...")
            next_level.append(parent)

        current_level = next_level
        level_number += 1

    return current_level[0]


# ============================================================
# REAL TRANSACTION HASHES FROM BITCOIN BLOCK 948,362
# ============================================================

print("=" * 65)
print("  MERKLE TREE CONSTRUCTION — Bitcoin Block 948,362")
print("=" * 65)

# 4 real transaction IDs from Block 948,362
transactions = [
    "8d5aba4db120f7c9dc586f4cc9125f9bd490d0a5cd97c4429007d849ecda08ee",  # TxA Coinbase
    "4a2b9afb30627d910b47b9c01e7c3fe760387aba6a699f36238092cd5ae52e48",  # TxB
    "ad584fa10b96946b30af9d42a9e999aa83a3305b74a6ffc8dd64030173a70931",  # TxC
    "9d49e4aca797c31554051273029cf06cc292929e9bee9555df35cc134f132886",   # TxD
]

print(f"""
Block Details:
--------------
Block Height : 948,362
Timestamp    : 2026-05-07 23:33:52
Miner        : Foundry USA
Transactions : 2,650 total (using first 4 for demonstration)

The 4 Transaction IDs (Leaves of the Merkle Tree):
---------------------------------------------------
TxA (Coinbase): {transactions[0]}
TxB           : {transactions[1]}
TxC           : {transactions[2]}
TxD           : {transactions[3]}
""")

print("Building Merkle Tree...")
print("-" * 65)

# Build the tree
calculated_root = build_merkle_tree(transactions)

print(f"""
{"-" * 65}
Merkle Tree Structure:
----------------------

                    Merkle Root
                        |
            +-----------+-----------+
            |                       |
        Hash(TxA+TxB)         Hash(TxC+TxD)
            |                       |
        +---+---+               +---+---+
        |       |               |       |
       TxA     TxB             TxC     TxD

Calculated Merkle Root:
  {calculated_root}

Note: This is calculated from only 4 of the 2,650 transactions.
The actual block Merkle root uses all 2,650 transactions.
The real block Merkle root is:
  9ff862e464b708f70ba9016b90d94ed8ab33ce8b9453cabdaf7f7dfa1939f791

Key Insight:
  Even a tiny change to any transaction would completely change
  the Merkle root — making tampering immediately detectable!
{"-" * 65}
""")