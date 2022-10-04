for n in range(10):
    for k in range(20):
        for m in range(200):
            if 10000*n + 5000*k + 500*m == 100000 and n+k+m == 100:
                print(f'{ n } быков\n{ k } коров\n{ m } телят')
