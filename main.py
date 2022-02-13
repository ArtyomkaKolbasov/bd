from flask import Flask, request, render_template, redirect, url_for, flash
from configuration import app, db
from models import Model, User, Support, Message
from sqlalchemy import *


# fav осталось

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":

        searchtype = request.form.get('searchname')
        searchperpose = request.form.get('searchlogin')
        searchsize = request.form.get('searchsize')

        if searchsize or searchperpose or searchtype:
            if searchsize and not searchperpose and not searchtype:
                user = Model.query.filter_by(size=searchsize).all()
            if not searchsize and searchperpose and not searchtype:
                user = Model.query.filter_by(purpose=searchperpose).all()
            if not searchsize and not searchperpose and searchtype:
                user = Model.query.filter_by(type=searchtype).all()
            if searchsize and searchperpose and not searchtype:
                user = Model.query.filter_by(size=searchsize, purpose=searchperpose).all()
            if searchsize and not searchperpose and searchtype:
                user = Model.query.filter_by(size=searchsize, type=searchtype).all()
            if not searchsize and searchperpose and searchtype:
                user = Model.query.filter_by(purpose=searchperpose, type=searchtype).all()
            if searchsize and searchperpose and searchtype:
                user = Model.query.filter_by(size=searchsize, purpose=searchperpose, type=searchtype).all()

            if user != '':
                return render_template('index.html', prod=user)
            else:
                flash('Не найдено')
                prod = Model.query.all()
                return render_template('index.html', prod=prod)
        else:
            flash('Введите запрос')
            prod = Model.query.all()
            return render_template('index.html', prod=prod)
    else:
        prod = Model.query.all()
        return render_template("index.html", prod=prod)


@app.route('/support', methods=["GET", "POST"])
def support():
    if request.method == "POST":

        searchtype = request.form.get('searchname')
        searchperpose = request.form.get('searchlogin')
        searchsize = request.form.get('searchsize')

        if searchsize or searchperpose or searchtype:
            if searchsize and not searchperpose and not searchtype:
                user = Model.query.filter_by(size=searchsize).all()
            if not searchsize and searchperpose and not searchtype:
                user = Model.query.filter_by(purpose=searchperpose).all()
            if not searchsize and not searchperpose and searchtype:
                user = Model.query.filter_by(type=searchtype).all()
            if searchsize and searchperpose and not searchtype:
                user = Model.query.filter_by(size=searchsize, purpose=searchperpose).all()
            if searchsize and not searchperpose and searchtype:
                user = Model.query.filter_by(size=searchsize, type=searchtype).all()
            if not searchsize and searchperpose and searchtype:
                user = Model.query.filter_by(purpose=searchperpose, type=searchtype).all()
            if searchsize and searchperpose and searchtype:
                user = Model.query.filter_by(size=searchsize, purpose=searchperpose, type=searchtype).all()

            if user != '':
                return render_template('support.html', prod=user)
            else:
                flash('Не найдено')
                prod = Model.query.all()
                return render_template('support.html', prod=prod)
        else:
            flash('Введите запрос')
            prod = Model.query.all()
            return render_template('support.html', prod=prod)

    else:

        prod = Model.query.all()

        return render_template('support.html', prod=prod)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        type = request.form['type']
        purpose = request.form['purpose']
        pattern = request.form['pattern']
        size = request.form['size']
        material = request.form['material']
        consump = request.form['consump']
        plan = request.form['plan']

        model = Model(
            type=type,
            purpose=purpose,
            pattern=pattern,
            size=size,
            material=material,
            consump=consump,
            plan=plan
        )

        try:
            db.session.add(model)
            db.session.commit()
            return redirect(url_for('.support'))
        except:
            print('ERROR')
            return render_template("support.html")
    else:
        return render_template("add.html")


@app.route('/delete/<int:id>')
def delete(id):
    model_to_delete = Model.query.get(id)
    try:
        db.session.delete(model_to_delete)
        db.session.commit()
        return redirect(url_for('.support'))
    except:
        print('ERROR')
        return redirect(url_for('.support'))


@app.route('/update/<int:id>', methods=["GET", "POST"])
def update(id):
    prod1 = Model.query.get(id)

    if request.method == "POST":
        prod1.type = request.form['type']
        prod1.purpose = request.form['purpose']
        prod1.pattern = request.form['pattern']
        prod1.size = request.form['size']
        prod1.material = request.form['material']
        prod1.consump = request.form['consump']
        prod1.plan = request.form['plan']

        try:
            db.session.commit()
            return redirect(url_for('.support'))
        except:
            return "Ошибка обновления"
    else:
        return render_template("update.html", prod1=prod1)


@app.route('/userslist', methods=["GET", "POST"])
def userslist():
    user = []
    if request.method == 'POST':
        name = request.form.get('searchname')
        login = request.form.get('searchlogin')
        if name or login:
            if name and not login:
                user = User.query.filter_by(name=name).all()
            if not name and login:
                user = User.query.filter_by(username=login).all()
            if name and login:
                user = User.query.filter_by(name=name, username=login).all()
            if user:
                return render_template('userslist.html', user=user)
            else:
                flash('Не найдено')
                user = User.query.order_by(User.id).all()
                return render_template('userslist.html', user=user)
        else:
            flash('Введите запрос')
            user = User.query.order_by(User.id).all()
            return render_template('userslist.html', user=user)

    else:
        user = User.query.order_by(User.id).all()
        return render_template('userslist.html', user=user)


@app.route('/chat', methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        userid = request.form.get('userid')
        supportid = request.form.get('supportid')

        if userid or supportid:

            if userid and supportid:
                mes = Message.query.filter_by(user_username=userid, support_username=supportid).all()
            if userid and not supportid:
                mes = Message.query.filter_by(user_username=userid).all()
            if not userid and supportid:
                mes = Message.query.filter_by(support_username=supportid).all()
            if mes:
                return render_template('chat.html', prod=mes)
            else:
                flash('Не найдено')
                mes = Message.query.all()
                return render_template('chat.html', prod=mes)


        else:
            user = request.form['user']
            support = request.form['support']
            msg = request.form['msg']

            model = Message(
                user_username=user,
                support_username=support,
                message=msg
            )

            try:
                db.session.add(model)
                db.session.commit()
                return redirect(url_for('.chat'))
            except:
                print('ERROR')
                return render_template("chat.html")

    else:
        mes = Message.query.all()
        return render_template('chat.html', prod=mes)


@app.route('/deletemes/<int:id>')
def deletemes(id):
    model_to_delete = Message.query.get(id)
    try:
        db.session.delete(model_to_delete)
        db.session.commit()
        return redirect(url_for('.chat'))
    except:
        print('ERROR')
        return redirect(url_for('.chat'))


@app.route('/user', methods=["GET", "POST"])
def user():
    if request.method == "POST":

        searchtype = request.form.get('searchname')
        searchperpose = request.form.get('searchlogin')
        searchsize = request.form.get('searchsize')
        if searchsize or searchperpose or searchtype:
            if searchsize and not searchperpose and not searchtype:
                user = Model.query.filter_by(size=searchsize).all()
            if not searchsize and searchperpose and not searchtype:
                user = Model.query.filter_by(purpose=searchperpose).all()
            if not searchsize and not searchperpose and searchtype:
                user = Model.query.filter_by(type=searchtype).all()
            if searchsize and searchperpose and not searchtype:
                user = Model.query.filter_by(size=searchsize, purpose=searchperpose).all()
            if searchsize and not searchperpose and searchtype:
                user = Model.query.filter_by(size=searchsize, type=searchtype).all()
            if not searchsize and searchperpose and searchtype:
                user = Model.query.filter_by(purpose=searchperpose, type=searchtype).all()
            if searchsize and searchperpose and searchtype:
                user = Model.query.filter_by(size=searchsize, purpose=searchperpose, type=searchtype).all()

            if user != '':
                return render_template('support.html', prod=user)
            else:
                flash('Не найдено')
                prod = Model.query.all()
                return render_template('support.html', prod=prod)

    else:

        prod = Model.query.all()

    prod = Model.query.all()
    return render_template('user.html', prod=prod, support=support)


@app.route('/supportlist', methods=["GET", "POST"])
def supportlist():
    user = []
    if request.method == 'POST':
        name = request.form.get('searchname')
        login = request.form.get('searchlogin')
        if name and not login:
            user = Support.query.filter_by(name=name).all()
            if user:
                return render_template('supportlist.html', user=user)
            else:
                flash('Не найдено')
                return render_template('supportlist.html')

        if not name and login:
            user = Support.query.filter_by(username=login).all()
            if user:
                return render_template('supportlist.html', user=user)
            else:
                flash('Не найдено')
                return render_template('supportlist.html')

        if name and login:
            user = Support.query.filter_by(name=name, username=login).all()
            if user:
                return render_template('supportlist.html', user=user)
            else:
                flash('Не найдено')
                return render_template('supportlist.html')

    else:
        user = Support.query.order_by(Support.id).all()
        return render_template('supportlist.html', user=user)


@app.route('/fav', methods=["GET", "POST"])
def fav():
    # вывести айди юзера и товар, поиск, удаление
    return render_template('fav.html')


@app.route('/chatus', methods=["GET", "POST"])
def chatus():
    if request.method == "POST":
        userid = request.form.get('userid')
        supportid = request.form.get('supportid')

        if userid or supportid:

            if userid and supportid:
                mes = Message.query.filter_by(user_username=userid, support_username=supportid).all()
            if userid and not supportid:
                mes = Message.query.filter_by(user_username=userid).all()
            if not userid and supportid:
                mes = Message.query.filter_by(support_uaername=supportid).all()
            if mes:
                return render_template('chatus.html', prod=mes)
            else:
                flash('Не найдено')

        else:
            user = request.form['user']
            support = request.form['support']
            msg = request.form['msg']

            model = Message(
                user_username=user,
                support_username=support,
                message=msg
            )

            try:
                db.session.add(model)
                db.session.commit()
                return redirect(url_for('.chatus'))
            except:
                print('ERROR')
                return render_template("chatus.html")

    else:
        mes = Message.query.all()
        return render_template('chatus.html', prod=mes)


@app.route('/deletemes1/<int:id>')
def deletemes1(id):
    model_to_delete = Message.query.get(id)
    try:
        db.session.delete(model_to_delete)
        db.session.commit()
        return redirect(url_for('.chatus'))
    except:
        print('ERROR')
        return redirect(url_for('.chatus'))


if __name__ == "__main__":
    app.run(debug=True)
