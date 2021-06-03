if __name__ == '__main__':
    print("Estou sendo Executado diretamente no terminal")
    print(__name__)
else:
    print("Estou sendo importado e executado por outro código")
    print(__name__)