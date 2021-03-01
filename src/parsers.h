#pragma once
#include "include.h"
#include "error.h"
#include "schedule.h"

char *cookie_parser(char* source);
char *account_parser();
char *name_parser();
schedule *schedule_parser(size_t *size);
void login_check(char *response);
