// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

/**
 * @title Storage
 * @dev Store & retrieve value in a variable
 */
contract GreenPass {
    enum GreenPassStatus {
        Expired,
        Valid
    }
    GreenPassStatus public status;

    mapping(uint256 => Pass) public passs;
    mapping(uint256 => uint256) public indexes;
    uint256 public count = 0;
    uint256 internal day = 86400;

    address owner;
    uint256 validatedIn = 1613820891;

    modifier onlyOwner() {
        require(msg.sender == owner);
        _;
    }
    struct Pass {
        string firstName;
        string lastName;
        uint256 id;
        uint256 expiration;
    }

    constructor() {
        owner = msg.sender;
    }

    function addGreenPass (
        string memory _firstName,
        string memory _lastName,
        uint256 _id,
        uint256 _expiration
    ) public onlyOwner{
        uint256 expiration_date = block.timestamp + (day * _expiration);
        incrementCount();
        indexes[count] = _id;
        passs[_id] = Pass(_firstName, _lastName, _id, expiration_date);
    }

    function incrementCount() internal {
        count++;
    }

    function isOwner() view public returns(bool) {
        return msg.sender == owner;
    }

    function updateExpiration(uint256 _id,uint256 _expiration)
        public onlyOwner
    {
        passs[_id].expiration = _expiration + (day * 30);
    }
}