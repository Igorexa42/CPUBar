import plotext as plt
import psutil

def main():
	names = ["CPU", "RAM"]
	percentages = [psutil.cpu_percent(), psutil.virtual_memory().available, ]
	plt.bar(names, percentages)
	plt.title("Resource Control")
	plt.show()

if __name__ == "__main__":
	main()
