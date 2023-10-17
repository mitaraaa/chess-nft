# Kasparov's Legacy NFT Collection

<p align="center">
    <img src="https://i.seadn.io/s/raw/files/964981610452af55dc72619ef043c6ae.png?auto=format&dpr=1&w=1920" />
</p>

This repository contains the Kasparov's Legacy NFT Collection. The collection consists of 56 unique NFTs, each representing a unique chess position from Garry Kasparov's career. The NFTs are generated using a custom algorithm that takes a chess position as input and outputs a unique image. The NFTs are stored on the Sepolia testnet blockchain and can be viewed on [Opensea](https://testnets.opensea.io/collection/kasparov-s-legacy-1).

## How to generate the NFTs

The NFTs are generated using a custom algorithm that takes a chess position as input and outputs a unique image. The algorithm is implemented in Python and uses the [python-chess](https://python-chess.readthedocs.io/en/latest/) library to parse the chess positions. The algorithm is implemented in the `generate.py` file. The algorithm is deterministic, meaning that the same input will always produce the same output.

## How to mint the NFTs

The NFTs are minted using the [Sepolia](https://sepolia.io/) blockchain. The NFTs are stored on the Sepolia testnet blockchain and can be viewed on [Opensea](https://testnets.opensea.io/collection/kasparov-s-legacy-1). The NFTs are minted using the `mint.py` file. The `mint.py` file uses the [Hardhat](https://hardhat.org/) framework to interact with the Sepolia blockchain.

To mint the NFTs, you need to have a [Metamask](https://metamask.io/) wallet with some Sepolia testnet ETH. You can get some Sepolia testnet ETH from the [Sepolia faucet](https://faucet.sepolia.io/). You also need to have [Node.js](https://nodejs.org/en/) installed on your computer.

Before running, make sure to create a `.env` file in the root directory of the project and add the following environment variables:

```sh
INFURA_API_KEY=< your_api_key >
SEPOLIA_PRIVATE_KEY=< your_wallet_private_key >
CONTRACT_ADDRESS=< deployed_contract_address >
OWNER_ADDRESS=< your_wallet_address >
```

```sh
# Install dependencies
yarn install

# Compile the smart contract
npx hardhat compile

# Deploy the smart contract
npx hardhat run scripts/deploy.ts --network sepolia

# Mint the NFTs
npx hardhat run scripts/mint.ts --network sepolia
```

## How to run the tests

```sh
# Run the tests
npx hardhat test

# Run the tests with coverage
npx hardhat coverage
```
