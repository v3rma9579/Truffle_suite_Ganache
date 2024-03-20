// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract reverse {
    int rev;
    constructor() {
        rev = 0;
    }

    function reverseDigits(int a) public {
        int temp = a;
        int r = 0;
        while (temp > 0) {
            int lastDigit = temp % 10;
            r = r * 10 + lastDigit;
            temp /= 10;
        }
        rev = r;
    }

    function getResult() public view returns (int) {
        return rev;
    }
}
