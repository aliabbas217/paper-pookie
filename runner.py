from utils.book_to_images import book_to_images
import os

def main():
    book_path = "book/Chemistry-9 complete-2025-26.pdf"
    output_dir = "book/chemistry9_images"

    # Convert the book to images
    book_to_images(book_path, output_dir)
    print(f"Images saved in {output_dir}")

if __name__ == "__main__":
    main()