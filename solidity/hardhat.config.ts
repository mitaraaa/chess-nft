import "@nomicfoundation/hardhat-toolbox";
import { config as envConfig } from "dotenv";
import { HardhatUserConfig } from "hardhat/types";

envConfig();

const INFURA_API_KEY = process.env.INFURA_API_KEY || "";
const SEPOLIA_PRIVATE_KEY = process.env.SEPOLIA_PRIVATE_KEY || "";
const LOCALHOST_PRIVATE_KEY = process.env.LOCALHOST_PRIVATE_KEY || "";

const config: HardhatUserConfig = {
    solidity: "0.8.20",
    networks: {
        sepolia: {
            url: `https://sepolia.infura.io/v3/${INFURA_API_KEY}`,
            accounts: [SEPOLIA_PRIVATE_KEY],
        },
    },
};

export default config;
