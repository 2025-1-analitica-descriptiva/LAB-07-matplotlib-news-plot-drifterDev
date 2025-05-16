"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """

    import os
    import pandas as pd
    import matplotlib.pyplot as plt

    datos = pd.read_csv("files/input/news.csv", index_col=0)

    estilo_lineas = {
        "Television": {"color": "dimgray", "ancho": 2, "z": 1},
        "Newspaper": {"color": "grey", "ancho": 2, "z": 1},
        "Internet": {"color": "tab:blue", "ancho": 3, "z": 2},
        "Radio": {"color": "lightgrey", "ancho": 2, "z": 1},
    }

    fig, ax = plt.subplots()

    for medio, props in estilo_lineas.items():
        ax.plot(
            datos[medio],
            label=medio,
            color=props["color"],
            linewidth=props["ancho"],
            zorder=props["z"],
        )

    ax.set_title("How people get their news", fontsize=16)
    ax.spines["top"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.get_yaxis().set_visible(False)

    anio_inicio, anio_fin = datos.index[0], datos.index[-1]

    for medio, props in estilo_lineas.items():
        y_inicio = datos.loc[anio_inicio, medio]
        y_fin = datos.loc[anio_fin, medio]

        ax.scatter(anio_inicio, y_inicio, color=props["color"], zorder=props["z"])
        ax.text(anio_inicio - 0.2, y_inicio, f"{medio} {y_inicio}%", ha="right", va="center", color=props["color"])

        ax.scatter(anio_fin, y_fin, color=props["color"], zorder=props["z"])
        ax.text(anio_fin + 0.2, y_fin, f"{y_fin}%", ha="left", va="center", color=props["color"])

    plt.tight_layout()

    os.makedirs("files/plots", exist_ok=True)
    plt.savefig("files/plots/news.png")
    plt.show()

pregunta_01()

