def run():
    with open('numeros.txt', 'w') as f:
        for i in range(10):
            f.write(str(i) + '\n')


if __name__ == '__main__':
    run()
