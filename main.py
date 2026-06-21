# =============================================================================
# ACTIVIDAD: Aprendizaje Autónomo 2 — Lógica de Programación
# DESCRIPCIÓN: Sistema Automatizado de Gestión de Ventas e Inventario
# ARCHIVO: main.py
# =============================================================================

def ejecutar_sistema():
    # 1. Inicialización de variables de stock simuladas y precios
    stock_producto_A = 15
    stock_producto_B = 10
    
    precio_A = 25.00  # Precio unitario Producto A
    precio_B = 40.00  # Precio unitario Producto B
    
    total_venta = 0.0
    continuar_compra = "si"
    
    print("=== BIENVENIDO AL SISTEMA DE GESTIÓN DE VENTAS UIDE ===")
    
    # 2. ESTRUCTURA REPETITIVA (BUCLE): Controla el flujo continuo de la compra
    while continuar_compra.lower() == "si":
        print("\nProductos Disponibles:")
        print(f"1. Producto A - Precio: ${precio_A} (Stock: {stock_producto_A})")
        print(f"2. Producto B - Precio: ${precio_B} (Stock: {stock_producto_B})")
        
        opcion = input("\nSeleccione el número del producto que desea comprar (1 o 2): ")
        
        # 3. ESTRUCTURA CONDICIONAL: Validación y procesamiento de la selección
        if opcion == "1":
            cantidad = int(input(f"Ingrese la cantidad que desea del Producto A (Máx {stock_producto_A}): "))
            
            # Condicional anidada para validar la disponibilidad real del stock
            if cantidad <= stock_producto_A and cantidad > 0:
                subtotal_item = cantidad * precio_A
                stock_producto_A -= cantidad  # Actualización del inventario
                total_venta += subtotal_item
                print(f"-> Añadido con éxito. Subtotal: ${subtotal_item:.2f}")
            else:
                print("[ERROR] Cantidad no válida o supera el stock disponible.")
                
        elif opcion == "2":
            cantidad = int(input(f"Ingrese la cantidad que desea del Producto B (Máx {stock_producto_B}): "))
            
            if cantidad <= stock_producto_B and cantidad > 0:
                subtotal_item = cantidad * precio_B
                stock_producto_B -= cantidad  # Actualización del inventario
                total_venta += subtotal_item
                print(f"-> Añadido con éxito. Subtotal: ${subtotal_item:.2f}")
            else:
                print("[ERROR] Cantidad no válida o supera el stock disponible.")
                
        else:
            print("[ALERTA] Opción de producto inválida. Intente nuevamente.")
            
        # Pregunta de control para continuar o romper el bucle 'while'
        continuar_compra = input("\n¿Desea agregar otro producto al carrito? (si/no): ")
    
    # 4. ESTRUCTURA CONDICIONAL AVANZADA: Aplicación de descuentos por volumen
    print("\n==============================================")
    print(f"Subtotal Bruto de la Venta: ${total_venta:.2f}")
    
    descuento = 0.0
    if total_venta >= 150.00:
        descuento = total_venta * 0.15  # 15% de descuento por compras altas
        print("¡Felicidades! Se aplicó un 15% de descuento por superar los $150.")
    elif total_venta >= 50.00:
        descuento = total_venta * 0.05  # 5% de descuento
        print("Se aplicó un 5% de descuento por superar los $50.")
    else:
        print("No se registran descuentos aplicables para este monto.")
        
    monto_final = total_venta - descuento
    print(f"Descuento Total: -${descuento:.2f}")
    print(f"TOTAL NETO A PAGAR: ${monto_final:.2f}")
    print("==============================================")
    print("Transacción finalizada con éxito. Inventario actualizado.")

if __name__ == "__main__":
    ejecutar_sistema()