import { ethers } from "hardhat";

async function main() {
    const [deployer] = await ethers.getSigners();
    console.log("Deploying contracts with the account:", deployer.address);

    const Contract = await ethers.getContractFactory("Chess");
    const contract = await Contract.deploy(deployer.address);

    await contract.waitForDeployment();

    console.log("Token address:", await contract.getAddress());
}

main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error);
        process.exit(1);
    });
