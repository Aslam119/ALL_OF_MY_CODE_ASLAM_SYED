from flask import Flask,render_template,redirect,session,request

def findMovie(movie):
    import requests

    url = "https://imdb8.p.rapidapi.com/auto-complete"

    querystring = {"q":f"{movie}"}

    headers = {
        'x-rapidapi-key': "fd594f3563msh3d486a0bb27d35bp10467ajsn23bb828965ec",
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = response.json()
    d = data['d']
    n = len(d)
    imgs = []
    titles = []
    years = []
    n = len(d)

    for x in range(n):
        try:
            imgs.append(d[x]['i']['imageUrl'])
            titles.append(d[x]['l'])
            years.append(d[x]['y'])
        except Exception as e:
            pass    
    details = {
        'titles': titles,
        'years': years,
        'images': imgs,
        'count': len(titles)
    }
    return details

app = Flask(__name__)
@app.route('/',methods=['POST','GET'])
def home():
    if request.method == "POST":
        query = request.form['query']
        result = findMovie(f"{query}")
        return render_template('index.html',title=result['titles'],year=result['years'],image=result['images'],count=result['count'])
    else:
        return render_template('index2.html')

if __name__ == '__main__':
    app.run(debug=True)