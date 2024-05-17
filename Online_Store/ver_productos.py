# store/ver_productos.py
from flask import Flask, render_template
from app import app, db, Producto

@app.route('/ver_productos')
def ver_productos():
    productos = Producto.query.all()
    return render_template('ver_productos.html', productos=productos)
