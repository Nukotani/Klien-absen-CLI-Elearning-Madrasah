#include "parsers.h"

char* substring(char* haystack, int offset, int length){
	char* result;
	int i = 0;
	result = calloc(1, sizeof result);
	while (offset < length - 1) {
		result = realloc(result, (i + 1) * sizeof result);
		result[i] = haystack[offset];
		i++;
		offset++;
	}
	result = realloc(result, (i + 1) * sizeof result);
	result[i] = '\0';
	return result;
}

int search_char(char* source) {
	int i = 0;
	while(source[i] != '=') {
		i++;
	}
	return i++;
}

char *cookie_parser(char *source) {
	char *re; 
	regex_t regex;	
	regmatch_t pmatch[1];
	regoff_t offset, length;

	re = "PHPSESSID=.*;";
	if (regcomp(&regex, re, REG_EXTENDED | 	REG_NEWLINE))
		error("parsing cookie gagal#1");
	if (regexec(&regex, source, sizeof pmatch / sizeof pmatch[0], pmatch, 0))
		error("parsing cookie gagal#0");
	return substring(source, pmatch[0].rm_so, pmatch[0].rm_eo);
}
char *account_parser() {
	char *buffer, *data;
	buffer = calloc(255, sizeof buffer);
	data = calloc(1, sizeof data);
	FILE *account_file;
	account_file = fopen("akun", "r");
	if (account_file == NULL)
		error("gagal membuka file akun");
	while(fgets(buffer, 255, account_file) != NULL) {
		data = realloc(data, (strlen(data) + 2 + strlen(buffer)) * sizeof data);
		strtok(buffer, "\n");
		strcat(data, buffer);
		strcat(data, "&");
	}
	data = realloc(data, (strlen(data) + 13) * sizeof data);
	strcat(data, "ajaran=2020");
	free(buffer);
	fclose(account_file);
	return data;
}
schedule *schedule_parser(size_t *size) {
	char *buffer, *control, *filename;
	schedule *schedule_array;
	FILE *schedule_file;
	time_t seconds = time(NULL);
	struct tm *time_structured = localtime(&seconds);
	int i = 0, weekday = time_structured->tm_wday, pos;

	switch(weekday) {
		case 0:
			error("ini hari minggu bre");
			break;
		case 1:
			control = "Mon";
			break;
		case 2:
			control = "Tue";
			break;
		case 3:
			control = "Wed";
			break;
		case 4:
			control = "Thu";
			break;
		case 5:
			control = "Fri";
			break;
		case 6:
			control = "Sat";
			break;
		default:
			error("gagal mencoocokkan hari");
			break;
	}
	filename = calloc(8, sizeof filename);
	strcpy(filename, "jadwal/");
	filename = realloc(filename, (strlen(filename) + strlen(control) + 1) * sizeof filename);
	strcat(filename, control);

	buffer = calloc(255, sizeof buffer);
	schedule_array = calloc(1, sizeof(schedule));

	schedule_file = fopen(filename, "r");
	if (schedule_file == NULL)
		error("gagal membuka file jadwal");
	while(fgets(buffer, 255, schedule_file) != NULL) {
		schedule_array = realloc(schedule_array, (i + 1) * sizeof(schedule));
		pos = search_char(buffer);
		schedule_array[i].name = substring(buffer, 0, pos + 1);
		schedule_array[i].link = substring(buffer, pos + 1, strlen(buffer));
		i++;
	}
	*size = i;
	free(filename);
	free(buffer);
	fclose(schedule_file);

	return schedule_array;
}
void login_check(char *response) {
	char *re;	
	regex_t regex;	
	regoff_t offset, length;

	re = "student";
	if (regcomp(&regex, re, REG_EXTENDED | REG_NEWLINE))
		error("login gagal! periksa password atau username");
	if (regexec(&regex, response, 0, NULL, 0))
		error("login gagal! periksa password atau username");
	puts("berhasil login");
}
