# store/agregar.py
from flask import Flask, render_template, request, redirect, url_for
from app import app, db, Producto, Categoria



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
