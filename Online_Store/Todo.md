### Tablas de la Base de Datos:

1. **Usuarios:**
   * `usuario_id` (clave primaria)
   * `nombre`
   * `correo electrónico`
   * `contraseña`
   * `fecha_registro`
2. **Categorías:**
   * `categoria_id` (clave primaria)
   * `nombre`
3. **Productos:**
   * `producto_id` (clave primaria)
   * `nombre`
   * `descripción`
   * `precio`
   * `disponibilidad`
   * `categoria_id` (clave foránea que referencia a la tabla de Categorías)
4. **Carrito de Compra:**
   * `carrito_id` (clave primaria)
   * `usuario_id` (clave foránea que referencia a la tabla de Usuarios)
5. **Productos en Carrito:**
   * `producto_carrito_id` (clave primaria)
   * `carrito_id` (clave foránea que referencia a la tabla de Carrito de Compra)
   * `producto_id` (clave foránea que referencia a la tabla de Productos)
   * `cantidad`
6. **Pedidos:**
   * `pedido_id` (clave primaria)
   * `usuario_id` (clave foránea que referencia a la tabla de Usuarios)
   * `fecha_pedido`
   * `estado` (por ejemplo, pendiente, completado, cancelado)
7. **Detalles del Pedido:**
   * `detalle_pedido_id` (clave primaria)
   * `pedido_id` (clave foránea que referencia a la tabla de Pedidos)
   * `producto_id` (clave foránea que referencia a la tabla de Productos)
   * `cantidad`
   * `precio_unitario`
