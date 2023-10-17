import { config } from "dotenv";
import * as fs from "fs";
import { ethers } from "hardhat";
import contractJSON from "../artifacts/contracts/Chess.sol/Chess.json";

config();

const address = "0x24368A68cBcc2F2446A5A301adbFCC9189424369";

const main = async () => {
    const wallet = new ethers.Wallet(
        process.env.SEPOLIA_PRIVATE_KEY!,
        ethers.provider
    );
    const signer = wallet.connect(ethers.provider);

    const contract = new ethers.Contract(
        process.env.CONTRACT_ADDRESS!,
        contractJSON.abi,
        signer
    );

    const cids = JSON.parse(
        fs.readFileSync("../generation/out/cids.json").toString()
    );

    for (const cid of cids) {
        console.log("https://" + cid + ".ipfs.w3s.link");

        const tx = await contract.mintNFT(
            process.env.OWNER_ADDRESS!,
            "https://" + cid + ".ipfs.w3s.link"
        );

        tx.wait(10);
    }
};

main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error);
        process.exit(1);
    });
