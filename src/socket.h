#pragma once
#include "include.h"
#include "error.h"

int makesocket();
void client_connect(int sockfd, char uri[], char cookie[], bool post_flag, char buffer[]);
