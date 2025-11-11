def main():
    original = "The enemy is strong!"
    new_str = original.replace("enemy", "friend")
    print("Original string:", original)
    print("New string:", new_str)
    print()

    map_description = "A dark cave with a small torch on the wall"

 
    count_a = map_description.lower().count("a")
    print("Descrição do mapa:", map_description)
    print("Número de letras 'a':", count_a)
  
    words = map_description.split()
    print("Palavras da descrição:", words)
    print()


    npcs = ["maul", "plagueis", "bane"]

  
    print("NPCs formatados:")
    for name in npcs:
        cap = name.capitalize()
        print(cap, "->", f"Darth {cap}")
    print()

    word = input("Escreve uma palavra para codificar: ")

    vowels = "aeiouáéíóúàèìòùâêîôûãõAEIOUÁÉÍÓÚÀÈÌÒÙÂÊÎÔÛÃÕ"
    coded = "".join("*" if ch in vowels else ch for ch in word)

    print("Versão codificada:", coded)


if __name__ == "__main__":
    main()
