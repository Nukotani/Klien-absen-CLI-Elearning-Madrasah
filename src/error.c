#include "error.h"

void error(const char* error_message) {
	printf(error_message);
	printf("\n[Enter]");
	getchar();
	exit(1);
}
