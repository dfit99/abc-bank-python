class Bank:
    def __init__(self):
        self.customers = []

    def addCustomer(self, customer):
        self.customers.append(customer)

    def customerSummary(self):
        summary = ''.join(["\n - {} ({})".format(c.name, self._format(c.numAccs(), "account"))
                           for c in self.customers])
        return "Customer Summary{summary}" .format(summary=summary)

    def _format(self, number, word):
        return str(number) + " " + (word if (number == 1) else word + "s")

    def totalInterestPaid(self):
        total = 0
        for c in self.customers:
            total += c.totalInterestEarned()
        return total