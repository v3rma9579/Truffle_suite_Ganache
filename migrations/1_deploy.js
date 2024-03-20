const reverse = artifacts.require('reverse');

module.exports = function (deployer) {
    deployer.deploy(reverse);
}