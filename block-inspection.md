# Block Inspection Results
## Block 948,362 — Bitcoin Mainnet

------------------------
Block Height        : 948,362
Block Hash          : 00000000000000000001459c54f32ad19259af8d4b75876ff1851a37d8f36136
Previous Block Hash : 000000000000000000012fda74ca4615dc8fc0c01504cbb9276a39d961092c91
Merkle Root         : 9ff862e464b708f70ba9016b90d94ed8ab33ce8b9453cabdaf7f7dfa1939f791
Number of Transactions: 2,650
Timestamp           : 2026-05-07 23:33:52
Miner               : Foundry USA
Size                : 1.76 MB
Weight              : 3.99 MWU
Total Fees          : 0.021 BTC
Difficulty          : 132472011079030.5

------------------------

## What Each Field Means

### Block Height: 948,362
This is the position of the block in the blockchain.
Block 948,362 means 948,362 blocks have been mined before this one.
Think of it like a page number in a book.

### Block Hash: 00000000000000000001459c54f32ad...
This is the unique fingerprint of this block.
It is calculated by running the block header through SHA256 twice.
Notice it starts with many zeros, this is proof of work.
Miners had to try billions of times to find a hash starting with so many zeros.

### Previous Block Hash: 000000000000000000012fda74ca46...
This is the fingerprint of the block that came before this one (block 948,361).
This is how blocks are chained together, each block points to its parent.
If anyone tried to change block 948,361, its hash would change,
breaking the link to block 948,362 and every block after it.
This is what makes Bitcoin immutable.

### Merkle Root: 9ff862e464b708f70ba9016b90d94ed8...
This is a single hash that represents ALL 2,650 transactions in this block.
It is calculated by building a Merkle tree from all transaction hashes.
If even one transaction changed, the Merkle root would completely change.
This allows lightweight verification of any transaction without downloading the full block.

### Number of Transactions: 2,650
This block contains 2,650 transactions.
The first transaction is always the coinbase transaction —
the reward paid to the miner (Foundry USA) for mining this block.

### Timestamp: 2026-05-07 23:33:52
The time when this block was mined.
Bitcoin targets one new block every 10 minutes on average.

------------------------

## Key Insights

1. The block hash starts with many zeros (00000000000000000001...)
   This is proof of work, miners had to find a special number (nonce)
   that makes the hash start with enough zeros to meet the difficulty target.

2. The previous block hash links this block to block 948,361.
   This chain of hashes going all the way back to block 0 is what makes
   Bitcoin tamper-proof, changing any block breaks all blocks after it.

3. The Merkle root summarizes all 2,650 transactions in just one hash.
   This is extremely efficient, you can prove any transaction is in this
   block without downloading all 2,650 transactions.
