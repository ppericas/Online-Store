from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template,redirect,request,url_for


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mi_base_de_datos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Usuario(db.Model):
    __tablename__ = 'usuarios'
    usuario_id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo_electronico = db.Column(db.String(120), unique=True, nullable=False)
    contraseña = db.Column(db.String(200), nullable=False)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
    carritos = db.relationship('CarritoDeCompra', backref='usuario', lazy=True)
    pedidos = db.relationship('Pedido', backref='usuario', lazy=True)

class Categoria(db.Model):
    __tablename__ = 'categorias'
    categoria_id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    productos = db.relationship('Producto', backref='categoria', lazy=True)

class Producto(db.Model):
    __tablename__ = 'productos'
    producto_id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(500))
    precio = db.Column(db.Float, nullable=False)
    disponibilidad = db.Column(db.Boolean, default=True)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.categoria_id'), nullable=False)
    productos_en_carrito = db.relationship('ProductoEnCarrito', backref='producto', lazy=True)
    detalles_pedido = db.relationship('DetallePedido', backref='producto', lazy=True)
    url_imagen = db.Column(db.String(255))

class CarritoDeCompra(db.Model):
    __tablename__ = 'carritos_de_compra'
    carrito_id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.usuario_id'), nullable=False)
    productos_en_carrito = db.relationship('ProductoEnCarrito', backref='carrito', lazy=True)

class ProductoEnCarrito(db.Model):
    __tablename__ = 'productos_en_carrito'
    producto_carrito_id = db.Column(db.Integer, primary_key=True)
    carrito_id = db.Column(db.Integer, db.ForeignKey('carritos_de_compra.carrito_id'), nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.producto_id'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)

class Pedido(db.Model):
    __tablename__ = 'pedidos'
    pedido_id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.usuario_id'), nullable=False)
    fecha_pedido = db.Column(db.DateTime, default=datetime.utcnow)
    estado = db.Column(db.String(50), nullable=False)
    detalles_pedido = db.relationship('DetallePedido', backref='pedido', lazy=True)

class DetallePedido(db.Model):
    __tablename__ = 'detalles_pedido'
    detalle_pedido_id = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedidos.pedido_id'), nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.producto_id'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    precio_unitario = db.Column(db.Float, nullable=False)


@app.route('/agregar_producto', methods=['GET', 'POST'])
def agregar_producto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        precio = float(request.form['precio'])
        disponibilidad = request.form.get('disponibilidad') == 'on'
        categoria_id = int(request.form['categoria'])

        nuevo_producto = Producto(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            disponibilidad=disponibilidad,
            categoria_id=categoria_id
        )
        db.session.add(nuevo_producto)
        db.session.commit()
        return redirect(url_for('agregar_producto'))

    return render_template('agregar_producto.html')

@app.route('/ver_productos', methods=['GET'])
def ver_productos():
    productos = Producto.query.all()
    print(productos)
    return render_template('ver_productos.html', productos=productos)
@app.route('/carrito_de_compra',methods=['GET', 'POST'])
def carrito_de_compra():
        # Realizar una consulta para obtener información de productos en el carrito y sus detalles
        productos_en_carrito = db.session.query(ProductoEnCarrito, Producto).\
            join(ProductoEnCarrito.producto).all()

        # Crear una lista de diccionarios con la información de los productos en el carrito
        productos_info = []
        for producto_en_carrito, producto in productos_en_carrito:
            print("Nombre del producto:", producto.nombre)
            print("Descripción del producto:", producto.descripcion)
            print("Precio del producto:", producto.precio)
            print("Cantidad en el carrito:", producto_en_carrito.cantidad)
            print("URL de la imagen del producto:", producto.url_imagen)

            productos_info.append({
                'producto_carrito_id': producto_en_carrito.producto_carrito_id, 
                'nombre': producto.nombre,
                'descripcion': producto.descripcion,
                'precio': producto.precio,
                'cantidad': producto_en_carrito.cantidad,
                'url_imagen': producto.url_imagen
            })

        print("Productos en el carrito:", productos_info)

        return render_template('carrito_de_compra.html', productos_info=productos_info)

@app.route('/borrar_productos_seleccionados', methods=['POST'])
def borrar_productos_seleccionados():
    data = request.get_json()
    productos_seleccionados = data.get('productos', [])
    for producto_id in productos_seleccionados:
        producto_en_carrito = ProductoEnCarrito.query.filter_by(producto_carrito_id=producto_id).first()
        if producto_en_carrito:
            db.session.delete(producto_en_carrito)
            db.session.commit()
    return jsonify({'message': 'Productos eliminados correctamente'})

@app.route('/eliminar_producto_carrito', methods=['POST'])
def eliminar_producto_carrito():
    accion = request.form['accion']
    if accion == 'borrar':
        productos_a_borrar = request.form.getlist('borrar_producto')
        # Aquí puedes realizar la lógica para borrar los productos seleccionados
    elif accion == 'pagar':
        return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)


