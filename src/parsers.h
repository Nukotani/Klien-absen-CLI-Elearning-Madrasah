#pragma once
#include "include.h"
#include "error.h"
#include "schedule.h"

char *cookie_parser(char* source);
void account_parser(char data[]);
char *name_parser();
size_t schedule_parser(schedule schedule_array[]);
void login_check(char *response);
