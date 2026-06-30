class SmartCard:
    def __init__(self):
        self.lambda_value = None
        self.eta = None
        self.zeta = None
        self.public_key = None

    def display(self):
        print("\n===== Smart Card =====")
        print("Lambda :", self.lambda_value)
        print("Eta    :", self.eta)
        print("Zeta   :", self.zeta)
        print("PK      :", self.public_key)