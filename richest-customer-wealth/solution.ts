function maximumWealth(accounts: number[][]): number {
    let max: number = -Infinity;
    accounts.map((accountsForCustomer: number[]): number => {
        let sum: number = 0;
        accountsForCustomer.forEach(amount => sum+=amount);
        return sum;
    }).forEach((sumForCustomer: number) => sumForCustomer > max ? max = sumForCustomer : max = max)
    return max;
};
