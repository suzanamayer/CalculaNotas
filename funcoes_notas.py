def media_ponderada_tres_notas(nota1, nota2, nota3):
    """
    Calcula a média ponderada de três avaliações,
    com pesos 2, 3 e 5, respectivamente.
    """

    # Processamento
    media = (nota1 * 2 + nota2 * 3 + nota3 * 5) / (2 + 3 + 5)

    return media