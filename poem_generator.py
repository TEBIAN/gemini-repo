import random

def generate_poem():
    poems = [
        """
        يا بلادي
        فيك طبيعة ساحرة وجمال رباني
        فيك النيل العظيم وسهولك الخضراء
        فيك الكرم والجود وأهلك الطيبين
        يا سودان يا وطني
        """,
        """
        يا وطني يا بلد
        يا حبيب يا سند
        فيك الخير اتولد
        وبيك الخير انوجد
        """,
        """
        سودانا فوق
        فوق السحاب
        رمز الشموخ
        رمز الإباء
        """
    ]
    return random.choice(poems)

def write_poem_to_file(poem, filename="poem.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(poem)

if __name__ == "__main__":
    poem = generate_poem()
    write_poem_to_file(poem)
    print(f"Poem written to poem.txt")
