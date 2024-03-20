#include <stdio.h>

void printMultiplesOfSeven() {
	int num;
	printf("Các số nguyên có 2 chữ số và là bội của 7:\n");
	for (num = 14; num < 100; num += 7) {
		printf("%d ", num);
	}
	printf("\n");
}

int main() {
	printMultiplesOfSeven();
	return 0;
}