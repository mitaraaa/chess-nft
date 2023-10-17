import { loadFixture } from "@nomicfoundation/hardhat-toolbox/network-helpers";
import { expect } from "chai";
import { ethers } from "hardhat";
import { Chess } from "../typechain-types/contracts/Chess";

describe("Chess", () => {
    const deployPollFixture = async () => {
        const [owner, otherAccount] = await ethers.getSigners();

        const Chess = await ethers.getContractFactory("Chess");

        const contract: Chess = await Chess.deploy(owner.address);

        return { contract, owner, otherAccount };
    };

    it("Should mint NFT", async () => {
        const { contract, owner } = await loadFixture(deployPollFixture);

        const response = await contract.mintNFT(
            owner.address,
            "https://bafkreig6kunk3lhzgg4qyc2xdaf6d4ixwkxopqvyta4gjkss7aimwquaqu.ipfs.w3s.link/"
        );

        expect(response)
            .to.emit(contract, "Transfer")
            .withArgs(owner.address, owner.address, 0);
    });

    it("Should transfer NFT", async () => {
        const { contract, owner, otherAccount } = await loadFixture(
            deployPollFixture
        );

        await contract.mintNFT(
            owner.address,
            "https://bafkreig6kunk3lhzgg4qyc2xdaf6d4ixwkxopqvyta4gjkss7aimwquaqu.ipfs.w3s.link/"
        );

        await contract.transferOwnership(otherAccount.address);

        const response = await contract.owner();

        expect(response).to.equal(otherAccount.address);
    });

    it("Should not transfer NFT", async () => {
        const { contract, owner, otherAccount } = await loadFixture(
            deployPollFixture
        );

        await contract.mintNFT(
            owner.address,
            "https://bafkreig6kunk3lhzgg4qyc2xdaf6d4ixwkxopqvyta4gjkss7aimwquaqu.ipfs.w3s.link/"
        );

        await expect(
            contract
                .connect(otherAccount)
                .transferOwnership(otherAccount.address)
        ).to.be.reverted;
    });
});
