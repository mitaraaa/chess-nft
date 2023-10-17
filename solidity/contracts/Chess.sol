// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";

contract Chess is ERC721URIStorage, Ownable {
    uint256 private _nextTokenId;

    constructor(address initialOwner) ERC721("Kasparov's Legacy", "KSPV") Ownable(initialOwner) {}

    function mintNFT(address recipient, string memory tokenURI)
        public onlyOwner
        returns (uint256)
    {
        _nextTokenId++;

        uint256 newItemId = _nextTokenId++;
        _safeMint(recipient, newItemId);
        _setTokenURI(newItemId, tokenURI);

        return newItemId;
    }
}
