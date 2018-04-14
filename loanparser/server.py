from flask import Flask
app = Flask(__name__)

@app.route("/")
def loan_summary():
    return {
            "we_need": "€50k to fund working capital as we have just won a new contract to supply Waitrose",
            "we_do": [
                "Veganic is growing company supplying organic vegan ready meals",
                "Three years in operation with annual growth of 120%",
                "Full ethical supply chain with ingredients sourced from local certified organic producers",
                "Funded from owners equity, overdraft (UB) and LEO grant",
                ],
            "finances": [
                {
                    "year": "2016",
                    "sales": 50000,
                    "gross_profit": 25000,
                    "op_ex": 24500,
                    "profit": 500,
                    "debtors": 8333,
                    "creditors": -6250,
                    "cash_od": -2083,
                },

                {
                    "year": "2017",
                    "sales": 150000,
                    "gross_profit": 75000,
                    "op_ex": 73500,
                    "profit": 1500,
                    "debtors": 25000,
                    "creditors": -18750,
                    "cash_od": -6250,
                },

                {
                    "year": "2018",
                    "sales": 200000,
                    "gross_profit": 100000,
                    "op_ex": 84000,
                    "profit": 16000,
                    "debtors": 33333,
                    "creditors": -25000,
                    "cash_od": -8333,
                },

                {
                    "year": "2019",
                    "sales": 750000,
                    "gross_profit": 375000,
                    "op_ex": 300000,
                    "profit": 75000,
                    "debtors": 125000,
                    "creditors": -93750,
                    "cash_od": -31250,
                },
            ]

