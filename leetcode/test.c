#include<stdio.h>

int main(){

	char* s = "abcd";
	char* t = "abcde";

	char res = 0;
	for(int i = 0; i < 4; i++)
		res ^= s[i];

	for(int i = 0; i < 5; i++)
		res ^= t[i];
	printf("%c", res);
	return 0;
}
