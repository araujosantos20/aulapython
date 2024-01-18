import ctypes

func = ctypes.CDLL("./saida.so")
func.limpar()
func.sistema()