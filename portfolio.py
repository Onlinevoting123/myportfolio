from flask import Flask,render_template

portfolio=Flask(__name__)

@portfolio.route('/')
def port():
    return render_template('about.html')

if __name__=='__main__':
    portfolio.run(debug=True,port=9000)
