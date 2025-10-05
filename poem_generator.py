'''
def generate_poem():
    poem = """
    يا بلادي
    فيك طبيعة ساحرة وجمال رباني
    فيك النيل العظيم وسهولك الخضراء
    فيك الكرم والجود وأهلك الطيبين
    يا سودان يا وطني
    """
    return poem

def write_poem_to_file(poem, filename="poem.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(poem)

if __name__ == "__main__":
    poem = generate_poem()
    write_poem_to_file(poem)
    print(f"Poem written to poem.txt")
'''