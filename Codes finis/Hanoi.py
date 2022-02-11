def hanoi(disque: int, start=1, aux=2, end=3) -> list: 
	if disque == 1:
		print(f"Disque {disque}: T{start} --> T{end}") 
	else:
		hanoi(disque - 1, start, end, aux)
		print(f"Disque {disque}: T{start} --> T{end}")
		hanoi(disque - 1, aux, start, end)

hanoi(int(input("nombre de disque : ")))