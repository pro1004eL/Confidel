from flask import Flask, request, jsonify
from random import randint
from datetime import datetime
from datetime import timedelta 
import json, requests
import logging
import psycopg2
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)


SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name':"Seans-Python-Flask-REST-Boilerplate"}
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

logging.basicConfig(filename='logs.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
login_list = {}

conn = psycopg2.connect(dbname='anton_db', user='anton_u', password='123', host='159.69.151.133', port='5056')
cursor = conn.cursor()











# добавить CALLBACK         
@app.route('/callback', methods=['POST'])
def callback():

    name = request.form.get('name')
    phone_number = request.form.get('phone_number')
    current_datetime = datetime.now()+timedelta(hours=1) 

    if conn:

        print('CONN =====')

        base_data = (name, phone_number, current_datetime)

        p_query = """INSERT INTO public.callback (name, phone_number, datetime) VALUES (%s,%s,%s)"""
        cursor.execute(p_query, base_data)

        conn.commit()

    result = 'Callback added successfully!'

    return result


# получить callback список 
@app.route('/get_callback', methods=['GET'])
def get_callback():

    callback_list = []

    if conn:
        print('CONN =====')

        p_query = """SELECT id, name, phone_number, datetime FROM public.callback"""
        cursor.execute(p_query)
        callback_data = cursor.fetchall()

        for callback in callback_data:

            call_id = callback[0]
            call_name = callback[1]
            call_phone_number = callback[2]
            call_datetime = callback[3]

            print('call_name', call_name)

            callback_obj = {'call_id': call_id,
                        'call_name': call_name,
                        'call_phone_number': call_phone_number,
                        'call_datetime': call_datetime}

            callback_list.append(callback_obj)

            print(callback)

    return jsonify(callback_list)


# удалить CALLBACK         
@app.route('/del_callback', methods=['DELETE'])
def del_callback():

    callback_id = request.form.get('id')
    one = int(callback_id) 
    print(one)

    if conn:

        print('CONN =====')

        
        p_query_id = """SELECT id FROM public.callback"""
        cursor.execute(p_query_id)
        count_id = cursor.fetchall()
        list_db = list(count_id)
        print (list_db)

        for i in list_db:
            if i[0] == one:
                base_data = (one)
                p_query = ""f"DELETE FROM public.callback  WHERE id={base_data}""" 
                cursor.execute(p_query, base_data)
                conn.commit()
                result = 'Сallback delete successfully!'
                break

        else:
            result = 'Callback с данным id не существует'
            conn.commit()

    return result

# end callback        



# добавить order            
@app.route('/order_cookie', methods=['POST'])
def order_cookie():

    name = request.form.get('name')
    phone_number = request.form.get('phone_number')
    email = request.form.get('email')
    product_id = int(request.form.get('product_id'))
    count = int(request.form.get('count'))
    current_datetime = datetime.now()+timedelta(hours=1)

    if conn:

        print('CONN =====')

        base_data = (name, phone_number, email, product_id, count, current_datetime)

        p_query = """INSERT INTO public.order_cookie (name, phone_number, email, product_id, count, datetime) VALUES (%s,%s,%s,%s,%s,%s)"""
        cursor.execute(p_query, base_data)

        conn.commit()


    result = 'Order added successfully!'
    
    return result

# end order     

# получить список оредров
@app.route('/get_order_cookie', methods=['GET'])
def get_order_cookie():

    order_cookie_list = []

    if conn:
        print('CONN =====')

        p_query = """SELECT id, name, phone_number, email, product_id, count, datetime FROM public.order_cookie"""
        cursor.execute(p_query)
        order_cookie_data = cursor.fetchall()

        for order_cookie in order_cookie_data:

            order_id = order_cookie[0]
            order_name = order_cookie[1]
            order_phone_number = order_cookie[2]
            order_email = order_cookie[3]
            order_product_id = order_cookie[4]
            order_count = order_cookie[5]
            order_datetime = order_cookie[6]

            print('order_name ', order_name)

            order_cookie_obj = {'order_id': order_id,
                                'order_name': order_name,
                                'order_phone_number': order_phone_number,
                                'order_email': order_email,
                                'order_product_id': order_product_id,
                                'order_count': order_count,
                                'order_datetime': order_datetime}

            order_cookie_list.append(order_cookie_obj)

            print(order_cookie)

    return jsonify(order_cookie_list)

# удалить order
@app.route('/del_order_cookie', methods=['DELETE'])
def del_order_cookie():

    order_id = request.form.get('id')
    one = int(order_id) 
    print(one)

    if conn:

        print('CONN =====')

        
        p_query_id = """SELECT id FROM public.order_cookie"""
        cursor.execute(p_query_id)
        count_id = cursor.fetchall()
        list_db = list(count_id)
        print (list_db)

        for i in list_db:
            if i[0] == one:
                base_data = (one)
                p_query = ""f"DELETE FROM public.order_cookie  WHERE id={base_data}""" 
                cursor.execute(p_query, base_data)
                conn.commit()
                result = 'Order delete successfully!'
                break

        else:
            result = 'Order с данным id не существует'
            conn.commit()

    return result
# end order_cookie            



# добавить product          
@app.route('/product_macaron', methods=['POST'])
def product_macaron():

    name = request.form.get('name')
    price = request.form.get('price')

    if conn:

        print('CONN =====')

        base_data = (name, price)

        p_query = """INSERT INTO public.product_macaron (name, price) VALUES (%s,%s)"""
        cursor.execute(p_query, base_data)

        conn.commit()

 
    result = 'Cookie added successfully!'
    
    return result

# end product    

# получить список product
@app.route('/get_product_macaron', methods=['GET'])
def get_product_macaron():

    macaron_list = []

    if conn:
        print('CONN =====')

        p_query = """SELECT id, name, price FROM public.product_macaron"""
        cursor.execute(p_query)
        product_macaron_data = cursor.fetchall()

        for product_macaron in product_macaron_data:

            pr_id = product_macaron[0]
            pr_name = product_macaron[1]
            pr_price = product_macaron[2]

            print('pr_id', pr_id)

            macaron_obj = {'pr_id': pr_id,
                        'pr_name': pr_name,
                        'pr_price': pr_price}

            macaron_list.append(macaron_obj)

            print(product_macaron)

    return jsonify(macaron_list)

# удалить product
@app.route('/del_product_macaron', methods=['DELETE'])
def del_product_macaron():

    product_id = request.form.get('id')
    one = int(product_id) 
    print(one)

    if conn:

        print('CONN =====')

        
        p_query_id = """SELECT id FROM public.product_macaron"""
        cursor.execute(p_query_id)
        count_id = cursor.fetchall()
        list_db = list(count_id)
        print (list_db)

        for i in list_db:
            if i[0] == one:
                base_data = (one)
                p_query = ""f"DELETE FROM public.product_macaron  WHERE id={base_data}""" 
                cursor.execute(p_query, base_data)
                conn.commit()
                result = 'Product delete successfully!'
                break

        else:
            result = 'Product с данным id не существует'
            conn.commit()

    return result

# end product   

#===================================================================================================                   

