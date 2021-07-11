from dotenv import load_dotenv
from utils import *

load_dotenv()

class BoxDetector:
    """
    Pipeline that uses the utility functions to process document image, separate selection elements
    and find associated text.
    """
    def __init__(self):
        self.client = cloudClientFactory().aws_client()
 
    def run(self, document):
        """Runs pipeline on the input document image.

        Args:
            document (.png, .jpeg): Image of scanned document.

        Returns:
            dict: Selection element text, bounding box and status.
        """
        output = process_document(document, self.client)
        kmap, vmap, bmap = get_kv_map(output)
        results = get_selection_elements(bmap, vmap, kmap)
        return results
