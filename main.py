from imagem import Imagem

def main():
    for i in range(1,4,1):
        img = Imagem('foto{}.jpg'.format(i))
        print(img)


if __name__ == "__main__":
    main()