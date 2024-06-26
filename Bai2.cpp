﻿#include <stdio.h>
#include <math.h>

// Hàm kiểm tra số chính phương
int isPerfectSquare(int num) {
	int squareRoot = sqrt(num);
	return (squareRoot * squareRoot == num);
}

// Hàm đếm và in ra các số chính phương nhỏ hơn n
void printPerfectSquares(int n) {
	printf("Cac so chinh phuong nho hon %d la:\n", n);
	int count = 0;
	for (int i = 1; i < n; i++) {
		if (isPerfectSquare(i)) {
			printf("%d ", i);
			count++;
		}
	}
	printf("\nTong so chinh phuong: %d\n", count);
}

int main() {
	int n;
	printf("Nhap so nguyen duong n: ");
	scanf("%d", &n);
	printPerfectSquares(n);
	return 0;
}