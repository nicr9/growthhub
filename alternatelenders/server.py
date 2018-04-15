import copy
import requests
import os

from enum import Enum
from flask import Flask, jsonify

app = Flask(__name__)

class reason(Enum):
    INVOICE = 1
    SUPPLY = 2
    GROWTH = 3
    FACTORING = 4
    EQUITY = 5
    UNSECURED = 6
    SLOW_PAYERS = 7
    WHEELED_ASSET = 8
    SPECIALIST_ASSET = 9
    ASSET = 10

lenders = [
        {
            "name": "Accerelated Payments",
            "loan_types": {
                reason.INVOICE,
                reason.FACTORING,
                reason.SLOW_PAYERS,
            },
            "max": 250000,
            "min": 25000,
            "rates": "5% to 10%",
        },
        {
            "name": "Supply Finance",
            "loan_types": {
                reason.INVOICE,
                reason.SUPPLY,
                reason.FACTORING,
                reason.SLOW_PAYERS,
            },
            "max": 250000,
            "min": 25000,
            "rates": "5% to 10%",
        },
        {
            "name": "Peer Finance",
            "loan_types": {
                reason.GROWTH,
                reason.UNSECURED,
                reason.WHEELED_ASSET,
                reason.SPECIALIST_ASSET,
                reason.ASSET,
            },
            "max": 100000,
            "min": 10000,
            "rates": "5% to 10%",
        },
        {
            "name": "Crowd Me",
            "loan_types": {
                reason.GROWTH,
                reason.UNSECURED,
                reason.WHEELED_ASSET,
                reason.SPECIALIST_ASSET,
                reason.ASSET,
            },
            "max": 25000,
            "min": 5000,
            "rates": "5% to 10%",
        },
        {
            "name": "Prop Fund",
            "loan_types": {},
            "max": 250000,
            "min": 150000,
            "rates": "5% to 10%",
        },
        {
            "name": "Vans Etc",
            "loan_types": {
                reason.WHEELED_ASSET,
            },
            "max": 40000,
            "min": 15000,
            "rates": "5% to 10%",
        },
    ]

@app.route("/")
def select_lenders():
    """
    Input:
    {
        loan_id: [a-zA-Z0-9],
        debtors: [
            {
                name: string,
                value: [0-9],
            },
            ...
        ],
        loan: {
            type: reason.*,
            ammount: [0-9],
        },
        ...
    }

    Return:
    {
        "lenders": [
            {
                "name": lenders.*,
                "rates": string,
                "reasons": [string, ...],
            },
            ...
        ]
    }
    """

    # POST data
    inp = {
        "loan_id": "abc123",
        "debtors": [
            {
                "name": "debtor01",
                "value": 1000,
            },
            {
                "name": "debtor02",
                "value": 1000,
            },
            {
                "name": "debtor03",
                "value": 1000,
            },
            {
                "name": "debtor04",
                "value": 1000,
            },
            {
                "name": "debtor05",
                "value": 1000,
            },
        ],
        "loan": {
            "type": reason.SLOW_PAYERS,
            "ammount": 30000,
        },
    }

    # Initialise results
    results = {
            "lenders": [],
            "application_summary": get_loan_summary(inp['loan_id']),
            }

    for i, lender in enumerate(lenders):
        profile = {
                "name": lender['name'],
                "rates": lender['rates'],
                "reasons": [],
                }

        # Reject loans types the lender doesn't support
        if inp['loan']['type'] not in lender['loan_types']:
            profile['reasons'].append("Lender does not offer loans for that purpose")

        ammount = inp['loan']['ammount']
        if (ammount < lender['min']) or (ammount > lender['max']):
            profile['reasons'].append("Lender does not offer loans within that range")

        # Append to results
        results['lenders'].append(profile)

    return jsonify(results)

def get_loan_summary(loan_id):
    url = os.getenv("LOAN_PARSER", "http://127.0.0.1:5001/")
    resp = requests.get(url)

    return resp.json()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
