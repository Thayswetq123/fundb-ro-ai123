import pandas as pd
import os


def save_progress(weight, calories):

    data = {
        "Gewicht": [weight],
        "Kalorien": [calories]
    }

    df = pd.DataFrame(data)

    file_exists = os.path.isfile("progress.csv")

    df.to_csv(
        "progress.csv",
        mode="a",
        header=not file_exists,
        index=False
    )
