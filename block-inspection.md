# Task 1: Block Inspection Results
## Bitcoin Block 948,362 — Inspected via mempool.space

---

## Block Inspection Results

Block Inspection Results
Block Height          : 948,362
Block Hash            : 00000000000000000001459c54f32ad19259af8d4b75876ff1851a37d8f36136
Previous Block Hash   : 000000000000000000012fda74ca4615dc8fc0c01504cbb9276a39d961092c91
Merkle Root           : 9ff862e464b708f70ba9016b90d94ed8ab33ce8b9453cabdaf7f7dfa1939f791
Number of Transactions: 2,650
Timestamp             : 2026-05-07 23:33:52


---

## What Each Field Means

**Block Height (948,362)**
This is the position of the block in the blockchain, like a page number in a
book. Block 0 is the very first Bitcoin block ever mined (the Genesis block).
Block 948,362 means 948,362 blocks have been mined before this one.

**Block Hash (000000...8f36136)**
This is the unique fingerprint of this block produced by running the block
header through SHA256 twice. Notice it starts with many zeros, this is proof
of work. Miners tried billions of combinations to find a hash starting with
enough zeros to meet the difficulty target.

**Previous Block Hash (000000...1092c91)**
This is the fingerprint of block 948,361, the block that came before this one.
This is how blocks are chained together. If anyone tried to change block
948,361 its hash would change breaking the link to block 948,362 and every
block after it. This is what makes Bitcoin tamper-proof and immutable.

**Merkle Root (9ff862e4...1939f791)**
A single hash representing ALL 2,650 transactions in this block. It is
calculated by building a Merkle tree from all transaction hashes. If even one
transaction changed the Merkle root would completely change. This allows
lightweight verification of any transaction without downloading the full block.

**Number of Transactions (2,650)**
This block contains 2,650 transactions. The very first transaction is always
the coinbase transaction — the mining reward paid to Foundry USA for
successfully mining this block.

**Timestamp (2026-05-07 23:33:52)**
The time when this block was mined. Bitcoin targets a new block every 10
minutes on average.

---

## Process and Findings

### How I Found This Block
1. Visited mempool.space on a browser
2. Identified the confirmed (blue) blocks on the right side of the homepage
3. Clicked on Block 948,362 mined by Foundry USA
4. Recorded all block header details from the block page
5. Copied the Previous Block Hash by navigating to block 948,361

### Key Finding
The block hash starts with 18 leading zeros
(00000000000000000001...). This represents an enormous amount of
computational work, miners had to try billions of nonce values before finding
a hash that met the difficulty requirement. This is the proof of work that
secures the Bitcoin network.