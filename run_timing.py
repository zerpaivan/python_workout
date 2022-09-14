# script para generar el tiempo promedio de varias carreras.
def runTiming():
    n = 1
    run_time_list = []
    while True:
        r_time = input(f"tiempo en la carrera nº {n} de 10Km: ")
        if not r_time:
            break
        else:
            try:
                run_time_list.append(float(r_time))
                n = n + 1
            except ValueError as val_e:
                print("El valor tiene que ser numerico!. Intente de nuevo")
    
    average_time = sum(run_time_list) / (n - 1)
    print(f"el tiempo promedio es {average_time:.2f}")

runTiming()
