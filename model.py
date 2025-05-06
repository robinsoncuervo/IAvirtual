from sklearn.linear_model import LinearRegression
import pandas as pd

def seleccionar_top3_freelancers(data, tarifa_deseada, valoracion_deseada):
    if not data:
        return []

    df = pd.DataFrame(data)

    # Validación de columnas necesarias
    required_cols = ["Valoración", "tarifa", "Experiencia", "habilidades"]
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Falta la columna '{col}' en los datos.")

    df = df.dropna(subset=["Valoración", "tarifa", "Experiencia"])

    # Variables predictoras
    X = df[["Valoración", "tarifa", "Experiencia"]]

    # Variable objetivo: minimizar distancia respecto a los valores deseados
    y = -((df["tarifa"] - tarifa_deseada) ** 2 + (df["Valoración"] - valoracion_deseada) ** 2)

    # Modelo de regresión
    model = LinearRegression()
    model.fit(X, y)

    df["score"] = model.predict(X)
    top3 = df.sort_values(by="score", ascending=False).head(3)

    return top3.to_dict(orient="records")
