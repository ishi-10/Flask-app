from flask import Flask, render_template, request

app = Flask(__name__)
quest =['What club was Messi with in Argentina before he moved to Barcelona?',
 'Against who did Messi make his debut for Argentina?',
 'How many La Liga titles has Messi won with Barcelona?',
 "What year did Messi win his first Ballon d'Or and FIFA World Player of the Year awards?",
 "How many “UEFA Men's Player of the Year” award did Messi receive?",
 "What year did Messi receive the Laureus World Sports Award?"]

op=[['River Plate','Boca Juniors',"Newell's Old Boys",'Independiente'],['England','Netherlands','SWitzerland','Hungary'],['6','15','18','10'],
   ['2010','2009','2001','2013'],['4','2','1','None'],['2011','2020','2018','2016']]
ans=["Newell's Old Boys",'Hungary','10','2009','2','2020']

@app.route('/')
def quiz():
    return render_template('content.html',q=quest, o=op)

@app.route('/quiz', methods=['POST']) # specificying POST is important, else you will get 'Method not allowed' error.
def quiz_answers():
    correct = 0
    for i in range(6):
        answered = request.form.get[i]
        if ans[i] == answered:
            correct = correct+1
    return '<h1>Correct Answers: <u>'+str(correct)+'</u></h1>'


if __name__ == "__main__":

    print('starting server')
    app.run(debug=True)
