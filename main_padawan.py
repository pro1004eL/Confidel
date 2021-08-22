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









@app.route('/katya_table_19_nea', methods=['POST'])
def katya_table_19_nea():

    if request.method == 'POST':


        username = request.form.get('username') 
        password = request.form.get('password')
        email = request.form.get('email')
        # email = request.form.get('email')
        # reminder_id = 0


        if conn:


            print('CONN =====')

            base_data = (username, password, email)

            p_query = """INSERT INTO public.table_19_nea (username, password, email) VALUES (%s,%s,%s)"""
            cursor.execute(p_query, base_data)

            conn.commit()
            # sl = cursor.execute("select * from public.remind;")

            # print(sl)

            cursor.close()

    succes_message = 'Check added user ' + username

    return succes_message


@app.route('/tanya_mobile', methods=['POST'])
def tanya_mobile():

    if request.method == 'POST':


        device_id = request.form.get('device_id')
        full_name = request.form.get('full_name')
        birthday = request.form.get('birthday')
        # reminder_id = 0


        if conn:


            print('CONN =====')

            base_data = (device_id, full_name, birthday)

            p_query = """INSERT INTO public.remind (device_id, full_name, birthday) VALUES (%s,%s,%s)"""
            cursor.execute(p_query, base_data)

            conn.commit()
            # sl = cursor.execute("select * from public.remind;")

            # print(sl)

            cursor.close()

    succes_message = ''

    return succes_message



def check_token(tkn):


    check_login = tkn.split('/')[2]
    user_exists = False

    if check_login in login_list:
        user_exists = True

    # logging.info('Checked token', tkn)


    return user_exists





@app.route('/')
def first():
    logging.info('User request to /')
    return 'Hello!!'



@app.route('/first')
def second():

    logging.info('User request to /first')
    return 'This is the first responce from server!!!!!'


@app.route('/get_method', methods=['GET', 'POST'])
def get_method():
    if request.method == 'GET':


        name = request.args.get('name')
        age = request.args.get('age')

        logging.info('User %s, %s years request to /get_method', name, age)

        return jsonify(name, age)




@app.route('/alexandra_16_add_python_padawan', methods=['POST'])
def alexandra_16_add_python_padawan():

    id = request.form.get('id')
    name = request.form.get('name')
    age = request.form.get('age')
    future_salary = int(request.form.get('future_salary'))
    country = request.form.get('country')
    city = request.form.get('city')
    email = request.form.get('email')
    phone = request.form.get('phone')
    python_group = request.form.get('python_group')

    future_salary_2 = future_salary*2

    # if conn:
    #     base_data = (id, name, age, future_salary_2, country, city, email, phone, python_group)
    #     # logging.info('volhalysiakova_create_padawan', id, name, age, future_salary, country, city, email, phone,
    #     #              qa_group)
    #     p_query = """INSERT INTO public.python_padawans (id, name, age, future_salary, country, city, email, phone, python_group) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    #     cursor.execute(p_query, base_data)
    #     conn.commit()


    result = 'Hello ' + name + ' your salary will be ' + str(future_salary_2) + '$ in 2 years !!!'

    return jsonify(result)


@app.route('/volhalysiakova_create_padawan', methods=['POST'])
def volhalysiakova_create_padawan():

    if request.method == 'POST':

        id = request.form.get('id')
        name = request.form.get('name')
        age = request.form.get('age')
        future_salary = int(request.form.get('future_salary'))
        country = request.form.get('country')
        city = request.form.get('city')
        email = request.form.get('email')
        phone = request.form.get('phone')
        qa_group = request.form.get('qa_group')



        # logging.info('volhalysiakova_create_padawan', id, name, age, future_salary, country, city, email, phone, qa_group)

        # future_salary = future_salary * 100;
        # try:
        #     str(name)
        # except:
        #     FormatException('name is not string')



        # if conn:
        #     print('CONN =====')
        #     base_data = (id, name, age, future_salary, country, city, email, phone, qa_group)
        #     # logging.info('volhalysiakova_create_padawan', id, name, age, future_salary, country, city, email, phone,
        #     #              qa_group)
        #     p_query = """INSERT INTO public.qa_padawans (id, name, age, future_salary, country, city, email, phone, qa_group) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        #     cursor.execute(p_query, base_data)
        #     conn.commit()
            # sl = cursor.execute("select * from public.pets_3;")

        result = 'Hello' + name + 'your salary will be ' + str(future_salary*4) + 'in five years !!!'
        return jsonify(result)






@app.route('/new_data', methods=['GET', 'POST'])
def new_data():

    # print('POST_POST')

    if request.method == 'POST':

        au_token = request.form.get('auth_token')
        ch_token = check_token(au_token)

        if ch_token:

            name = request.form.get('name')
            age = request.form.get('age')
            salary = int(request.form.get('salary'))

            result = {'name':name,
                    'age': int(age),
                    'salary': [salary, str(salary*2), str(salary*3)]}


            # if conn:
            #
            #     print('CONN =====')
            #     base_data = (str(1), name, str(age), str(salary))
            #
            #
            #     p_query = """INSERT INTO users_2 (ID,NAME,AGE,SALARY) VALUES (%s,%s,%s,%s)"""
            #     cursor.execute(p_query, base_data)
            #
            #     cursor.close()




            # logging.info('User request to /new_data', 'name = ', name, 'age = ', age, 'salary = ', salary)
            return jsonify(result)

        else:
            # logging.info("Invalid token. Sign in please", au_token)
            return jsonify("Invalid token. Sign in please")




@app.route('/user_info', methods=['GET', 'POST'])
def user_info():
    print('POST_POST___')

    if request.method == 'POST':

        print('111 == ', request.json)


        b_token = request.json['auth_token']

        print('b_token', b_token)

        au_token = request.json['auth_token']
        ch_token = check_token(au_token)




        if ch_token:

            age = int(request.json['age'])
            salary = int(request.json['salary'])
            user_name = request.json['name']

            result = {'start_qa_salary':salary,
                    'qa_salary_after_6_months': salary * 2,
                    'qa_salary_after_12_months': salary * 2.9,
                    'person':{'u_name':[user_name, salary, age],
                                'u_age':age,
                                'u_salary_1_5_year': salary * 4}
                                }


            # logging.info('User request to /user_info', 'user_name = ', user_name, 'age = ', str(age), 'salary = ', str(salary))
            return jsonify(result)

        else:
            return jsonify("Invalid token. Sign in please")


@app.route('/user_info2', methods=['GET', 'POST'])
def user_info2():
    print('POST_POST___')

    if request.method == 'POST':

        au_token = request.form.get('auth_token')
        ch_token = check_token(au_token)


        if ch_token:

            age = int(request.form.get('age'))
            salary = int(request.form.get('salary'))
            user_name = request.form.get('name')

            result = {'start_qa_salary':salary,
                    'qa_salary_after_6_months': salary * 2,
                    'qa_salary_after_12_months': salary * 2.9,
                    'person':{'u_name':[user_name, salary, age],
                                'u_age':age,
                                'u_salary_1_5_year': salary * 4}
                                }

            # logging.info('User request to /user_info', 'user_name = ', user_name, 'age = ', str(age), 'salary = ', str(salary))
            return jsonify(result)

        else:
            return jsonify("Invalid token. Sign in please")


@app.route('/lera_test', methods=['POST'])
def lera_test():

    if request.method == 'POST':

        age = int(request.form.get('age'))
        pets = request.form.get('pets')
        pet_food = request.form.get('pet_food')
        pet_color = request.form.get('pet_color')


        result = {'Pet_name': pets,
                  'age': age+1,
                  'pet_food':'Meat',
                  'pet_color': 'Ginger'
                  }

        # cursor = conn.cursor()

        # if conn:
        #     print('CONN =====')
        #     base_data = (pets, str(age), pet_food, pet_color)
        #
        #     p_query = """INSERT INTO pets_3 (Pet_name,age,pet_food,pet_color) VALUES (%s,%s,%s,%s)"""
        #     cursor.execute(p_query, base_data)
        #     conn.commit()
        #     sl = cursor.execute("select * from public.pets_3;")

            # cursor.close()





    return jsonify(result)


@app.route('/ikoshel_test', methods=['POST'])
def ikoshel_test():
    if request.method == 'POST':

        id = int(request.form.get('id'))
        title = request.form.get('title')
        # pet_food = request.form.get('pet_food')
        # pet_color = request.form.get('pet_color')

        result = {'id': id,
                  'title': title
                  }

        # cursor = conn.cursor()

        # if conn:
        #     print('CONN =====')
        #     base_data = (2, title)
        #
        #     p_query = """INSERT INTO public.payment_system (id,system_title) VALUES (%s,%s)"""
        #     cursor.execute(p_query, base_data)
        #     conn.commit()
        #     # sl = cursor.execute("select * from public.pets_3;")
        #
        #     # cursor.close()

    return jsonify(result)



@app.route('/post_method_2', methods=['GET', 'POST'])
def post_method_2():

    if request.method == 'POST':

        return jsonify(request.json, request.json)


@app.route('/test_pet_info', methods=['GET', 'POST'])
def test_pet_info():

    if request.method == 'POST':


        au_token = request.form.get('auth_token')
        ch_token = check_token(au_token)

        if ch_token:
            age = int(request.form.get('age'))
            weight = int(request.form.get('weight'))
            name = request.form.get('name')

            result = {'name': name,
                        'age': age,
                        'daily_food':weight * 0.012,
                        'daily_sleep': weight * 2.5}
            # logging.info('User request to /test_pet_info', 'name = ', name, 'age = ', age, 'weight = ', weight)
            return jsonify(result)

        else:
            return jsonify("Invalid token. Sign in please")


@app.route('/get_test_user', methods=['GET', 'POST'])
def get_user():
    if request.method == 'POST':

        au_token = request.form.get('auth_token')
        ch_token = check_token(au_token)

        if ch_token:
            name = request.form.get('name')
            age = request.form.get('age')
            salary = int(request.form.get('salary'))

            result = {'name': name,
                        'age':age,
                        'salary': salary,
                        'family':{'children':[['Alex', 24],['Kate', 12]],
                        'u_salary_1_5_year': salary * 4}
                        }

            return jsonify(result)

        else:
            return jsonify("Invalid token. Sign in please")


@app.route('/login', methods=['GET', 'POST'])
def test_login():

    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')

        t_token = str('/s34lfgbj/' + str(login) + '/jjd909/' + str(randint(3434, 100023)) + 'kjkWpqc' + str(randint(443, 5467)) + str(password) + str(randint(12, 459086)) + 'evny')

        result = {'token': t_token}
        login_list[str(login)] = t_token

        # logging.info(login_list)


        return jsonify(result)




@app.route('/age_europe', methods=['POST'])
def age_europe():

    # print('POST_POST')

    if request.method == 'POST':

        age = int(request.form.get('age'))

        if age < 18:



            print('age_europe = ', age)

            result_json = {'age': str(age),
                           'age_type': 'underage',
                           'content': ['Tom & Jerry (Feb. 26)',
                                       'Raya and the Last Dragon (Mar. 5)',
                                       'Peter Rabbit 2: The Runaway (April 2)',
                                       'Rumble (May 14)',
                                       'Minions: The Rise of Gru (July 2)',
                                       'Space Jam 2: A New Legacy (July 16)',
                                       'The Addams Family 2 (Oct. 8)',
                                       'Encanto (Nov. 24)']}


            return jsonify(result_json)

        elif age >= 18 and age < 50:

            print('age_europe = ', age)

            result_json = {'age': str(age),
                           'age_type': 'adult',
                           'content': ['Tom & Jerry (Feb. 26)',
                                       'Raya and the Last Dragon (Mar. 5)',
                                       'Peter Rabbit 2: The Runaway (April 2)',
                                       'Rumble (May 14)',
                                       'Minions: The Rise of Gru (July 2)',
                                       'Space Jam 2: A New Legacy (July 16)',
                                       'The Addams Family 2 (Oct. 8)',
                                       'Encanto (Nov. 24)',
                                       'The Matrix 4 (2021)',
                                       'Ghostbusters: Afterlife (2021)',
                                       'Chaos Walking (2021)',
                                       'Eternals (2021)',
                                       'Godzilla vs. Kong (2021)',
                                       'The Tomorrow War (2021)',
                                       'Venom: Let There Be Carnage (2021)',
                                       'Black Widow (2021)',
                                       'Dune (2021)']}

            return jsonify(result_json)

        elif age >= 50 and age < 100:

            print('age_europe = ', age)

            result_json = {'age': str(age),
                           'age_type': 'antiquity',
                           'content': ['An American Pickle',
                                       'The Lovebirds',
                                       'Bill & Ted Face The Music',
                                       'The Personal History Of David Copperfield',
                                       'Emma',
                                       'Happiest Season',
                                       'Spontaneous',
                                       'Palm Springs']}

            return jsonify(result_json)


@app.route('/age_usa', methods=['POST'])
def age_usa():


    if request.method == 'POST':



        age = int(request.form.get('age'))

        if age < 21:

            print('age_usa = ', age)

            result_json = {'age': str(age),
                           'age_type': 'underage',
                           'content': ['Tom & Jerry (Feb. 26)',
                                       'Raya and the Last Dragon (Mar. 5)',
                                       'Peter Rabbit 2: The Runaway (April 2)',
                                       'Rumble (May 14)',
                                       'Minions: The Rise of Gru (July 2)',
                                       'Space Jam 2: A New Legacy (July 16)',
                                       'The Addams Family 2 (Oct. 8)',
                                       'Encanto (Nov. 24)']}


            return jsonify(result_json)

        elif age > 21 and age < 50:

            print('age_usa = ', age)

            result_json = {'age': str(age),
                           'age_type': 'adult',
                           'content': ['Tom & Jerry (Feb. 26)',
                                       'Raya and the Last Dragon (Mar. 5)',
                                       'Peter Rabbit 2: The Runaway (April 2)',
                                       'Rumble (May 14)',
                                       'Minions: The Rise of Gru (July 2)',
                                       'Space Jam 2: A New Legacy (July 16)',
                                       'The Addams Family 2 (Oct. 8)',
                                       'Encanto (Nov. 24)',
                                       'The Matrix 4 (2021)',
                                       'Ghostbusters: Afterlife (2021)',
                                       'Chaos Walking (2021)',
                                       'Eternals (2021)',
                                       'Godzilla vs. Kong (2021)',
                                       'The Tomorrow War (2021)',
                                       'Venom: Let There Be Carnage (2021)',
                                       'Black Widow (2021)',
                                       'Dune (2021)']}

            return jsonify(result_json)

        elif age > 50 and age < 100:

            print('age_usa = ', age)

            result_json = {'age': str(age),
                           'age_type': 'antiquity',
                           'content': ['An American Pickle',
                                       'The Lovebirds',
                                       'Bill & Ted Face The Music',
                                       'The Personal History Of David Copperfield',
                                       'Emma',
                                       'Happiest Season',
                                       'Spontaneous',
                                       'Palm Springs']}

            return jsonify(result_json)





@app.route('/user_info_1', methods=['POST'])
def user_info_1():

    age = int(request.form.get('age'))
    weight = int(request.form.get('weight'))
    name = request.form.get('name')

    result = {'name': name,
              'age': age,
              'daily_food': weight * 0.012,
              'daily_sleep': weight * 2.5}

    return jsonify(result)


@app.route('/user_info_2', methods=['POST'])
def user_info_2():

    age = int(request.form.get('age'))
    salary = int(request.form.get('salary'))
    user_name = request.form.get('name')

    result = {'start_qa_salary': salary,
              'qa_salary_after_6_months': salary * 2,
              'qa_salary_after_12_months': salary * 2.7,
              'qa_salary_after_1.5_year': salary * 3.3,
              'qa_salary_after_3.5_years': salary * 3.8,
              'person': {'u_name': [user_name, salary, age],
                         'u_age': age,
                         'u_salary_5_years': salary * 4.2}
              }

    return jsonify(result)


@app.route('/user_info_3', methods=['POST'])
def user_info_3():
    name = request.form.get('name')
    age = request.form.get('age')
    salary = int(request.form.get('salary'))

    result = {'name': name,
              'age': age,
              'salary': salary,
              'family': {'children': [['Alex', 24], ['Kate', 12]],
                         'u_salary_1_5_year': salary * 4}
              }

    return jsonify(result)


@app.route('/user_info_4', methods=['POST'])
def user_info_4():

    name = request.form.get('name')
    age = request.form.get('age')
    salary = int(request.form.get('salary'))

    result = {'name': name,
              'age': int(age),
              'salary': [salary, str(salary * 2.5), str(salary * 3.5)]}

    return jsonify(result)



@app.route('/object_info_1', methods=['GET'])
def object_info_1():

    age = int(request.args.get('age'))
    weight = int(request.args.get('weight'))
    name = request.args.get('name')

    result = {'name': name,
              'age': age,
              'daily_food': weight * 0.012,
              'daily_sleep': weight * 2.5}

    return jsonify(result)


@app.route('/object_info_2', methods=['GET'])
def object_info_2():

    age = int(request.args.get('age'))
    salary = int(request.args.get('salary'))
    user_name = request.args.get('name')

    result = {'start_qa_salary': salary,
              'qa_salary_after_6_months': salary * 2,
              'qa_salary_after_12_months': salary * 2.7,
              'qa_salary_after_1.5_year': salary * 3.3,
              'qa_salary_after_3.5_years': salary * 3.8,
              'person': {'u_name': [user_name, salary, age],
                         'u_age': age,
                         'u_salary_5_years': salary * 4.2}
              }

    return jsonify(result)


@app.route('/object_info_3', methods=['GET'])
def object_info_3():

    name = request.args.get('name')
    age = request.args.get('age')
    salary = int(request.args.get('salary'))

    result = {'name': name,
              'age': age,
              'salary': salary,
              'family': {'children': [['Alex', 24], ['Kate', 12]],
                         'pets': {'cat':{'name':'Sunny',
                                         'age': 3},
                                  'dog':{'name':'Luky',
                                         'age': 4}},
                         'u_salary_1_5_year': salary * 4}
              }

    return jsonify(result)


@app.route('/object_info_4', methods=['GET'])
def object_info_4():

    name = request.args.get('name')
    age = request.args.get('age')

    salary = int(request.args.get('salary'))

    result = {'name': name,
              'age': int(age),
              'salary': [salary, str(salary * 2), str(salary * 3)]}

    return jsonify(result)