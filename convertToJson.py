import argparse
import glob
import os
from pathlib import Path
#from src.rdfToJson import convertRDFtoJson
#from src.jsonToJsonld import asJLd

if __name__ == "__main__":
	
	parser = argparse.ArgumentParser()
	parser.add_argument("--generate",help="Generate à JSON-LD au RICO dictionnaire", action='append')
	parser.parse_args("--generate READ --generate FRAME".split())

	parser.add_argument("--input",help="Directory of inputs Files", required=True)
	parser.add_argument("--context",help="Fichier Context", required=False)
	parser.add_argument("--frame",help="Répértoire de fichiers Frame", required=False)
	parser.add_argument("--output",help="Répertoir pour stoker le résultat", required=False)
	
	arg = parser.parse_args()
	# Generate resources
	if 'READ' in arg.generate:

		# All token in the repo
		#for key, value in os.environ.items():
		#	print('{}: {}'.format(key, value))

		print(f"Directory Principal {os.environ["GITHUB_WORKSPACE"]}")
		dir_GITHUB_WORKSPACE = os.environ["GITHUB_WORKSPACE"]
		dirReferentiel = os.path.join(dir_GITHUB_WORKSPACE,"Referentiels")

		#read = convertRDFtoJson(arg.input,arg.output,arg.context)
		#read.convert_data_json()
		inputDirectory = Path(arg.input).absolute()
		#print(f"Directory Parent: {inputDirectory}")
		
		for (root,dirs,files) in os.walk(dirReferentiel):
			print (root)
			print (dirs)
			print (files)
		print("Directory Global")
		
		list_of_files = glob.glob("**/*.rdf",root_dir=dirReferentiel,recursive=True)
		print(list_of_files)
		
	if 'FRAME' in arg.generate:
		# Create a Json-LD Frame
		#asJLd(arg.input,arg.frame,arg.output).frame()
		print(arg.input)
