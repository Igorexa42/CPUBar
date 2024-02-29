import plotext as plt
import psutil

def main():
	plt.clt()
	plt.cld()
	names = ["CPU", "RAM"]
	percentages = [psutil.cpu_percent(), psutil.virtual_memory().available]
	plt.bar(names, percentages)
	plt.title("Resource Control")
	plt.show()

while __name__ == "__main__":
	main()
