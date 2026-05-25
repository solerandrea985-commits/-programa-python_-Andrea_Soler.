# CURSO: Fundamentos de Programación (213022)
# FASE 5: Evaluación Final POA - Banco de Problemas
# PROBLEMA SELECCIONADO: Problema 3 - Auditoría de Inventario
# ESTUDIANTE: Luisa Andrea Soler Suarez
# ==============================================================================

def calcular_cantidad_a_pedir(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0

def main():
    matriz_inventario = [
        ["ART01", "Papas", 12, 20],
        ["ART02", "Tomates", 35, 30],
        ["ART03", "Cebollas", 5, 15],
        ["ART04", "Zanahorias", 40, 25],
        ["ART05", "Lechuga", 2, 10]
    ]
    
    print("==================================================")
    print("       UNAD - FUNDAMENTOS DE PROGRAMACIÓN         ")
    print("   INFORME DE AUDITORÍA Y REABASTECIMIENTO        ")
    print("==================================================")
    print(f"{'PRODUCTO':<18} | {'CANTIDAD A PEDIR':<18}")
    print("--------------------------------------------------")
    
    for fila in matriz_inventario:
        nombre_articulo = fila[1]
        stock_actual = fila[2]
        stock_minimo = fila[3]
        
        cantidad_final = calcular_cantidad_a_pedir(stock_actual, stock_minimo)
        print(f"{nombre_articulo:<18} | {cantidad_final:<18}")
        
    print("==================================================")

if __name__ == "__main__":
    main()
