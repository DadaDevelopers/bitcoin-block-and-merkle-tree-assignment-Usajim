# Bitcoin Block and Merkle Tree Assignment
## Name: Mary 
---

## Overview
This assignment explores Bitcoin's block structure and Merkle tree construction
through hands-on inspection of a real Bitcoin block using mempool.space.

---

## Task 1: Block Inspection

I inspected Bitcoin Block 948,362 using mempool.space blockchain explorer.

### Key Findings
- Block Height    : 948,362
- Block Hash      : 00000000000000000001459c54f32ad19259af8d4b75876ff1851a37d8f36136
- Previous Hash   : 000000000000000000012fda74ca4615dc8fc0c01504cbb9276a39d961092c91
- Merkle Root     : 9ff862e464b708f70ba9016b90d94ed8ab33ce8b9453cabdaf7f7dfa1939f791
- Transactions    : 2,650
- Timestamp       : 2026-05-07 23:33:52
- Miner           : Foundry USA

Full details in block-inspection.md

---

## Task 2: Merkle Tree Construction

I constructed a Merkle tree using 4 real transaction hashes from Block 948,362.

### The 4 Transactions Used
- TxA (Coinbase): 8d5aba4db120f7c9dc586f4cc9125f9bd490d0a5cd97c4429007d849ecda08ee
- TxB           : 4a2b9afb30627d910b47b9c01e7c3fe760387aba6a699f36238092cd5ae52e48
- TxC           : ad584fa10b96946b30af9d42a9e999aa83a3305b74a6ffc8dd64030173a70931
- TxD           : 9d49e4aca797c31554051273029cf06cc292929e9bee9555df35cc134f132886


### How the Merkle Root is Calculated
Step 1: Hash(AB) = SHA256(SHA256(TxA + TxB))
Step 2: Hash(CD) = SHA256(SHA256(TxC + TxD))
Step 3: Merkle Root = SHA256(SHA256(Hash(AB) + Hash(CD)))

See code/merkle_tree.py for the full Python implementation.

---

## Key Learnings

1. Blocks are linked via hashes — changing any block breaks the entire chain
2. The Merkle root efficiently summarizes thousands of transactions in one hash
3. Proof of work requires the block hash to start with many zeros
4. Miners compete to find a nonce that produces a valid hash
5. The coinbase transaction is always the first transaction in every block

---

## Files
- README.md            : This main report
- block-inspection.md  : Detailed Task 1 findings
- code/merkle_tree.py  : Python Merkle tree implementation