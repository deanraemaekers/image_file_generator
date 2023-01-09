from craiyon import Craiyon
import sys
generator = Craiyon() # Instantiates the api wrapper
result = generator.generate(sys.argv[1])
result.save_images() # Saves the generated images to 'current working directory/generated', you can also provide a custom path
