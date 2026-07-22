import pandas as pd

# Load required files
fund_master = pd.read_csv("../data/raw/01_fund_master.csv")
scorecard = pd.read_csv("../reports/fund_scorecard.csv")

# Merge scorecard with risk category
recommendation_data = scorecard.merge(
    fund_master[["amfi_code", "scheme_name", "risk_category"]],
    on="amfi_code",
    how="left"
)

def recommend_funds(risk_level):
    recommendations = (
        recommendation_data[
            recommendation_data["risk_category"] == risk_level
        ]
        .sort_values("Sharpe_Ratio", ascending=False)
        .head(3)
    )

    return recommendations[
        [
            "scheme_name",
            "risk_category",
            "Sharpe_Ratio",
            "Fund_Score"
        ]
    ]

if __name__ == "__main__":
    print("Top Recommended Funds (Moderately High Risk)")
    print(recommend_funds("Moderately High"))