from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')  # 首页
def home(): 
    return render_template('index.html')

@app.route('/about')  # 关于我们
def about(): 
    return render_template('about.html')

@app.route('/news')  # 资讯
def news(): 
    return render_template('news.html')

@app.route('/business')  # 页面2：商家服务
def business(): 
    return render_template('business.html')

@app.route('/consumer')  # 页面3：消费者服务
def consumer(): 
    return render_template('consumer.html')

@app.route('/rider')  # 页面4：骑手服务
def rider(): 
    return render_template('rider.html')

@app.route('/profile')  # 个人中心
def profile(): 
    return render_template('profile.html')

# 以下是第二层子页面（页面6-13）的路由
@app.route('/service/6')  # 页面6
def service_6(): 
    return render_template('service_6.html')

@app.route('/service/7')  # 页面7
def service_7(): 
    return render_template('service_7.html')

@app.route('/service/8')  # 页面8
def service_8(): 
    return render_template('service_8.html')

@app.route('/service/9')  # 页面9
def service_9(): 
    return render_template('service_9.html')

@app.route('/service/10')  # 页面10
def service_10(): 
    return render_template('service_10.html')

@app.route('/service/11')  # 页面11
def service_11(): 
    return render_template('service_11.html')

@app.route('/service/12')  # 页面12
def service_12(): 
    return render_template('service_12.html')

@app.route('/service/13')  # 页面13
def service_13(): 
    return render_template('service_13.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)