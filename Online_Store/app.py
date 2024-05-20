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
@app.route('/carrito_de_compra')
def carrito_de_compra():
    productos_en_carrito = ProductoEnCarrito.query.all()
    productos_info = []
    for producto_en_carrito in productos_en_carrito:

        producto_id = producto_en_carrito.producto_id
        cantidad = producto_en_carrito.cantidad
        producto = Producto.query.get(producto_id)

        if producto:
            nombre = producto.nombre
            precio = producto.precio
            precio_total = precio * cantidad

            productos_info.append({'nombre': nombre, 'cantidad': cantidad, 'precio': precio, 'precio_total': precio_total})

    return render_template('carrito_de_compra.html', productos_info=productos_info)

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


