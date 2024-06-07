from datetime import datetime
from app import app, db, Usuario, Categoria, Producto, CarritoDeCompra, ProductoEnCarrito, Pedido, DetallePedido

# Crear un contexto de la aplicación Flask
with app.app_context():
    # Crear un nuevo usuario
    nuevo_usuario = Usuario(
        nombre='Nombre del usuario',
        correo_electronico='correo@example.com',
        contraseña='contraseña',
        fecha_registro=datetime.utcnow()
    )

    # Agregar el nuevo usuario a la sesión
    db.session.add(nuevo_usuario)

    # Confirmar los cambios en la base de datos
    db.session.commit()

    nueva_categoria = Categoria(
        nombre='Nombre de la categoría'
    )

    # Agregar la nueva categoría a la sesión
    db.session.add(nueva_categoria)

    # Confirmar los cambios en la base de datos
    db.session.commit()

    nuevo_carrito = CarritoDeCompra(
        usuario_id=1  # Aquí debes especificar el ID del usuario al que pertenece el carrito
    )

    # Agregar el nuevo carrito de compra a la sesión
    db.session.add(nuevo_carrito)

    # Confirmar los cambios en la base de datos
    db.session.commit()

    nuevo_producto_en_carrito = ProductoEnCarrito(
        carrito_id=1,  # Aquí debes especificar el ID del carrito de compra al que pertenece el producto en el carrito
        producto_id=1,  # Aquí debes especificar el ID del producto que se agregará al carrito
        cantidad=2  # Aquí debes especificar la cantidad del producto que se agregará al carrito
    )

    # Agregar el nuevo registro de ProductoEnCarrito a la sesión
    db.session.add(nuevo_producto_en_carrito)

    # Confirmar los cambios en la base de datos
    db.session.commit()

    from app import app, db, Pedido
from datetime import datetime

with app.app_context():
    # Crear un nuevo pedido
    nuevo_pedido = Pedido(
        usuario_id=1,  # Aquí debes especificar el ID del usuario que realiza el pedido
        fecha_pedido=datetime.utcnow(),  # Utiliza la fecha y hora actual del servidor
        estado='En proceso'  # Estado inicial del pedido
    )

    # Agregar el nuevo pedido a la sesión
    db.session.add(nuevo_pedido)

    # Confirmar los cambios en la base de datos
    db.session.commit()

    with app.app_context():
    # Crear un nuevo detalle de pedido
        nuevo_detalle_pedido = DetallePedido(
            pedido_id=1,  # Aquí debes especificar el ID del pedido al que pertenece el detalle
            producto_id=1,  # Aquí debes especificar el ID del producto del detalle
            cantidad=2,  # Aquí debes especificar la cantidad del producto en el detalle
            precio_unitario=10.99  # Aquí debes especificar el precio unitario del producto en el detalle
        )

        # Agregar el nuevo detalle de pedido a la sesión
        db.session.add(nuevo_detalle_pedido)

        # Confirmar los cambios en la base de datos
        db.session.commit()
