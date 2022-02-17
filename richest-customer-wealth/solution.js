/**
 * @param {number[][]} accounts
 * @return {number}
 */
 var maximumWealth = function(accounts) {
    let max = -Infinity;
    accounts.map(accountsForCustomer => {
        let sum = 0;
        accountsForCustomer.forEach(amount => sum+=amount);
        return sum;
    }).forEach(sumForCustomer => sumForCustomer > max ? max = sumForCustomer : max = max)
    return max;
};
