from flask import Flask, render_template
app = Flask(__name__)

lorem_ipsum = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Lacus sed turpis tincidunt id aliquet risus. Vitae semper quis lectus nulla. Sagittis aliquam malesuada bibendum arcu vitae elementum curabitur. Facilisis volutpat est velit egestas dui id ornare arcu odio. Sagittis id consectetur purus ut faucibus. Ultricies lacus sed turpis tincidunt. Felis eget velit aliquet sagittis id consectetur. Ullamcorper malesuada proin libero nunc consequat interdum. Nunc sed velit dignissim sodales ut eu sem integer vitae. Dolor sit amet consectetur adipiscing elit pellentesque.Proin nibh nisl condimentum id venenatis a condimentum. Etiam erat velit scelerisque in dictum non. Sapien et ligula ullamcorper malesuada. Orci nulla pellentesque dignissim enim sit amet venenatis urna. Massa placerat duis ultricies lacus sed. Arcu vitae elementum curabitur vitae nunc sed velit dignissim. Mattis pellentesque id nibh tortor id aliquet lectus proin. Purus faucibus ornare suspendisse sed nisi lacus sed viverra. Quis commodo odio aenean sed adipiscing diam. Vitae suscipit tellus mauris a diam.'

articles = [{'id': 1, 'author': "Donald Trump", 'title': "Hitler snýr aftur", 'content': lorem_ipsum},
            {'id': 2, 'author': "Guðni T.H.", 'title': "Buff í stað Hjálma!", 'content': lorem_ipsum},
            {'id': 3, 'author': "Hillary Clinton", 'title': "9/11 aftur", 'content': lorem_ipsum}]
author, title, content = '', '', ''
lenA = len(articles)

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/frett/<ID>')
def sida1(ID):
	for x in range(lenA):
		if int(ID) == articles[x]['id']:
			author = articles[x]['author']
			title = articles[x]['title']
			content = articles[x]['content']
	return render_template('verk3.html', id=ID, author=author, title=title ,content=content, len=lenA)
if __name__ == "__main__":
	app.run(debug=True)

@app.errorhandler(404)
def error404(error):
    return '<br><br><h1 style="text-align: center;">ERROR 404</h1><h2 style="text-align: center;">page not found<h2>'