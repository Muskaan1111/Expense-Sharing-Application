from enum import Enum
from datetime import datetime
import uuid

class SplitType(Enum):
    EQUAL = "EQUAL"
    EXACT = "EXACT"
    PERCENT = "PERCENT"

class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
    def to_dict(self):
        return {"user_id": self.user_id, "name": self.name}

class Expense:
    def __init__(self, amount, payer_id, category, split_type, splits):
        self.id = str(uuid.uuid4())
        self.amount = amount
        self.payer_id = payer_id
        self.category = category
        self.split_type = split_type
        self.splits = splits
        self.timestamp = datetime.now()

class ExpenseManager:
    def __init__(self):
        self.users = {}       
        self.user_balances = {} 
        self.activity_log = []  

    def add_user(self, user_id, name, email):
        if user_id in self.users:
            raise ValueError(f"User {user_id} already exists.")
        
        # --- FIXED: Created the object and returning it ---
        new_user = User(user_id, name, email)
        self.users[user_id] = new_user
        self.user_balances[user_id] = 0.0
        return new_user 

    def create_expense(self, split_type, amount, payer_id, split_data, category="General"):
        if payer_id not in self.users: raise ValueError("Payer not found")
        
        splits = self._calculate_splits(split_type, amount, split_data)

        self.user_balances[payer_id] += amount
        for split in splits:
            uid = split['user_id']
            if uid not in self.users: raise ValueError(f"User {uid} not found")
            self.user_balances[uid] -= split['amount']

        self.activity_log.append({
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "category": category,
            "amount": amount,
            "details": f"Paid by {self.users[payer_id].name} for {category}"
        })

    def get_history(self):
        return self.activity_log

    def simplify_debts(self):
        debtors = []
        creditors = []
        for uid, amount in self.user_balances.items():
            if amount < -0.01: debtors.append({'id': uid, 'amount': amount})
            elif amount > 0.01: creditors.append({'id': uid, 'amount': amount})

        transactions = []
        i = 0 
        j = 0 
        while i < len(debtors) and j < len(creditors):
            debtor = debtors[i]
            creditor = creditors[j]
            amount = min(abs(debtor['amount']), creditor['amount'])

            transactions.append({
                "from": self.users[debtor['id']].name,
                "to": self.users[creditor['id']].name,
                "amount": round(amount, 2)
            })

            debtor['amount'] += amount       
            creditor['amount'] -= amount     

            if abs(debtor['amount']) < 0.01: i += 1
            if creditor['amount'] < 0.01: j += 1
        return transactions

    def _calculate_splits(self, split_type, amount, split_data):
        splits = []
        if split_type == SplitType.EQUAL.value:
            count = len(split_data)
            share = round(amount / count, 2)
            splits = [{'user_id': s['user_id'], 'amount': share} for s in split_data]
            splits[0]['amount'] += amount - (share * count)
        elif split_type == SplitType.EXACT.value:
            splits = split_data
        elif split_type == SplitType.PERCENT.value:
             splits = [{'user_id': s['user_id'], 'amount': (amount * s['percent'] / 100.0)} for s in split_data]
        return splits