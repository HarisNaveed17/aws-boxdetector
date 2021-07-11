from dotenv import load_dotenv
from utils import *

load_dotenv()

class BoxDetector:
    """[summary]
    """
    def __init__(self):
        self.client = cloudClientFactory().aws_client()
 
    def run(self, document):
        output = process_document(document, self.client)
        kmap, vmap, bmap = get_kv_map(output)
        results = get_selection_elements(bmap, vmap, kmap)
        return results
