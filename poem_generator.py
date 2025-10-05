import random

def generate_poem_with_llm():
    """
    This function should be updated to call a Large Language Model (LLM)
    to generate a poem in Sudanese Arabic.
    """
    # Replace this with your LLM API call
    # For example, using a hypothetical 'llm' library:
    # from llm import generate
    # prompt = "Write a short poem in Sudanese Arabic about the Nile river."
    # return generate(prompt)

    # For now, returning a random poem from a predefined list.
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
    poem = generate_poem_with_llm()
    write_poem_to_file(poem)
    print(f"Poem written to poem.txt")
