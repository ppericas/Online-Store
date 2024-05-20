# store/agregar.py
from flask import Flask, render_template, request, redirect, url_for
from app import app, db, Producto, Categoria

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

@app.route('/agregar_categoria', methods=['GET', 'POST'])
def agregar_categoria():
    if request.method == 'POST':
        nombre = request.form['nombre']

        nueva_categoria = Categoria(nombre=nombre)
        db.session.add(nueva_categoria)
        db.session.commit()
        return redirect(url_for('agregar_categoria'))

    return render_template('agregar_categoria.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
