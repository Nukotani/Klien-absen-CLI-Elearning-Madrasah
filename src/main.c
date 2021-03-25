#include "socket.h"
#include "error.h"
#include "parsers.h"
#include "schedule.h"

int main(){
	int sockfd = makesocket();
	char response[500];
	schedule schedule_array[5];

	client_connect(sockfd, "/login/do_login", "d", 1, response);
	login_check(response);
	char *cookie = cookie_parser(response);
	size_t schedule_size = schedule_parser(schedule_array); 
	close(sockfd);
	memset(response, 0, 500);
	for (size_t i = 0; i < schedule_size; i++) {
		sockfd = makesocket();
		printf("Mengisi absen %s\n", schedule_array[i].name);
		client_connect(sockfd, schedule_array[i].link, cookie, 0, response);
		printf("berhasil\n");
		close(sockfd);
		memset(response, 0, strlen(response));
	}
	return 0;
}
