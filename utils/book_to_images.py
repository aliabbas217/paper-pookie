import fitz
import tqdm
import os

def book_to_images(book_path, output_dir, dpi=300, image_format="png"):
    """
    Convert a PDF book to images.
    
    Parameters:
    book_path (str): Path to the PDF book.
    output_dir (str): Directory to save the images.
    """
    os.makedirs(output_dir, exist_ok=True)
    with fitz.open(book_path) as doc:
        for page_num in tqdm.tqdm(range(len(doc)), desc="Converting pages"):
            page = doc[page_num]
            pix = page.get_pixmap(dpi=dpi)
            pix.save(os.path.join(output_dir, f"page{page_num + 1}.{image_format}"))