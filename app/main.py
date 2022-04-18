from flask import Flask, request, jsonify
from flask_cors import CORS
from torch_utils import transform_image, get_prediction

app = Flask(__name__)
CORS(app, allow_headers=['Content-Type', 'Access-Control-Allow-Origin',
                         'Access-Control-Allow-Headers', 'Access-Control-Allow-Methods'])
# export FLASK_APP=main.py  export FLASK_ENV=development

CLASS_NAME = [
"rice leaf roller",
"rice leaf caterpillar",
"paddy stem maggot",
"asiatic rice borer",
"yellow rice borer",
"rice gall midge",
"Rice Stemfly",
"brown plant hopper", 
"white backed plant hopper", 
"small brown plant hopper", 
"rice water weevil", 
"rice leafhopper", 
"grain spreader thrips", 
"rice shell pest", 
"grub", 
"mole cricket",
"wireworm",
"white margined moth", 		
"black cutworm", 			    
"large cutworm", 			    
"yellow cutworm", 		        
"red spider", 			        
"corn borer", 			        
"army worm", 			        
"aphids", 			            
"Potosiabre vitarsis", 		
"peach borer", 		     	
"english grain aphid", 		
"green bug", 			        
"bird cherry-oataphid", 		
"wheat blossom midge", 		
"penthaleus major", 			
"longlegged spider mite", 		
"wheat phloeothrips", 			
"wheat sawfly",					
"cerodonta denticornis",			
"beet fly",						
"flea beetle",						
"cabbage army worm",				
"beet army worm",					
"Beet spot flies",					
"meadow moth",						
"beet weevil",						
"sericaorient alismots chulsky", 	
"alfalfa weevil",					
"flax budworm",					
"alfalfa plant bug",				
"tarnished plant bug", 			
"Locustoidea",							
"lytta polita",					
"legume blister beetle", 			
"blister beetle",					
"therioaphis maculata Buckton", 	
"odontothrips loti",				
"Thrips",							
"alfalfa seed chalcid", 			
"Pieris canidia",					
"Apolygus lucorum",				
"Limacodidae",						
"Viteus vitifoliae",				
"Colomerus vitis",					
"Brevipoalpus lewisi McGregor", 	
"oides decempunctata", 			
"Polyphagotars onemus latus",		
"Pseudococcus comstocki Kuwana", 	
"parathrene regalis",				
"Ampelophaga",						
"Lycorma delicatula",				
"Xylotrechus",						
"Cicadella viridis",				
"Miridae",							
"Trialeurodes vaporariorum",						
"Erythroneura apicalis",			
"Papilio xuthus",			
"Panonchus citri McGregor",		
"Phyllocoptes oleiverus ashmead",	
"Icerya purchasi Maskell",			
"Unaspis yanonensis",				
"Ceroplastes rubens",				
"Chrysomphalus aonidum",			
"Parlatoria zizyphus Lucus",		
"Nipaecoccus vastalor",			
"Aleurocanthus spiniferus",		
"Tetradacus c Bactrocera minax",	
"Dacus dorsalis(Hendel)",			
"Bactrocera tsuneonis",			
"Prodenia litura",					
"Adristyrannus",					
"Phyllocnistis citrella Stainton",	
"Toxoptera citricidus",			
"Toxoptera aurantii",				
"Aphis citricola Vander Goot",		
"Scirtothrips dorsalis Hood",		
"Dasineura sp",					
"Lawana imitata Melichar",			
"Salurnis marginella Guerr",		
"Deporaus marginatus Pascoe",		
"Chlumetia transversa",			
"Mango flat beak leafhopper",		
"Rhytidodera bowrinii white",		
"Sternochetus frigidus",			
"Cicadellidae",			 ]

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
def allowed_file(filename):
    # xxx.png
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET'])
def test():
  return jsonify({'message': 'Backend is running'})

@app.route('/predict', methods=['POST'])
def predict():
  if request.method == 'POST':
        file = request.files.get('file')
        if file is None or file.filename == "":
            return jsonify({'error': 'no file'})
        if not allowed_file(file.filename):
            return jsonify({'error': 'format not supported'})

        try:
            img_bytes = file.read()
            tensor = transform_image(img_bytes)
            prediction = get_prediction(tensor)
            data = {'prediction': prediction.item() + 1, 'class_name': CLASS_NAME[prediction.item()]}
            response = jsonify(data)
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response
        except:
            return jsonify({'error': 'error during prediction'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)			        
