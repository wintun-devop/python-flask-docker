from flask import Blueprint,jsonify,make_response,request
from server.resources.apis import PRODUCT
#import database and model from models
from server.models import db,Products
from server.utils.helper import uuid_string
from server.services.db_session import db_read_session,db_write_session

#authorzation
# from flask_jwt_extended import (
#     jwt_required
#     )

#error handling
from sqlalchemy import exc



#register blue print
product_bp = Blueprint('product', __name__,url_prefix=PRODUCT)
@product_bp.route('/',methods=["POST"])
def create():
    req_body = request.get_json()
    try:
        model = req_body["model_no"]
        is_model_exist=db_read_session.query(Products).filter_by(model_no=model).first()
        if is_model_exist is not None:
            return make_response(jsonify({'status':'fail','msg':'product already exist'}),400)
        new_product = Products(
            name=req_body["name"],
            model_no=model,
            price=req_body["price"]
            )
        db_write_session.add(new_product)
        db_write_session.commit()
        # print(new_product)
        # print("type",type(new_product))
        product=db_read_session.query(Products).filter_by(model_no=model).first()
        response={
            "id":product.id,
            "name":product.name,
            "model_no":product.model_no,
            "qty":product.qty,
            "price":product.price,
            "description":product.description,
            "created_at":product.created_at,
            "updated_at":product.updated_at
            }
        return make_response(jsonify(response),201)
    except exc.SQLAlchemyError as e:
        # db_write_session.rollback()
        print("error",e)
        return make_response(jsonify({"status":"failed","msg":"Internal Server Error"}),500)
    
@product_bp.route('/<id>',methods=["GET"])
# @jwt_required()
def get(id):
    try:
        product = db_read_session.query(Products).filter_by(id=id).first()
        if product is None:
            return make_response(jsonify({"status": "fail", "msg": "Product not found"}), 404)
        response = {
            "id": product.id,
            "name": product.name,
            "qty": product.qty,
            "price": product.price,
            "description": product.description,
            "created_at": product.created_at,
            "updated_at": product.updated_at
        }
        return make_response(jsonify(response), 200)
    except exc.SQLAlchemyError as e:
        print("error", e)
        return make_response(jsonify({"status": "failed", "msg": "Internal Server Error"}), 500)

@product_bp.route('/<id>',methods=["PUT"])
# @jwt_required()
def update(id):
    req_body = request.get_json()
    try:
        product = db_read_session.query(Products).filter_by(id=id).first()
        if product is None:
            return make_response(jsonify({"status": "fail", "msg": "Product not found"}), 404)
        product.name = req_body.get("name", product.name)
        product.model_no = req_body.get("model_no", product.model_no)
        product.price = req_body.get("price", product.price)
        product.qty = req_body.get("qty", product.qty)
        product.description = req_body.get("description", product.description)
        db_write_session.commit()
        response = {
            "id": product.id,
            "name": product.name,
            "model_no": product.model_no,
            "qty": product.qty,
            "price": product.price,
            "description": product.description,
            "created_at": product.created_at,
            "updated_at": product.updated_at
        }
        return make_response(jsonify(response), 200)
    except exc.SQLAlchemyError as e:
        print("error", e)
        return make_response(jsonify({"status": "failed", "msg": "Internal Server Error"}), 500)

@product_bp.route('/<id>', methods=["DELETE"])
# @jwt_required()
def delete(id):
    try:
        # Then proceed with delete as usual
        product = db_write_session.query(Products).filter_by(id=id).first()
        if product is None:
            return make_response(jsonify({"status": "fail", "msg": "Product not found"}), 404)
        # Re-associate product with the write session
        db_write_session.delete(product)
        db_write_session.commit()
        return make_response(jsonify({"status": "success", "msg": "Product deleted"}), 200)
    except exc.SQLAlchemyError as e:
        print("error", e)
        return make_response(jsonify({"status": "failed", "msg": "Internal Server Error"}), 500)
    

@product_bp.route('/all', methods=["GET"])
# @jwt_required()  # Optional, if you want to protect the route
def get_all():
    try:
        products = db_read_session.query(Products).all()
        response = []
        for product in products:
            response.append({
                "id": product.id,
                "name": product.name,
                "model_no": product.model_no,
                "qty": product.qty,
                "price": product.price,
                "description": product.description,
                "created_at": product.created_at,
                "updated_at": product.updated_at
            })
        return make_response(jsonify(response), 200)
    except exc.SQLAlchemyError as e:
        print("error", e)
        return make_response(jsonify({"status": "failed", "msg": "Internal Server Error"}), 500)
