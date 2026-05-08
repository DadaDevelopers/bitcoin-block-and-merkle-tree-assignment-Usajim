# Bitcoin Block and Merkle Tree Assignment
## Name: Mary

---

## Overview
This assignment explores Bitcoin's block structure and Merkle tree construction
through hands-on inspection of a real Bitcoin block using mempool.space.

---

## Task 1: Block Inspection
Full details and explanation in block-inspection.md

### Summary
- Block Height    : 948,362
- Block Hash      : 00000000000000000001459c54f32ad19259af8d4b75876ff1851a37d8f36136
- Previous Hash   : 000000000000000000012fda74ca4615dc8fc0c01504cbb9276a39d961092c91
- Merkle Root     : 9ff862e464b708f70ba9016b90d94ed8ab33ce8b9453cabdaf7f7dfa1939f791
- Transactions    : 2,650
- Timestamp       : 2026-05-07 23:33:52
- Miner           : Foundry USA

---

## Task 2: Merkle Tree Visualization
Full diagram and calculation in merkle-tree-diagram.md

---

## Key Learnings

**1. Blocks are linked by hashes**
Each block contains the hash of the previous block creating an unbreakable
chain. Changing any block would change its hash breaking every block after it.

**2. The Merkle root summarizes all transactions efficiently**
Instead of storing all 2,650 transaction hashes individually Bitcoin condenses
them into one single 32-byte Merkle root stored in the block header.

**3. Proof of work is visible in the block hash**
The block hash starts with many zeros (00000000000000000001...). Miners tried
billions of nonce values to find a hash with that many leading zeros.

**4. Merkle trees enable lightweight verification**
A mobile wallet does not need to download all 2,650 transactions to verify one
payment. A Merkle proof allows verification using only a few hashes.

**5. The coinbase transaction is always first**
TxA is the coinbase transaction, the reward Foundry USA received for mining
this block (3.146 BTC = block subsidy + transaction fees).