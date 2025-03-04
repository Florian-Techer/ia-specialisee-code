
from flask import Flask,render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.stats import pearsonr
from lifxlan import LifxLAN

# Init
num_lights = None
lifx = LifxLAN(num_lights)
lifx.get_power_all_lights()
 # Textes à comparer 
texts = [ 
   "Le traitement du langage naturel est fascinant.", 
   "Le traitement des langues est une branche de l'intelligence artificielle.", 
   "L'analyse de texte est utilisée pour la traduction automatique.",
   "Allumer la lampe de la salle 505",
   "Allume la cuisine",
   "Eteint la cuisine",
   "Allume le salon",
   "Eteint le salon"
]



app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/lamp')
def lamp():
    query = request.args.get('query')
    # Allumer
    lifx.set_power_all_lights("on")
    # Eteindre
    lifx.set_power_all_lights("off")
    texts.insert(0, query)  # Ajoute 1 à l'index 0

    # Vectorisation TF-IDF
    vect = TfidfVectorizer()
    tfidf_mat = vect.fit_transform(texts).toarray()
    query_tf_idf = tfidf_mat[0]
    corpus = tfidf_mat[1:]


    # Corellation de pearson
    for id, document_tf_idf in enumerate(corpus):
      pearson_corr, _ = pearsonr(query_tf_idf, document_tf_idf)
      if pearson_corr > 0.20:
         result = {"ID": id, "document": texts[id+1], "similarity": pearson_corr}
         return result
    # return render_template('index.html')


@app.route('/search', methods=['GET'])
def search():
   print("tab")
   print(texts)
   query = request.args.get('query')
   texts.insert(0, query)  # Ajoute 1 à l'index 0

   # Vectorisation TF-IDF
   vect = TfidfVectorizer()
   tfidf_mat = vect.fit_transform(texts).toarray()

   query_tf_idf = tfidf_mat[0]
   corpus = tfidf_mat[1:]


   # Corellation de pearson
   for id, document_tf_idf in enumerate(corpus):
      pearson_corr, _ = pearsonr(query_tf_idf, document_tf_idf)
      if pearson_corr > 0.80:
         result = {"ID": id, "document": texts[id+1], "similarity": pearson_corr}
         print("result")
         print(result["document"])
        #  if result.document

   return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
