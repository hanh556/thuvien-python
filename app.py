from flask import Flask, render_template
from flask_pymongo import PyMongo
import config
from routes.user_routes import user_routes

app = Flask(__name__)

# Kết nối MongoDB
app.config["MONGO_URI"] = config.MONGO_URI
mongo = PyMongo(app)
app.mongo = mongo

# Route trang chủ (giữ nguyên)
@app.route('/')
def home():
    return render_template("index.html")
    # name = "Anh"
    # return render_template("index.html", username=name)

@app.route('/trangluu')
def trangluu():
    return render_template("trangluu.html")
    
# Trang admin
@app.route('/admin')
def admin_dashboard():
    return render_template("admin/dashboard.html")

# Đăng ký route người dùng (users)
app.register_blueprint(user_routes)

if __name__ == '__main__':
    app.run(debug=True)
